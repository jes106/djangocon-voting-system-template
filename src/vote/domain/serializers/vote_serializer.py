from rest_framework import serializers

class VoteSerializer(serializers.Serializer):
    options = serializers.JSONField()