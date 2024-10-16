# disaster_management/utils.py
import logging
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth import get_user_model

def send_alert_notification(alert):
    User = get_user_model()  # Use the custom user model
    users = User.objects.filter(receive_alert_notifications=True)
    
    subject = f'New Alert: {alert.alert_message}'
    message = f'An alert has been created:\n\n{alert.alert_message}\n\nView details: http://127.0.0.1:8000/alerts/'  # Adjust the URL accordingly
    recipient_list = [user.email for user in users if user.email]

    if recipient_list:  # Only send email if there are recipients
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        except BadHeaderError:
            logging.error(f"Invalid header found while sending email for alert {alert.id}")
        except Exception as e:
            logging.error(f"Failed to send email for alert {alert.id}: {e}")
