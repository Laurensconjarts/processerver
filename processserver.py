import pymssql
import requests


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

mac = input("mac")
appa = input("appa")

def apparaat_insert():
    try:
        querie = "select max(ApparaatID) from Apparaat"
        cursor.execute(querie)
        result = cursor.fetchone()
        ido = result[0]
        idn = ido + 1
        querie1 = f"INSERT INTO Apparaat(ApparaatID, MACADRES, Typeapparaat) VALUES ({idn}, '{mac}', '{appa}');"
        cursor.execute(querie1)
        conn.commit()
    except pymssql.Error as e:
        print(e)
        querie2 = f"select ApparaatID from Apparaat where MACADRES ='{mac}'"
        cursor.execute(querie2)
        result = cursor.fetchone()
        mac1 = result[0]
        print(mac1)
apparaat_insert()
