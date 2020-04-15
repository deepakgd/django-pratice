from django.urls import path
from . import views

app_name = "helloworld"

urlpatterns = [
    path('', views.index, name="index"),
    path('name/', views.dynamiccontent, name="dynamicname"),
    path('add/', views.add, name="addtwonumber"),
    path('result/', views.result, name="result"),
    path('multiply/', views.multiply, name="multiply"),
    path('multiplyresult', views.multiplyresult, name="multiplyresult"),
    path('subtraction', views.subtraction, name="subtraction"),
    path('subresult', views.subresult, name='subresult'),
    path('viewimage', views.viewImageAsset, name="viewimageasset"),
    path('students', views.listStudents, name="list students")
]