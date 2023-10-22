from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from back.stars.models import StarsModel
from .serializers import StarsSerializer




class StarsViewSet(viewsets.ModelViewSet):
    queryset = StarsModel.objects.all()

    serializer_class = StarsSerializer

    def give_star(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        message = 'star given successfully'
        return Response(message, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        star_id = kwargs.get('pk')
        star = get_object_or_404(StarsModel, pk=star_id)

        serializer = self.get_serializer(star, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        message = 'star updated successfully'
        return Response(message, status=status.HTTP_200_OK)
    
    