from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from list.serializers import ListSerializers
from list.models import List
from rest_framework.generics import ListCreateAPIView
from task.serializers import TaskSerializers
from task.models import Task
from django.core.exceptions import PermissionDenied

# Create your views here.
class ListViewSet(ModelViewSet):
    serializer_class = ListSerializers
    queryset = List.objects.all()


# Get tasks for a list
class ListTaskAPIView(ListCreateAPIView):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()

    def get_queryset(self):
        list_id = self.kwargs['list_id']
        task_list = List.objects.filter(id=list_id, owner=self.request.user).first()
        if not list:
            raise PermissionDenied("You do not have permission to access this list task's")
        return Task.objects.filter(list=task_list)

    def perform_create(self, serializer):
        list_id = self.kwargs['list_id']
        task_list = List.objects.filter(id=list_id, owner=self.request.user).first()
        if not list:
            raise PermissionDenied("You do not have permission to add tasks to this lists")
        serializer.save(list=task_list)
