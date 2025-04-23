from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from src.users.domain.serializers.user_serializer import UserSerializer
from src.users.views import create_user, create_admin_user

@login_required
@api_view(['POST'])
def create_user_controller(request: Request):
    if not request.user.has_perm("admin_user"):
        return PermissionError("You are not authorized to perform this action")

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = create_user(serializer)
        return Response(status=200, data={'id': f'{user.id}', 'username': f'{user.username}'})
    else:
        return Response(status=400, data=serializer.errors)


@login_required
@api_view(['POST'])
def create_admin_controller(request: Request):
    if not request.user.has_perm("admin_user"):
        return PermissionError("You are not authorized to perform this action")

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        admin = create_admin_user(serializer)
        return Response(status=200, data={'id': f'{admin.id}', 'username': f'{admin.username}', 'role': 'admin'})
    else:
        return Response(status=400, data=serializer.errors)

