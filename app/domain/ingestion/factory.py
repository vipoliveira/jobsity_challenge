from app.models.ingestion import PipelineBase
from app.domain.ingestion import AbstractPipeline
from app.domain.ingestion.use_cases import CreateIngestion, CreateIngestionGrouped, GetWeeklyAverageOfTrips
from app.config import logger

class PipelineFactory:

    INGESTIONS_MAPPING = {
        'PipelineRequest': CreateIngestion,
        'PipelineGroupRequest': CreateIngestionGrouped, 
        'PipelineWeeklyAverageRequest': GetWeeklyAverageOfTrips
    }

    @staticmethod
    def from_request(request: PipelineBase) -> AbstractPipeline:

        params = request.dict()
        ingestion = PipelineFactory.INGESTIONS_MAPPING.get(request.__repr_name__())

        return ingestion(**params)