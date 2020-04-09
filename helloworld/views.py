from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

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