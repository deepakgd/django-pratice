from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    # normal function 
    path("", views.list, name="list"),
    path("create/", views.create, name="createtodo"),
    path("<int:id>/", views.edit_or_update, name="edittodo"),
    path("delete/<int:id>/", views.delete, name="deletetodo"),

    # class based view
    path("createtodo/", views.TodoCreateView.as_view(), name="createtodoview"),
    path("list/", views.TodoListView.as_view(), name="listtodo"),
    path("show/<int:pk>", views.TodoDetailedView.as_view(), name="listtodo"),
    path("update/<int:pk>", views.TodoUpdateView.as_view(), name="updatetodo"),
    path("deleteview/<int:pk>", views.TodoDeleteView.as_view(), name="deleteviewtodo"),

    # function to class view
    path("welcome/", views.WelcomeTodoView.as_view(), name="welcometodo"),
    path("welcome2/", views.WelcomeTodoView.as_view(template_name="todo_welcome2.html"), name="welcome2todo"),
    path("f2c/list/", views.F2CListTodoView.as_view(), name="func_to_class_list"),
    path("f2c/create/", views.F2CCreateTodoView.as_view(), name="func_to_class_create"),
    path("f2c/update/<int:id>", views.F2CUpdateTodoView.as_view(), name="func_to_class_edit_update")
]
