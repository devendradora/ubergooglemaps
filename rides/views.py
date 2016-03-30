from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import requests
import json
from django.core.mail import EmailMessage
from .forms import *


# Create your views here.

def index(request):
	remainder_form= ReminderForm()	
	return render(request,"index.html",{"remainder_form":remainder_form})


def index2(request):
	url = "https://api.uber.com/v1/estimates/time"
	parameters = {
	#"server_token": "BPehDhjfmMaomcn2ZbnWuyaqRzrZoTS1ezAMlZs1",
	"server_token" : "4AjEu0MGo1amID9ttROHitLNh1lS37fz3x1dhZkB",
        "start_latitude": 12.927880,
        "start_longitude": 77.627600,}
	
	response = requests.get(url, params=parameters)
	data=response.json()
	data=json.dumps(data)	
	#return HttpResponse(data)
	return render(request,"index.html",{"data":data})

def sendemail(request):
	email = EmailMessage(
    "Uber Booking Remainder",
    "Hi Devendra !!! Its time to book the uber ",
    "sender smtp gmail" +"<dev.tech24@gmail.com>",
    ["devendra.dora24@gmail.com"],
    headers = {"Reply-To": "dev@gmail.com" }
	)
	email.send()

def setReminder(request):
        data=[]
	if request.method == "POST":
            data = request.POST.get("uber_info")
            data =  json.loads(data)
            obj = Reminder(src_lat=data["src_lat"],dest_lat=data["dest_lat"],src_lng=data["src_lng"],dest_lng=data["dest_lng"],reminder_time=data["reminder_time"],email=data["email"])
            obj.save() 

         
            url = "https://api.uber.com/v1/reminders"
            headers = {"Content-type": "application/json", "Accept": "text/plain"}
            #"server_token": "4AjEu0MGo1amID9ttROHitLNh1lS37fz3x1dhZkB", 
            parameters = {
            "server_token": "BPehDhjfmMaomcn2ZbnWuyaqRzrZoTS1ezAMlZs1",                              
            "reminder_time": data["reminder_time"],
            "phone_number" : "+919666261963",
            "event": {
            "name":"Remind me of meeting",
            "time":data["dest_time"],
            "latitude": data["dest_lat"],
            "longitude": data["dest_lng"],
            "product_id" : "db6779d6-d8da-479f-8ac7-8068f4dade6f"}
            }

            #parameters=json.dumps(parameters,sort_keys=False)
            print "devjson",parameters
           
            response = requests.post(url, params=parameters, headers=headers)
            resdata=response.json()
            resdata=json.dumps(resdata)
            	
            return HttpResponse(resdata)
             
            #return render(request,"index.html",{"data":data})

