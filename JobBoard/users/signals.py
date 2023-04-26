from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Employer


# @receiver(post_save, sender=[Profile, Employer])
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        if isinstance(instance, Employer):
            employer = Employer.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                name=user.username,
            )
        else:
            profile = Profile.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                name=user.username,
            )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)

post_save.connect(createProfile, sender=Employer)
post_delete.connect(deleteUser, sender=Employer)
