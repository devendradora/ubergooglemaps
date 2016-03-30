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
	url = 'https://api.uber.com/v1/products'
	parameters = {
	#'server_token': 'BPehDhjfmMaomcn2ZbnWuyaqRzrZoTS1ezAMlZs1',
	'server_token' : '4AjEu0MGo1amID9ttROHitLNh1lS37fz3x1dhZkB',
        'latitude': 12.927880,
        'longitude': 77.627600,}
	
	response = requests.get(url, params=parameters)
	data=response.json()
	data=json.dumps(data)	
	return HttpResponse(data)
	#return render(request,"index.html",{'data':data})

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
    data=[]
    if request.method == "POST":
            data = request.POST.get('uber_info')
            data =  json.loads(data)
            url = 'https://api.uber.com/v1/reminders'
            parameters = {
            #'server_token': 'BPehDhjfmMaomcn2ZbnWuyaqRzrZoTS1ezAMlZs1',
            'server_token' : '4AjEu0MGo1amID9ttROHitLNh1lS37fz3x1dhZkB',
            'reminder_id':' 1255',
            'product_id' : 'db6779d6-d8da-479f-8ac7-8068f4dade6f',
            'reminder_time': data['remainder_time'],
            'phone_number' : '+919666261963',
            'event':{
            'name' :'Remind me of meeting',
            'time':data['remainder_time'],
            'latitude': data['dest_lat'],
            'longitude': data['dest_lng'],},}

            response = requests.get(url, params=parameters)
            data=response.json()
            data=json.dumps(data)	
    return HttpResponse(data)
           


