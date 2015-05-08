from django.shortcuts import render
from django.http import HttpResponse
from polls.data import get, get_all
# Create your views here.


def index(request):
    context = {
        'polls' : get_all()    
    }
    return render(request, 'index.html', context)

def detail(request, poll_id):
    context = {
        'poll' : get(poll_id)    
    }
    return render(request, 'detail.html', context)

def vote(request, poll_id, choice_id):
    return HttpResponse("vote : poll = %s, choice = %s" % (poll_id, choice_id))

def result(request, poll_id):
    return HttpResponse("result : poll = %s" % (poll_id,))