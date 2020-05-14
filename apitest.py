
import requests
testlist = []
def api_con():
    global response
    response = requests.get("http://145.220.75.101:8005/api/v1/locations/sutoka")
    data = response.json()
    for each in data['locations']:
        testlist.append(each['sensors']['d'])
        testlist.append(each['sensors']['s']['wifi'])
    print(testlist)
api_con()