from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from task.serializers import TaskSerializers
from task.models import Task

# Create your views here.
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
