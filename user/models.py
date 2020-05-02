from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    TYPE_USER = (
        (1, 'author'),
        (2, 'buyer'),
    )    
    user_type = models.PositiveSmallIntegerField(choices=TYPE_USER)


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')
    address = models.TextField()
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_buyer_profile(sender, instance, created, **kwargs):
    if created:
        Buyer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_buyer_profile(sender, instance, **kwargs):
    instance.buyer.save()
