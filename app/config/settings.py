from pydantic import BaseSettings, BaseModel

class Settings(BaseSettings):
    user_email: str 
    csv_file_path: str
    sendgrid_api_key: str
    sendgrid_email_sender: str
    google_application_credentials: str
    google_cloud_bucket_name: str = 'test'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "jobsity_ingestion_api"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }