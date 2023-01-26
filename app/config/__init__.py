from app.config.settings import Settings, LogConfig
import logging

settings = Settings(_env_file=".env", _env_file_encoding='utf-8')

logging.config.dictConfig(LogConfig().dict())
logger = logging.getLogger("jobsity_ingestion_api")