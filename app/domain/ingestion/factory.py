from app.models.ingestion import IngestionRequest
from app.domain.ingestion.use_cases import CreateIngestion
from app.config import settings

class IngestionFactory:

    @staticmethod
    def from_request(request: IngestionRequest):

        user_email = request.user_email or settings.user_email
        file_path = settings.csv_file_path

        ingestion = CreateIngestion(user_email, file_path)

        return ingestion