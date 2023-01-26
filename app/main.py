from fastapi import FastAPI, HTTPException
from app.models.ingestion import IngestionRequest
from app.domain.ingestion.factory import IngestionFactory

app = FastAPI()

@app.post("/create_ingestion")
async def create_ingestion(ingestion: IngestionRequest):
    
    try:
        ingestion_job = IngestionFactory.from_request(ingestion)
        result = ingestion_job.execute()
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f'An error ocurred: {e}'
        )

    return result