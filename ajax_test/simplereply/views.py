from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
	return render(request, "index.html")

def request_reply(request):
	response = {
		"data" : ["data1", "data2", "data3", "data4"]
	}
	return HttpResponse(json.dumps(response), content_type="application/json")
