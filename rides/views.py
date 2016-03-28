from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import requests
import json

# Create your views here.

def index(request):
	url = 'https://api.uber.com/v1/estimates/time'
	parameters = {
	'server_token': 'BPehDhjfmMaomcn2ZbnWuyaqRzrZoTS1ezAMlZs1',
    'start_latitude': 12.927880,
    'start_longitude': 77.627600,}
	
	response = requests.get(url, params=parameters)
	data=response.json()
	data=json.dumps(data)
	print "dev",data
	#return HttpResponse(data)
	return render(request,"index.html",{'data':data})
