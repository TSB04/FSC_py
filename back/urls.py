from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from back.users import views as users_views
from back.sheets import views as sheets_views
from back.comments import views as comments_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Free library API",
        default_version="v1"
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'sheets', sheets_views.SheetsViewSet)
router.register(r'comments', comments_views.CommentsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('comments/', comments_views.CommentsViewSets.as_view({'get': 'list'}), name='comments'),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
