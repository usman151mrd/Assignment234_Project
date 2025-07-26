
from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(email_confirmed)
def set_email_verified(sender, request, email_address, **kwargs):
    user = email_address.user
    #user.is_email_verified = True
    user.save()
