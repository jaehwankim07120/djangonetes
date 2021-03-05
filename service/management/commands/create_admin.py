from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create a default superuser'

    def handle(self, *args, **options):
        User.objects.create_superuser('admin', 'admin@djangonetes.com', 'adminadmin')
