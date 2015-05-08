from django.shortcuts import render
from django.http import HttpResponse
from main.data import user_all
# Create your views here.

def index(request):
    context = {
        'userList' : user_all()
    }
    return render(request, 'index1.html',context)
        
