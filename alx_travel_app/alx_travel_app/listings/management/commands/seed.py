from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No user found. Create a user first.'))
            return

        for i in range(5):
            Listing.objects.create(
                title=f'Sample Listing {i+1}',
                description='A nice place to stay.',
                location='Ethiopia',
                price_per_night=random.randint(50, 200),
                host=user,
            )
        self.stdout.write(self.style.SUCCESS('Sample listings created.'))
