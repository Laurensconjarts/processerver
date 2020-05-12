
import requests
def api_con():
    global response
    response = requests.get("http://145.220.75.101:8005/api/v1/locations/sutoka")
    data = response.json()
    for each in data['locations']:
        print(each['d'])

api_con()