from fastapi import FastAPI
from app.models.ingestion import IngestionRequest
from app.domain.ingestion.factory import IngestionFactory

app = FastAPI()

@app.post("/ingestion")
async def create_ingestion(ingestion: IngestionRequest):

    ingestion_job = IngestionFactory.from_request(ingestion)
    result = ingestion_job.execute()

    return result