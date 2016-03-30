

https://developer.uber.com/docs/v1-reminders-post


I used above to create a remainder , but only sms is allowed.

when I try to post the parameters to this :  "https://api.uber.com/v1/reminders"

            url = "https://api.uber.com/v1/reminders"
            headers = {"Content-type": "application/json", "Accept": "text/plain"}           
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

            parameters=json.dumps(parameters,sort_keys=False)     
           
            response = requests.post(url, params=parameters, headers=headers)
            resdata=response.json()

            It is giving the error , authorization failed but when I remove line parameters=json.dumps(parameters,sort_keys=False) , authorization is success , but json parsing fails in request headers

            Moreover , as I used the api many times , it is giving  Max retries exceeded with url: /v1/reminders




If duration from A to B takes 1 hr , then the server checks for the availability of uber as per below:

It checks  before 1+1  hrs , 1 + 1/2 hrs , 1+1/4 hrs ,......., and subsequiently updates the time to be remainded to reach the destination.