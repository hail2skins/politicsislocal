# auth_app/mail_backend.py
from django.core.mail.backends.base import BaseEmailBackend
from .mail import send_email
# Import settings
from django.conf import settings

class MailjetEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        for message in email_messages:
            send_email(
                from_email=settings.DEFAULT_FROM_EMAIL,
                from_name=settings.DEFAULT_FROM_NAME,
                to_email=message.to[0],
                subject=message.subject,
                text_content=message.body,
                html_content=message.body,
            )