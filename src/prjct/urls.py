"""prjct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework.schemas import get_schema_view
from rest_framework.renderers import OpenAPIRenderer


urlpatterns = [
    re_path(r'^', include('todo.urls')),
]

if settings.DEBUG:
    #  https://www.django-rest-framework.org/api-guide/schemas/#the-get_schema_view-shortcut
    schema_view = get_schema_view(
        title="Server Monitoring API",
        urlconf=urlpatterns,
        url='http://localhost:8000/api/',
        renderer_classes=[OpenAPIRenderer],
    )
    urlpatterns += [
        re_path('openapi/', schema_view),
        path('admin/', admin.site.urls),
    ]
