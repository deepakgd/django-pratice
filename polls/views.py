from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # -pub_date mean desc order, pub_date mean asc order
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    # loop latest_question and return question_text in comma separated value
    output = ', '.join([q.question_text for q in latest_questions])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)