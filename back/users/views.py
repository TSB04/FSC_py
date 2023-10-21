from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from back.security.permissions import IsPostRequest
from rest_framework.permissions import IsAuthenticated
from back.users.serializers import UserSerializer
from rest_framework.generics import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        if self.action == 'create':
            permission_classes = [IsPostRequest]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    # Customize create and update user so the password can be hashed

    def create(self, request, *args, **kwargs):
        password = request.data.get('password')

        # only need to check password since username is required by default
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


