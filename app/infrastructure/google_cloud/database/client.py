from google.cloud import bigquery
from app.config import logger
from datetime import datetime

class GoogleCloudBigqueryClient:

    def __init__(self) -> None:
        self.__bigquery_client = bigquery.Client()
        self.dataset_id = 'jobsity'
        self.project_id = self.__bigquery_client.project

    def create_table_from_blob(self, blob_uri: str, table_name: str, schema = None):

        table_id = f'{self.project_id}.{self.dataset_id}.{table_name}'

        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            skip_leading_rows=1,
            source_format=bigquery.SourceFormat.CSV
        )

        if schema:
            job_config.schema = schema

        load_job = self.__bigquery_client.load_table_from_uri(blob_uri, table_id, job_config=job_config)
        logger.info(f"Starting job {load_job.job_id}.")

        result = load_job.result()
        logger.warning(f'When the job completes you will be notified: {result}')
            
        return table_id

    def get_table_by_name(self, table_name: str) -> datetime:
        table_id = f'{self.project_id}.{self.dataset_id}.{table_name}'
        table = self.__bigquery_client.get_table(table_id)
        
        return table.created


    def execute_query(self, query: str):

        query_job = self.__bigquery_client.query(query)

        return query_job.result()