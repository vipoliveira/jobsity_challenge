from app.infrastructure.storage.google_cloud.client import GoogleCloudStorageClient
from app.config import settings

class CreateIngestion:
    
    def __init__(self, email: str, file_path: str):
        self.__email = email
        self.__file_path = file_path

    def execute(self):
        
        return self.upload_file_to_bucket()
    
    def upload_file_to_bucket(self):

        source_file_path = settings.csv_file_path
        destination_file_blob = f"csv/{source_file_path.split('/')[-1]}"

        google_cloud_storage_client = GoogleCloudStorageClient()
        result =  google_cloud_storage_client.upload_file_to_blob(source_file_path, destination_file_blob)

        return result

    