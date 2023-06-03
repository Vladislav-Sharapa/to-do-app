from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.

@api_view(['GET'])
def overview(request):
    """Get available urls"""

    urls = {
        '1': 'first',
    }
    return Response(urls)

@api_view(['GET'])
def task_list(request):
    """Output all tasks"""

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)


class CreateTask(generics.GenericAPIView):
    serializer_class = TaskSerializer

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)