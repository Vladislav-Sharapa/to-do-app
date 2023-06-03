from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def overview(request):
    urls = {
        '1': 'first',
    }
    return Response(urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)
