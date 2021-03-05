from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Build Service'


    def handle(self, *args, **options):
        print('Build..')