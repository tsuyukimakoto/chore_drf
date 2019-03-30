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

    def to_internal_value(self, data):
        values = super().to_internal_value(data)
        values['todo_id'] = self.context['todo_id']
        return values

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
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Comment.objects.all(),
                fields=('todo_id', 'title'),
                message="title can't same on each Todo.",
            ),
        ]
