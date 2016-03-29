from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import requests
import json
from django.core.mail import EmailMessage


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
	#return HttpResponse(data)
	return render(request,"index.html",{'data':data})

def sendemail(request):
	email = EmailMessage(
    'Uber Booking Remainder',
    'Hi Devendra !!! Its time to book the uber ',
    'sender smtp gmail' +'<dev.tech24@gmail.com>',
    ['devendra.dora24@gmail.com'],
    headers = {'Reply-To': 'dev@gmail.com' }
	)
	email.send()
