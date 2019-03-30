from django.urls import include, path
from rest_framework import routers

from .views import (
  CommentViewSet,
  TodoViewSet,
)

# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'todos', TodoViewSet)
router.register(
      r'todos/(?P<todo_id>\d)/comments',
      CommentViewSet,
      basename='todo_comment',
  )

urlpatterns = [
    path('api/', include(router.urls)),
]
