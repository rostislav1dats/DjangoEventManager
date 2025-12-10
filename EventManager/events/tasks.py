from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_event_email(organizer_email, title, date, location):
    subject = f'Event created: {title}'
    message = (
        f'Hello!!! You are successfully created event.\n\n'
        f'Name: {title}\n'
        f'Date: {date}\n'
        f'Place: {location}\n\n'
        f'Thanks for using our app!!!'
    )
    send_mail(
        subject,
        message,
        None,
        [organizer_email],
        fail_silently=False
    )