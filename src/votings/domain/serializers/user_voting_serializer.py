from rest_framework import serializers

class VotingUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    winners = serializers.IntegerField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()