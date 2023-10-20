from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from back.users.serializers import UserSerializer, GroupSerializer
from rest_framework.generics import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # Customize create and update user so the password can be hashed
    def create(self, request, *args, **kwargs):
        user = User.objects.create_user(
            username=request.data.get('username'),
            email=request.data.get('email'),
        )
        # hash password
        user.set_password(request.data.get('password'))
        message = 'User created successfully'
        return Response(message, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        password = request.data.get('password')
        user = get_object_or_404(User, pk=user_id)

        # hash password if it is provided
        if password:
            user.set_password(password)
            
        # update user
        user.save()
        message = 'user updated successfully'
        return Response(message, status=status.HTTP_200_OK)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
