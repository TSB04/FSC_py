from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import SheetsSerializer
from .models import SheetsModel

class SheetsViewSet(viewsets.ModelViewSet):
    queryset = SheetsModel.objects.all()

    serializer_class = SheetsSerializer

    def create(self, request, *args, **kwargs):
        serializer = SheetsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        sheet_ine = kwargs.get('ine')
        sheet = get_object_or_404(SheetsModel, ine=sheet_ine)

        serializer = self.get_serializer(sheet)
        return Response(serializer.data, status=status.HTTP_200_OK)