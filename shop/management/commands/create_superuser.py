from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            admin = User.objects.create_superuser(email="a@a.ru", username='admin', password='mystrongadminpassword')
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            self.stdout.write('Superuser was created!')
