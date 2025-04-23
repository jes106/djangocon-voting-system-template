from django.urls import path
from .controllers import create_user_controller, create_admin_controller

urlpatterns = [
    path('/signup', create_user_controller, name='create-user'),
    path('/createadmin', create_admin_controller, name='create-admin'),
]