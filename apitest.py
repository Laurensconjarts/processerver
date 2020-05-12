
import requests
def api_con():
    global response
    response = requests.get("1http://145.220.75.101:8005/api/v1/locations/sutoka")


    print(response.text)
api_con()