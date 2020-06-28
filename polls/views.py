from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404

from .models import Question
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    #template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #return HttpResponse("you are looking at question %s. " % question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    response = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on question %s. " % question_id)