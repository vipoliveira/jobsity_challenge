from abc import abstractmethod, ABC
from app.config import settings
from app.infrastructure.email_server.sendgrid.client import SendgridMailClient


class AbstractPipeline(ABC):

    def __init__(self, user_email, ingestion_name, **kwargs) -> None:
        self.__user_email = user_email or settings.user_email
        self.__ingestion_name = ingestion_name
        self.extra_params = kwargs

    def notify_user(self):
        SendgridMailClient.send_email(
            from_email=settings.sendgrid_email_sender,
            to_emails=self.__user_email,
            subject='Important message | Status of your ingestion from jobsity platform',
            html_content=f'<strong> Your ingestion {self.__ingestion_name} finished! </strong>'
        )

    @abstractmethod
    def execute(self, **kwargs):
        raise NotImplementedError()