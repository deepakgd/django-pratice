from django.urls import path
from . import views

app_name = "helloworld"

urlpatterns = [
    path('', views.index, name="index"),
    path('name/', views.dynamiccontent, name="dynamicname"),
    path('add/', views.add, name="addtwonumber"),
    path('result/', views.result, name="result")
]