from pydantic import BaseModel


class PipelineBase(BaseModel):
    user_email: str = "your_email@example.com.br"
    ingestion_name: str = 'default'
    table_name: str = 'trips'

class PipelineRequest(PipelineBase):
    pass


class PipelineGroupRequest(PipelineBase):
    fields: list = ['region', 'origin_coord', 'destination_coord', 'datetime']
    output_table_name: str = 'trips_grouped'


class PipelineWeeklyAverageRequest(PipelineBase):
    latitude1: int
    latitude2: int
    longitude1: int
    longitude2: int