import psycopg2


class DatabaseConnector:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="elefantSQL")
        self.conn.autocommit = True

    def getData(self):
      with self.conn.cursor() as cur:
        # Here's a start of the code for this part
        sql = """SELECT jsonb_build_object('idnr', l.idnr,
                                           'location', jsonb_build_object('lon', l.lon, 
                                                                          'lat', l.lat,
                                                                          'address', l.address,
                                                                          'working', l.working)
                                                                          ) AS location_json
                FROM Locations AS l;"""
        cur.execute(sql)
        res = cur.fetchall()
        if res:
            outdict = {'idnumbers':[], 'lon':[], 'lat':[], 'address':[], 'working': []}
            #print(res)
            for tuplethingy in res:
               outdict['idnumbers'].append(tuplethingy[0]['idnr'])
               outdict['lon'].append(tuplethingy[0]['location']['lon'])
               outdict['lat'].append(tuplethingy[0]['location']['lat'])
               outdict['address'].append(tuplethingy[0]['location']['address'])
               outdict['working'].append(tuplethingy[0]['location']['working'])
               #idnumberlist.append(object['idnr'])
            return outdict
        else:
            return """{"result":"Not found :("}"""


def getError(e):
    message = repr(e)
    message = message.replace("\\n"," ")
    message = message.replace("\"","\\\"")
    return message