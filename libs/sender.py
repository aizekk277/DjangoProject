from django.core.mail import send_mail

from core import settings

send_mail(
    subject="Hello"
    message="Hello"
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[ubarakanov11@gmail.com]
)