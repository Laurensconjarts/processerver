
import requests
testlist = []
testlist2 = []
testlist3 = []
def api_con():
    global response
    response = requests.get("http://145.220.75.101:8005/api/v1/locations/sutoka")
    data = response.json()
    for each in data['locations']:
        testlist.append(each['sensors']['d'])
    print(testlist)
    count = 0
    while count < 5:

        data2 = data['locations'][count]['sensors']['s']['wifi']
        for each in data2:
            testlist2.append(each)
        data3 = testlist2[count]
        print(data3)
        count += 1
api_con()