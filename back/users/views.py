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
        password = request.data.get('password')

        # only need to check password since username is required
        if password:
            user = User.objects.create_user(**request.data)
            user.set_password(password)
            message = 'user created successfully'
            return Response(message, status=status.HTTP_201_CREATED)
        return Response('password is required', status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        password = request.data.get('password')
        user = get_object_or_404(User, pk=user_id)

        # hash password if it is provided
        if password:
            user.set_password(password)
            user.save()
            message = 'user updated successfully'
            return Response(message, status=status.HTTP_200_OK)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        message = 'user updated successfully'
        return Response(message, status=status.HTTP_200_OK)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
