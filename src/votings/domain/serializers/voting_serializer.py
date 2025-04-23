from rest_framework import serializers

class VotingSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    status = serializers.CharField()
    winners = serializers.IntegerField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    voting_creator = serializers.IntegerField()
    last_update = serializers.DateTimeField()