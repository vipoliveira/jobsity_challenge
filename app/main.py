from fastapi import FastAPI, HTTPException
from app.models.ingestion import PipelineRequest, PipelineGroupRequest, PipelineWeeklyAverageRequest
from app.domain.ingestion.factory import PipelineFactory

app = FastAPI()

@app.post("/create_ingestion")
async def create_ingestion(ingestion: PipelineRequest):
    
    try:
        ingestion_job = PipelineFactory.from_request(ingestion)
        result = ingestion_job.execute()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f'An error ocurred: {e}'
        )

    return result

@app.post("/create_grouped_data")
async def create_grouped_data(ingestion: PipelineGroupRequest):

    try:
        ingestion_job = PipelineFactory.from_request(ingestion)
        result = ingestion_job.execute()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f'An error ocurred: {e}'
        )

    return result

@app.post("/get_weekly_average_number_of_trips")
async def get_weekly_average_number_of_trips(ingestion: PipelineWeeklyAverageRequest):

    try:
        ingestion_job = PipelineFactory.from_request(ingestion)
        result = ingestion_job.execute()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f'An error ocurred: {e}'
        )

    return result
