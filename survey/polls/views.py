from django.http import HttpResponse, HttpResponseRedirect
from polls.models import *
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Create your views here.


def index(request):
    context = {
        'polls' : Poll.objects.all()    
    }
    return render(request, 'index.html', context)

def detail(request, poll_id):
    context = {
        'poll' : get_object_or_404(Poll, id=poll_id)    
    }
    return render(request, 'detail.html', context)

def vote(request, poll_id, choice_id):
    poll = get_object_or_404(Poll, id=poll_id)
    try:
        selected_choice = poll.choice_set.get(id=choice_id)
    except (Choice.DoesNotExist):
        return render(request, 'detail.html', {
                'poll' : poll,
                'error_message' : 'You didn`t select a choice.'
    })
    else:
        selected_choice.votes = selected_choice.votes + 1
        selected_choice.save()
        return HttpResponseRedirect('/polls/%s/result' % (poll_id,))

def result(request, poll_id):
    context = {
        'poll': get_object_or_404(Poll, id=poll_id)    
    }
    return render(request, 'results.html', context)

def add_poll(request):
    return render(request, 'add_poll.html')

def submit_poll(request):
    try:
        question = request.POST['question'].strip()
        choice1 = request.POST['choice1'].strip()
        choice2 = request.POST['choice2'].strip()
    except (KeyError):
        context = {
            'error_message':'Invalid request'   
        }
        return render(request, 'add_poll.html',context)
    else:
        if not question:
            context = {
                'error_message' : 'Question cannot be empty'
            }
            return render(request, 'add_poll.html',context)
        else:
            poll = Poll(question = question, pub_date = timezone.now())
            poll.save()
            if choice1:
                poll.choice_set.create(choice_text=choice1)
            if choice2:
                poll.choice_set.create(choice_text=choice2)
            return HttpResponseRedirect('/polls')