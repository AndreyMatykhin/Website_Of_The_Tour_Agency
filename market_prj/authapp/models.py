# from tarfile import TruncatedHeaderError

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class BuyerUser(AbstractUser):
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")],
                                    unique=True)


class BuyerUserProfile(models.Model):
    SILVER = 'S'
    GOLD = 'G'
    PLATINUM = 'P'
    LEVEL_CHOICES = ((SILVER, 'S'), (GOLD, 'G'), (PLATINUM, 'P'),)

    user = models.OneToOneField(BuyerUser, unique=True, null=False,
                                db_index=True, on_delete=models.CASCADE)
    buyer_level = models.CharField(verbose_name='Уровень покупателя', max_length=1, choices=LEVEL_CHOICES, blank=True,
                                   default='S')
    location = models.CharField(verbose_name='Адрес', max_length=128, blank=True)

    @receiver(post_save, sender=BuyerUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            BuyerUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=BuyerUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.buyeruserprofile.save()
