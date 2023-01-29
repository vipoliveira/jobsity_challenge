from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.config import settings, logger

class SendgridMailClient:

    @staticmethod
    def send_email(
        from_email: str, 
        to_emails: str, 
        subject: str, 
        html_content: str):
        
        try:
            kwargs = locals()
            email = Mail(**kwargs) 

            sendgrid_client = SendGridAPIClient(settings.sendgrid_api_key)
            logger.info('Sending email')
            response = sendgrid_client.send(email)
            logger.info(f'Response code from sendgrid: {response.status_code}')

            return response
            
        except Exception as e:
            logger.error(f'An exception ocurred while sending an email: {e}')
