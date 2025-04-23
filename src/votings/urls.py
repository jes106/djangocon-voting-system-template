from django.urls import path
from .controllers import update_voting_controller, create_voting_controller, delete_voting_controller, get_owned_votes_controller, get_active_votings_controller

urlpatterns = [
    path('/create', create_voting_controller, name='create-voting'),
    path('/update/<str:voting_id>', update_voting_controller, name='update-voting'),
    path('/delete/<str:voting_id>', delete_voting_controller, name='delete-voting'),
    path('/owned', get_owned_votes_controller, name='owned-voting'),
    path('/active', get_active_votings_controller, name='active-voting'),
]