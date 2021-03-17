from rest_framework import serializers
from .models import Todo



class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('name', 'task', 'due','email')
