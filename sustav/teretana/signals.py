from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from teretana.models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    # Ensure that we are creating an user instance, not updating it
    if created:
        Profile.objects.create(user=instance)