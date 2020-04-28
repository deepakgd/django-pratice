from rest_framework import serializers

from todos.models import Todos

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ["title", "description", "status", "user_id"]