from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import TodoForm
from .models import Todos

# Create your views here.
def list(request):
    todos = Todos.objects.all()
    # to view fields in todos[0[ object]]
    # print(dir(todos[0]))
    return render(request, 'todos.html', { 'todos': todos })

def create(request):
    if(request.method == 'GET'):
        form = TodoForm()
        return render(request, 'todos_create.html', { 'form': form })
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos:list")
        else:
            # form context contains error message 
            return render(request, 'todos_create.html', { 'form': form })

def edit_or_update(request, id):
    todo = get_object_or_404(Todos, pk=id)
    if request.method == 'GET':
        form = TodoForm(None, instance=todo)
        return render(request, 'todo_edit.html', { 'form': form })
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return (redirect("todos:list"))
        else:
            return render(request, 'todo_edit.html', { 'form': form })

def delete(request, id):
    todo = get_object_or_404(Todos, pk=id)
    todo.delete()
    return redirect("todos:list")
        