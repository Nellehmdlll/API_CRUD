from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import taskSerializer

class TaskCreateView(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=taskSerializer
    
class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer
