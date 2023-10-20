from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import IsGetRequest
from .serializers import SheetsSerializer
from .models import SheetsModel
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SheetsViewSet(viewsets.ModelViewSet):
    queryset = SheetsModel.objects.all()

    serializer_class = SheetsSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsGetRequest]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(
        operation_description="Create sheet",
        responses={201: openapi.Response('Sheet created', SheetsSerializer)},
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        sheet_ine = kwargs.get('ine')
        sheet = get_object_or_404(SheetsModel, ine=sheet_ine)

        serializer = self.get_serializer(sheet)
        return Response(serializer.data, status=status.HTTP_200_OK)