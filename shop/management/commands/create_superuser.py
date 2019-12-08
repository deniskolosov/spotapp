from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shop.models import Customer


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            admin = User.objects.create_superuser(email="a@a.ru", username='admin', password='mystrongadminpassword')
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            self.stdout.write('Created superuser')
        else:
            self.stdout.write('Superuser was already created!')
