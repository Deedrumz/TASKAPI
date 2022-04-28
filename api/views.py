from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
            'Lists': '/task-list/',
            'Detail View': '/task-list/<str:pk>/',
            'Create': '/task-create/',
            'Update': 'task-update',
            'Delete': '/task-delete/<str:pk>',

    }
    # return Response('API BASE', safe=False)
    return Response(api_urls)


#this function is to List out all the thing inputed backend
@api_view(['GET'])
def taskList(request):
            tasks = Task.objects.all().order_by('-id')
            serializer = TaskSerializer(tasks, many=True)

            return Response(serializer.data)


#this is to get a particular detail in the task list
@api_view(['GET'])
def taskDetail(request, pk):

    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)


#this is to create and post to the backend
@api_view(['POST'])
def taskCreate(request):

    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#this is to Update what's in the backend and post again to the backend
@api_view(['POST'])
def taskUpdate(request, pk):

    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#this is to Delete what has been posted to the backend
@api_view(['DELETE'])
def taskDelete(request, pk):

    tasks = Task.objects.get(id=pk)
    tasks.delete()
    

    return Response(' Task successfully deleted')