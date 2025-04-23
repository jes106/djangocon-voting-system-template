from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.request import Request

@api_view(["POST"])
def login(request: Request):
    username = request.POST["email"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response(status=200, data={"message": "You are logged in"})
    
    else:
        return Response(status=400, data={"error": "Failed login"})
    
@api_view
@login_required
def logout(request: Request):
    logout(request)