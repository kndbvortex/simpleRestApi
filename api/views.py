from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task


@api_view(["GET", "POST"])
def apiSimpleView(request):
    data = {
        'Rest_framework': "Django",
        "Student" : "Durande",
    }
    return Response(data)

@api_view(["GET", "POST"])
def task_list(request):
    tasks = Task.objects.all()
    serialiser = TaskSerializer(tasks,many=True)
    return Response(serialiser.data)


@api_view(["GET", "POST"])
def task_detail(request, id):
    try:
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task)
    except:
        class A:
            data = {
            "id": None,
            "title": None,
            "completed": None
        }
        serializer = A()
    return Response(serializer.data)

@api_view(["POST"])
def create_task(request):
    serialiser = TaskSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(["POST"])
def update_task(request, id):
    task = Task.objects.get(id=id)
    serialiser = TaskSerializer(instance=task ,data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)