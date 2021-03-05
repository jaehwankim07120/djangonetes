from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Djangonetes API 1.0",
        default_version="v1.0.0.210226-a1",
        description="Djangonetes Alpha Version API Doc",
        terms_of_service="",
        contact=openapi.Contact(name="Bart Kim", email="jaehwankim07120@gmail.com"),
        license=openapi.License(name="Djangonetes License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def get_urlpatterns():
    if settings.DEBUG:
        return [
        re_path(r'^api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^api/v1/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^api/v1/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),   
    ]
    else:
        return []
