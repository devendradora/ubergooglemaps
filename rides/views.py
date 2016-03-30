from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import requests
import json
from django.core.mail import EmailMessage
from .forms import *


# Create your views here.

def index(request):
	remainder_form= RemainderForm()	
	return render(request,"index.html",{'remainder_form':remainder_form})


def index2(request):
	url = 'https://api.uber.com/v1/estimates/time'
	parameters = {
	#'server_token': 'BPehDhjfmMaomcn2ZbnWuyaqRzrZoTS1ezAMlZs1',
	'server_token' : '4AjEu0MGo1amID9ttROHitLNh1lS37fz3x1dhZkB',
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

def setRemainder(request):
	if request.method == "POST":
            data = request.POST.get('uber_info')
            data =  json.loads(data)
            url = 'https://api.uber.com/v1/reminders'
            parameters = {
            #'server_token': 'BPehDhjfmMaomcn2ZbnWuyaqRzrZoTS1ezAMlZs1',
            'server_token' : '4AjEu0MGo1amID9ttROHitLNh1lS37fz3x1dhZkB',
            'reminder_time': data['remainder_time'],
            'phone_number' : '+919666261963',
            'event':'Remind me of meeting',
            'event.time':data['remainder_time'],
            'event.latitude': data['dest_lat'],
            'event.longitude': data['dest_lng'],}

            response = requests.get(url, params=parameters)
            data=response.json()
            data=json.dumps(data)	
            #return HttpResponse(data)
            obj = Remainder(src_lat=data['src_lat'],dest_lat=data['dest_lat'],src_long=data['src_lng'],dest_long=data['dest_lng'],remainder_time=data['remainder_time'],email=data['email'])
            obj.save()  
            return render(request,"index.html",{'data':data})

