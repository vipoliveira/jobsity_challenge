from pydantic import BaseSettings

class Settings(BaseSettings):
    user_email: str 
    csv_file_path: str
    #https://drive.google.com/file/d/14JcOSJAWqKOUNyadVZDPm7FplA7XYhrU/view?usp=sharing

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'