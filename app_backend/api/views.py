from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ToDoList
from .serializer import ToDoListSerializer


@api_view(["GET"])
def home(request):
    routes = [
        {
            "Endpoint": "/list/",
            "method": "GET",
            "body": None,
            "description": "returns an array of to do list"
        },
        {
            "Endpoint": "/task/",
            "method": "GET",
            "body": None,
            "description": "returns a single to do task"
        },
        {
            "Endpoint": "/add/",
            "method": "POST",
            "body": None,
            "description": "adds a single to do task"
        },
        {
            "Endpoint": "/delete/",
            "method": "GET",
            "body": None,
            "description": "deletes a single to do task"
        },
        {
            "Endpoint": "/update/",
            "method": "POST",
            "body": None,
            "description": "updates a single to do task"
        },
    ]
    # return JsonResponse(routes, safe=False)
    # return Response(data=routes)
    return render(request, "index.html")


@api_view(["GET"])
def get_to_do_list(request):
    lists = ToDoList.objects.all()
    serializer = ToDoListSerializer(lists, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_to_do_task(request, id):
    lists = ToDoList.objects.get(pk=id)
    serializer = ToDoListSerializer(lists, many=False)

    return Response(serializer.data)


@api_view(["POST"])
def add_to_do_task(request):
    data = request.data

    task = ToDoList.objects.create(
        body=data["body"]
    )

    serializer = ToDoListSerializer(task, many=False)

    return Response(serializer.data)


@api_view(["DELETE"])
def delete_to_do_task(request, id):
    task = ToDoList.objects.get(pk=id)
    task.delete()

    lists = ToDoList.objects.all()
    serializer = ToDoListSerializer(lists, many=True)

    return Response(serializer.data)


@api_view(["PUT"])
def update_to_do_task(request, id):
    task = ToDoList.objects.get(pk=id)

    serializer = ToDoListSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
