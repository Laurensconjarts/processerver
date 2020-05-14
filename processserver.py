import pymssql
import requests
devices = []
macdata = []
macadres = []
locatie = []
sterkte = []

def db_con():
    global conn
    conn   = pymssql.connect(server='145.220.75.101', user='sa', password='P@ssw0rd', database='find3')
    global cursor
    cursor = conn.cursor()
def api_con():
    global response
    response = requests.get("http://145.220.75.101:8005")
    print(response.status_code)


db_con()
api_con()

mac = 0
device = 0
signaal = 0
node = 0

def api_con2():
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
        print(node)
        del locatie[0]
        signaal = sterkte[0]
        print(signaal)
        del sterkte[0]
        apparaat_insert(mac, device)
        Signaal_insert(signaal, node)
        count1 += 1





def apparaat_insert(mac, device):
    global idn
    try:
        querie = "select max(ApparaatID) from Apparaat"
        cursor.execute(querie)
        result = cursor.fetchone()
        ido = result[0]
        idn = ido + 1
        querie1 = f"INSERT INTO Apparaat(ApparaatID, MACADRES, Typeapparaat) VALUES ({idn}, '{mac}', '{device}');"
        cursor.execute(querie1)
        conn.commit()
    except pymssql.Error as e:
        print(e)
        querie2 = f"select ApparaatID from Apparaat where MACADRES ='{mac}'"
        cursor.execute(querie2)
        result = cursor.fetchone()
        idn = result[0]
        print(idn)
def Signaal_insert(signaal, node):
        querie4 = f"INSERT INTO Signaal(ApparaatID, Signaalsterkte,Node) VALUES ({idn}, {signaal}, '{node}');"
        cursor.execute(querie4)



api_con2()
