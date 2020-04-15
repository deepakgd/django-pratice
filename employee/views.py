from django.shortcuts import render

from .models import Employee

# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', { 'employees': employees })