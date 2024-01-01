from rest_framework import serializers
from .models import Task

class taskSerializer(serializers.Serializer):
    class Meta:
        models=Task
        fields='__all__'