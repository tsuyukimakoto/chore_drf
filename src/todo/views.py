from rest_framework import viewsets

from .models import (
    Comment,
    Todo,
)
from .serializers import (
    CommentSerializer,
    TodoSerializer,
)


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(todo_id=self.kwargs['todo_id'])
