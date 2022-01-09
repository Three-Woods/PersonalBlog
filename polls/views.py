from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':"You didnot select a choice. ",})
    else:
        selected_choice.vote+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

    
"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  template = loader.get_template()
  # output=','.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
    
"""

# Create your views here.
