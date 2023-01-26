from app.config import settings
from google.cloud import storage

class GoogleCloudStorageClient:

    def __init__(self) -> None:
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(settings.google_cloud_bucket_name)    

    def upload_file_to_blob(self, file_path, destination_blob_name):
        blob = self.bucket.blob(destination_blob_name)

        blob.upload_from_filename(file_path)
        
        return "File uploaded"