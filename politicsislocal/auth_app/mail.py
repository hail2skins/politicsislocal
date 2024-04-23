# auth_app/mail.py
from mailjet_rest import Client
 # Import the settings module
from django.conf import settings


def send_email(from_email, from_name, to_email, subject, text_content, html_content):
    # Your Mailjet API key and secret
    api_key = settings.MAILJET_API_KEY
    api_secret = settings.MAILJET_API_SECRET
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
    'Messages': [
        {
        "From": {
            "Email": from_email,
            "Name": from_name,
        },
        "To": [
            {
            "Email": to_email,
            }
        ],
        "Subject": subject,
        "TextPart": text_content,
        "HTMLPart": html_content,
        #"CustomID": "AppGettingStartedTest",
        }
    ]
    }


    result = mailjet.send.create(data=data)
    return result.status_code
