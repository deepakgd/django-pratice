from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import generic

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
        
# create view
class TodoCreateView(generic.CreateView):
    template_name = "todos_create.html"
    form_class = TodoForm
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/todos/list'

# list view todos
class TodoListView(generic.ListView):
    template_name = "todos.html"
    context_object_name = 'todos'

    def get_queryset(self):
        return Todos.objects.all()

# Todo edit view
class TodoDetailedView(generic.DetailView):
    model = Todos
    template_name = "todo_show.html"
    context_object_name = "todo"

# Todo update view
class TodoUpdateView(generic.UpdateView):
    template_name = "todo_edit.html"
    form_class = TodoForm
    model = Todos

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return f'/todos/show/{self.kwargs["pk"]}'

# Todo delete view
class TodoDeleteView(generic.DeleteView):
    template_name = "todo_delete.html"
    model = Todos
    context_object_name = 'todo'

    def get_success_url(self):
        return '/todos/list'

