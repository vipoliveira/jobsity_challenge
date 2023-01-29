from datetime import datetime
from threading import Thread
from time import sleep
from app.domain.ingestion import AbstractPipeline
from app.config import settings
from app.models import PipelineRequestDefaultTable
from app.infrastructure.google_cloud.storage.client import GoogleCloudStorageClient
from app.infrastructure.google_cloud.database.client import GoogleCloudBigqueryClient


class CreateIngestion(AbstractPipeline):

    def __init__(self, user_email, ingestion_name, **kwargs) -> None:

        self.__google_cloud_bigquery_client = GoogleCloudBigqueryClient()
        self.__google_cloud_storage_client = GoogleCloudStorageClient()

        super().__init__(user_email, ingestion_name, **kwargs)

    def execute(self):

        blob_uri = self.__persist_file()
        table_name = self.extra_params.get('table_name')
        table_id = self.__create_data_product(blob_uri=blob_uri, table_name=table_name)

        table_created_date = None
        while not isinstance(table_created_date, datetime):
            table_created_date = self.__google_cloud_bigquery_client.get_table_by_name(table_name)
            sleep(10)

        async_notifify_user = Thread(target=self.notify_user, name='async_notifify_user')
        async_notifify_user.start()

        return {"table_id": table_id}
    
    def __persist_file(self):

        source_file_path = settings.csv_file_path
        file_name = source_file_path.split('/')[-1]
        destination_file_blob = f"csv/{file_name}"

        file_uri =  self.__google_cloud_storage_client.upload_file_to_blob(source_file_path, destination_file_blob)

        return file_uri

    def __create_data_product(self, **kwargs):
        
        kwargs['schema'] = PipelineRequestDefaultTable.get_schema()
        return self.__google_cloud_bigquery_client.create_table_from_blob(**kwargs)


class CreateIngestionGrouped(AbstractPipeline):

    def __init__(self, user_email, ingestion_name, **kwargs) -> None:

        self.__google_cloud_bigquery_client = GoogleCloudBigqueryClient()

        super().__init__(user_email, ingestion_name, **kwargs)
    
    def execute(self, **kwargs):

        table_name = self.extra_params.get('table_name')
        fields = self.extra_params.get('fields')
        output_table_name = self.extra_params.get('output_table_name')

        table_id = self.__create_data_product(table_name, output_table_name, fields)

        table_created_date = None
        while not isinstance(table_created_date, datetime):
            table_created_date = self.__google_cloud_bigquery_client.get_table_by_name(output_table_name)
            sleep(10)

        return {"table_id": table_id}
    
    def __create_data_product(self, table_ref, output_table, fields):

        project_id = self.__google_cloud_bigquery_client.project_id
        dataset_id = self.__google_cloud_bigquery_client.dataset_id
        input_table_id = f'{project_id}.{dataset_id}.{table_ref}'
        output_table_id = f'{project_id}.{dataset_id}.{output_table}'
        fields_for_query = ', '.join(fields)

        query = f"""
        CREATE TABLE {output_table_id} AS (
            SELECT
                {fields_for_query},
                COUNT(*) AS qtde
            FROM
                {input_table_id}
                GROUP BY {fields_for_query}
        );
        """

        self.__google_cloud_bigquery_client.execute_query(query)

        return output_table_id
    

class GetWeeklyAverageOfTrips(AbstractPipeline):

    def __init__(self, user_email, ingestion_name, **kwargs) -> None:

        self.__google_cloud_bigquery_client = GoogleCloudBigqueryClient()

        super().__init__(user_email, ingestion_name, **kwargs)
    
    def execute(self, **kwargs):

        table_name = self.extra_params.get('table_name')
        latitude1 = self.extra_params.get('latitude1')
        latitude2 = self.extra_params.get('latitude2')
        longitude1 = self.extra_params.get('longitude1')
        longitude2 = self.extra_params.get('longitude2')

        result = self.__create_data_product(table_name, latitude1, latitude2, longitude1, longitude2)

        return {"result": result}
    
    def __create_data_product(self, table_ref, latitude1, latitude2, longitude1, longitude2):

        project_id = self.__google_cloud_bigquery_client.project_id
        dataset_id = self.__google_cloud_bigquery_client.dataset_id
        input_table_id = f'{project_id}.{dataset_id}.{table_ref}'

        query = f"""
            SELECT
                region,
                EXTRACT(WEEK FROM datetime) as week,
                COUNT(*) as weekly_trips
            FROM {input_table_id}
                WHERE ST_INTERSECTSBOX(destination_coord, {latitude1}, {latitude2}, {longitude1}, {longitude2})
            GROUP BY 1, 2
        """

        query_result = self.__google_cloud_bigquery_client.execute_query(query)
        result = list(query_result)

        return result