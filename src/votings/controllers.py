from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.request import Request
from src.votings.domain.serializers.voting_serializer import VotingSerializer
from src.votings.domain.exceptions import VotingNotFoundError
from src.votings.views import create_voting, update_voting, delete_voting, get_active_votings, get_owned_votes
from datetime import datetime

@api_view(['POST'])
@login_required
def create_voting_controller(request: Request):
    if not request.user.has_perm("admin_user"):
        return PermissionError("You don't have permission to perform this action")
    
    # Create a copy of the data sent to the voting and set
    # the creator and the last update by the system
    voting_data = request.data.copy()
    voting_data["voting_creator"] = 1234
    voting_data["last_update"] = datetime.now()

    # Create the serializer for the voting data, check if
    # is valid and create it
    serializer = VotingSerializer(data=voting_data)
    if serializer.is_valid():
        voting = create_voting(serializer)
        return Response(status=200, data={'id': f'{voting.id}'})
    else:
        return Response(status=400, data=serializer.errors)

@api_view(['PUT'])
@login_required
def update_voting_controller(request: Request, voting_id: str):
    if not request.user.has_perm("admin_user"):
        return PermissionError("You don't have permission to perform this action")
    

    voting_data = request.data.copy()
    voting_data["voting_id"] = voting_id
    serializer = VotingSerializer(data=voting_data)
    if serializer.is_valid():
        voting = update_voting(serializer)
        return Response(status=200, data={'id': f'{voting.id}'})
    else:
        return Response(status=400, data=serializer.errors)

@api_view(['DELETE'])
@login_required
def delete_voting_controller(request: Request, voting_id: str):
    if not request.user.has_perm("admin_user"):
        return PermissionError("You don't have permission to perform this action")
    
    try:
        voting = delete_voting(voting_id, request.user.id)
        return Response(status=200, data={'id': f'{voting.id}'})
    except Exception as e:
        return Response(status=400, data={'error': f"The voting process couldn't be deleted because of: {e}"})

@api_view(['GET'])
@login_required
def get_active_votings_controller(request: Request):
    active_votings = get_active_votings()

    if not active_votings:
        return Response(status=404, data=VotingNotFoundError("No voting found"))
    
    else:
        return Response(status=200, data={voting.to_representation() for voting in active_votings})

@api_view(['GET'])
@login_required
def get_owned_votes_controller(request: Request):
    if not request.user.is_authenticated:
        return PermissionError("You can't perform this actions no logged")
    try:
        owned_votes = get_owned_votes(request.user.id)
    except Exception as e:
        return Response(status=400, data={"error": e})

    if owned_votes:
        return Response(status=200, data={voting.to_representation for voting in owned_votes})
    else:
        return Response(status=404, data=VotingNotFoundError("You don't have owned votings"))