from pydantic import BaseModel

class IngestionRequest(BaseModel):
    user_email: str = "your_email@example.com.br"