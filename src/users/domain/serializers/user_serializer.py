from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    username = serializers.IntegerField()
    password = serializers.CharField()
    email = serializers.DateTimeField()