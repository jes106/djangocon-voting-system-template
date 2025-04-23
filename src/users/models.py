from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    groups = ["User"]
    user_permissions = [("normal_user", "User who can vote and see results")]


class Admin(AbstractUser):
    groups = ["Admin"]
    user_permissions = [("admin_user", "User who create and manage votings")]