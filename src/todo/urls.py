from django.urls import include, path
from rest_framework import routers

from .views import TodoViewSet

# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
