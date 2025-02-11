from django.db.models.signals import post_save
from django.core.signals import request_started, request_finished, got_request_exception
from django.dispatch import receiver
from .models import Student, MyUser
from django.core.mail import send_mail

@receiver(post_save, sender=MyUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Our App!"
        message = f"Hello {instance.username},\n\nThank you for signing up for our app. We are excited to have you onboard!\n\nBest Regards,\nYour App Team"
        from_email = "mohitz.official23@gmail.com"  # Replace with your email
        recipient_list = [instance.email]  # Send email to the new user

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
@receiver(request_started)
def before_request(sender, environ, **kwargs):
    print("A new request has started!")

@receiver(request_finished)
def after_request(sender, **kwargs):
    print("A request has finished processing.")

@receiver(got_request_exception)
def request_error(sender, request, **kwargs):
    print("An error occurred in a request.")