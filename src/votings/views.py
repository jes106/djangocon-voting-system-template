from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler

from src.votings.domain.serializers.voting_serializer import VotingSerializer
from src.votings.domain.serializers.user_voting_serializer import VotingUserSerializer
from src.votings.models import Voting
from src.users.models import Admin
from src.votings.domain.exceptions import VotingNotFoundError, VotingNotOwnedError
from src.vote.views import get_all_votes

def create_voting(voting: VotingSerializer):
    voting = Voting(**voting.validated_data)
    voting.save()

    scheduler = BackgroundScheduler()
    scheduler.add_job(solve_voting, 'date', run_date=voting.end_date, args=[voting.id])
    scheduler.start()

    return voting

def update_voting(voting: VotingSerializer, user_id: str):
    voting_original = Voting.objects.get(id=voting.id)

    if not voting_original:
        return VotingNotFoundError("The voting wasn't found")
    
    if voting_original.voting_creator.id != user_id:
        return VotingNotOwnedError("You can't update a voting that's not yours")
    
    else:
        voting_original.update(validated_data=voting.validated_data)

def delete_voting(voting_id: str, user_id: str):
    voting = Voting.objects.get(id=voting_id)

    if not voting:
        return VotingNotFoundError("The voting wasn't found")
    
    if voting.voting_creator.id != user_id:
        return VotingNotOwnedError("You can't delete a voting that's not yours")
    
    voting.delete() 

def get_active_votings():
    votings = Voting.objects.filter(status="Active")

    normalized_voting = []

    for voting in votings:
        normalized_voting.append(VotingUserSerializer(data=voting))
    return normalized_voting

def get_owned_votes(user_id: str):
    user = Admin.objects.get(id=user_id)
    
    if not user:
        return AttributeError("The user you give is not Admin or doesn't exists")

    votings_owned = Voting.objects.filter(votings_creator=user)

    normalized_voting = []

    for voting in votings_owned:
        normalized_voting.append(VotingSerializer(data=voting))
    return normalized_voting

def solve_voting(voting_id: str):
    votes = get_all_votes()

    # Here is where you have to use your algorithm to obtain the winner

    voting = Voting.objects.get(id=voting_id)
    voting.status = "Closed"
    voting.update()
    