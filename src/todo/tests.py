from unittest.mock import patch

from factory.django import DjangoModelFactory
from pytest import mark
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIClient

from .models import Todo
from .views import TodoViewSet


class TodoFactory(DjangoModelFactory):
    class Meta:
        model = Todo


@mark.django_db
def test_list():
    TodoFactory.create()
    TodoFactory.create()

    client = APIClient()
    response = client.get('/todos', format='json')
    assert 2 == len(response.data)


# override_settings doesn't work
# https://stackoverflow.com/questions/29367043/unit-testing-django-rest-framework-authentication-at-runtime
# @override_settings(REST_FRAMEWORK={
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# })
@patch.object(TodoViewSet, 'permission_classes', new=[IsAuthenticated])
@mark.django_db
def test_list_permission():
    TodoFactory.create()
    TodoFactory.create()

    client = APIClient()
    response = client.get('/todos', format='json')
    assert 403 == response.status_code
