from rest_framework import serializers

from .models import (
    Comment,
    Todo,
)


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'headline',
            'content',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'title',
            'body',
            'created_at',
            'todo_id',
        )
        read_only_fields = (
            'id',
            'created_at',
            'todo_id',
        )
