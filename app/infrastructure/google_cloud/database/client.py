from google.cloud import bigquery
from app.config import logger

class GoogleCloudBigqueryClient:

    def __init__(self) -> None:
        self.bigquery_client = bigquery.Client()

    def create_table_from_blob(self, blob_uri: str, table_name: str):

        table_name = f'{self.bigquery_client.project}.jobsity.{table_name}'

        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            skip_leading_rows=1,
            source_format=bigquery.SourceFormat.CSV
        )

        load_job = self.bigquery_client.load_table_from_uri(blob_uri, table_name, job_config=job_config)
        logger.info(f"Starting job {load_job.job_id}.")
        logger.warning(f'When the job completes you will be notified: {load_job.result()}')

        return self.bigquery_client.get_table(table_name)


