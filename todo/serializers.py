from rest_framework import serializers
from .models.todo import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'completed']
