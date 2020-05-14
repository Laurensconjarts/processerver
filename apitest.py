
import requests
devices = []
macdata = []
macadres = []
locatie = []
sterkte = []
def api_con():
    global response
    response = requests.get("http://145.220.75.101:8005/api/v1/locations/sutoka")
    data = response.json()
    for each in data['locations']:
        devices.append(each['sensors']['d'])


    count = 0
    c = len(devices)
    while count < c:

        data2 = data['locations'][count]['sensors']['s']['wifi']
        for each in data2:
            macdata.append(each)
        macadres.append(macdata[0])
        macdata.clear()
        count += 1
    count3 = 0
    while count3 < c:
        locatie.append(data['locations'][count3]['prediction']['location'])
        count3 += 1
    count4 = 0
    while count4 < c:
        sterkte.append(data['locations'][count4]['prediction']['probability'])
        count4 += 1
    count1 = 0
    while count1 < c:
        mac = macadres[0]

        del macadres[0]
        device = devices[0]
        del devices[0]
        node = locatie[0]
        del locatie[0]
        signaal = sterkte[0]
        del sterkte[0]
        apparaat_insert(mac, device)
        def Signaal_insert(signaal, node)
        count1 += 1


api_con()