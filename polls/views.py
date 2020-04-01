from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from .models import Question, Choice

def index(request):
    
    # simply return text
    # return HttpResponse("Hello, world. You're at the polls index.")
    
    # return top five question as string
    # -pub_date mean desc order, pub_date mean asc order
    # latest_questions = Question.objects.order_by('-pub_date')[:5]
    # loop latest_question and return question_text in comma separated value
    # output = ', '.join([q.question_text for q in latest_questions])
    # return HttpResponse(output)


    # return template with top five question
    # get question in descendeing order or pub date
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_questions': latest_questions
    }

    # method - 1
    # load template
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    # method - 2
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    
    # get data from db and return or send 404 message
    # Method 1
    # try:
    #     # get question by primary key or you can do by id or question_text. here i am doing by pk
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     # throw 404 status code with text message
    #     raise Http404("Question does not exists")
    # return render(request, 'polls/detail.html', { 'question': question })

    # Method 2
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', { 'question': question })

# this function will return question which start with given text
def detailv2(request, text):
    questions = get_list_or_404(Question, question_text__startswith=text)
    return render(request, 'polls/detailv2.html', { 'questions': questions })


def results(request, question_id):
    # return HttpResponse("You're looking at the results of question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', { 'question': question })

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['choice']
        choice = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        # display the question voiting form with error message
        return render(request, 'polls/detail.html', { 
            'question': question, 
            'error_message': "You didn't select a choice."
        })
    else:
        # increment vote and save it
        choice.votes += 1
        choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))