from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="DRF JWT API",
        default_version='v0.1',
        description="Api for test task",
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
        path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]