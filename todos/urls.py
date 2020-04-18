from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path("", views.list, name="list"),
    path("create/", views.create, name="createtodo"),
    path("<int:id>/", views.edit_or_update, name="edittodo"),
    path("delete/<int:id>/", views.delete, name="deletetodo")
]