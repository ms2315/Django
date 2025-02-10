from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from django.core.mail import send_mail

@receiver(post_save, sender=Student)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print("Send Email")
        
