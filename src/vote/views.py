from django.shortcuts import render
from src.vote.models import Vote
from src.vote.domain.serializers.vote_serializer import VoteSerializer

# Create your views here.
def get_all_votes(voting):
    votes = Vote.objects.filter(voting=voting)

    normalized_votes = []

    for vote in votes:
        normalized_votes.append(VoteSerializer(data=vote))

    return normalized_votes


def create_vote(vote: VoteSerializer):
    pass