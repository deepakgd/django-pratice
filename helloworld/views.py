from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    # return HttpResponse('Hello world')
    return render(request, 'helloworld.html')

def dynamiccontent(request):
    return render(request, 'helloname.html', { "name": 'Deepak' })

def add(request):
    return render(request, 'add.html')

def result(request):
    value1 = int(request.GET['value1'])
    value2 = int(request.GET["value2"])
    result = value1 + value2
    print(value1)
    return render(request, 'result.html', { 'result': result })

def multiply(request):
    return render(request, 'mul.html')

def multiplyresult(request):
    value1 = int(request.GET["value1"])
    value2 = int(request.GET["value2"])
    multiply = value1 * value2
    return render(request, 'result.html', { 'result': multiply })

def subtraction(request):
    return render(request, 'subtraction-post-method.html')

def subresult(request):
    # in post method also we getting value as string so make it as int
    value1 = int(request.POST['value1'])
    value2 = int(request.POST['value2'])
    result = value1 - value2 
    return render(request, 'result.html', { 'result': result })

def viewImageAsset(request):
    return render(request, 'viewimage.html')

def listStudents(request):
    s1 = Student()
    s1.name = "adf"
    s1.age = 21
    s1.gender = "Male"
    s1.image = "s1.png"
    s1.is_active = True

    s2 = Student()
    s2.name = "qqqqqqq"
    s2.age = 33
    s2.gender = "Female"
    s2.image = "s2.png"
    s2.is_active = False

    s3 = Student()
    s3.name = "wwwww"
    s3.age = 24
    s3.gender = "Male"
    s3.image = "s3.png"
    s3.is_active = True

    students = [s1, s2, s3]
    return render(request, 'students.html', { 'students': students })
