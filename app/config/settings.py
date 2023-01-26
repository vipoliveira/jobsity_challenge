from pydantic import BaseSettings

class Settings(BaseSettings):
    user_email: str 
    csv_file_path: str
    google_application_credentials: str
    google_cloud_bucket_name: str = 'test'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'