from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentsSerializer
from .models import CommentsModel
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = CommentsModel.objects.all()

    serializer_class = CommentsSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @swagger_auto_schema(
        operation_description="Create comment",
        responses={201: openapi.Response('Comment created', CommentsSerializer)},
        response_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'exampleTest': openapi.Schema(type=openapi.TYPE_STRING, description='Example descroption'),

            },
            required=['exampleTest']
        )
    )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        message = 'comment created successfully'
        return Response(message, serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        comment_id = kwargs.get('pk')
        comment = get_object_or_404(CommentsModel, id=comment_id)

        serializer = self.get_serializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        comment_id = kwargs.get('pk')
        comment = get_object_or_404(CommentsModel, pk=comment_id)

        serializer = self.get_serializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        message = 'comment updated successfully'
        return Response(message, serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        comment_id = kwargs.get('pk')
        comment = get_object_or_404(CommentsModel, pk=comment_id)

        comment.delete()
        message = 'comment deleted successfully'
        return Response(message,status=status.HTTP_204_NO_CONTENT)
