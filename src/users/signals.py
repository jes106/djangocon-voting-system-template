from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from django.conf import settings

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    try:
        from src.users.models import Admin
        if not Admin.objects.filter(username='admin').exists():
            Admin.objects.create(
                username='admin',
                email='admin@example.com',
                password='admin_password',
            )
            print('Superusuario creado con éxito.')
    except Exception as e:
        print(f'Error al crear el superusuario: {e}')
