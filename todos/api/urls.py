from django.urls import path

from . import views

app_name= 'todos_api'

urlpatterns = [
    path("", views.list, name="list"),
    path("<int:id>", views.detail, name="tododetail"),
    path("create", views.create, name="create"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete")
]