from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

from todos.models import Todos
from todos.api.serializers import TodoSerializer

@api_view(['GET'])
def detail(request, id):
    try:
        todo = Todos.objects.get(pk=id)
        serialized = TodoSerializer(todo)
        print(serialized.data)
        return Response(serialized.data)
    except (Todos.DoesNotExist):
        print("serializedTodos.data")
        return Response(data={ 'message': "Todo not found" }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list(request):
    todos = Todos.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    # currently hard coded becuase no auth token
    user = User.objects.get(pk=1)

    todo = Todos(user=user)

    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, id):
    print(id)
    try:
        todo = Todos.objects.get(pk=id)
    except (Todos.DoesNotExist):
        print("not found")
        return Response(data={ 'message': "Invalid todo id" }, status=status.HTTP_400_BAD_REQUEST)

    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={ 'message': 'Todo updated' })
    print("invalid")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id):
    try:
        todo = Todos.objects.get(pk=id)
    except (Todos.DoesNotExist):
        return Response(data={ 'message': 'Invalid todo' }, status=status.HTTP_400_BAD_REQUEST)
    
    is_deleted = todo.delete()
    if is_deleted:
        return Response(data={ 'message': 'Todo deleted successfully' })
    return Response(data={ 'message': 'Todo deletion failed. Please try again' })