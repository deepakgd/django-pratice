from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path("", views.list, name="list"),
    path("create/", views.create, name="createtodo"),
    path("<int:id>/", views.edit_or_update, name="edittodo"),
    path("delete/<int:id>/", views.delete, name="deletetodo"),
    path("createtodo/", views.TodoCreateView.as_view(), name="createtodoview"),
    path("list/", views.TodoListView.as_view(), name="listtodo"),
    path("show/<int:pk>", views.TodoDetailedView.as_view(), name="listtodo"),
    path("update/<int:pk>", views.TodoUpdateView.as_view(), name="updatetodo"),
    path("deleteview/<int:pk>", views.TodoDeleteView.as_view(), name="deleteviewtodo")
]