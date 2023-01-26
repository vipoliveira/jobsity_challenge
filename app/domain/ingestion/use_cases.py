from app.infrastructure.google_cloud.storage.client import GoogleCloudStorageClient
from app.infrastructure.google_cloud.database.client import GoogleCloudBigqueryClient
from app.config import settings

class CreateIngestion:
    
    def __init__(self, email: str, file_path: str):
        self.__email = email
        self.__file_path = file_path

    def execute(self):
        
        blob_uri, file_name = self.persist_file()
        file_name_without_type = file_name.split('.')[0]

        result = self.create_data_product(blob_uri, file_name_without_type)
        
        return {"message": {"result": result}}
    
    def persist_file(self):

        source_file_path = settings.csv_file_path
        file_name = source_file_path.split('/')[-1]
        destination_file_blob = f"csv/{file_name}"

        google_cloud_storage_client = GoogleCloudStorageClient()
        file_uri =  google_cloud_storage_client.upload_file_to_blob(source_file_path, destination_file_blob)

        return file_uri, file_name

    def create_data_product(self, *args, **kwargs):

        google_cloud_bigquery_client = GoogleCloudBigqueryClient()
        
        return google_cloud_bigquery_client.create_table_from_blob(*args, **kwargs)

