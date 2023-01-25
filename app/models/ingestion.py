from pydantic import BaseModel

class IngestionRequest(BaseModel):
    user_email: str