from django.core.management.base import BaseCommand

from authapp.models import BuyerUser, BuyerUserProfile


class Command(BaseCommand):
    help = 'Update DB'
    def handle(self, *args, **options):
        users = BuyerUser.objects.all()
        for user in users:
            users_profile = BuyerUserProfile.objects.create(user=user)
            users_profile.save()