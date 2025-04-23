from src.users.models import User, Admin

# Create your views here.
def create_user(user_serializer):
    user = User.create(**user_serializer.validated_data)
    user.save()
    return user

def create_admin_user(user_serializer):
    user = Admin.create(**user_serializer.validated_data)
    user.save()
    return user