import requests
import json
import psycopg2

def main():

    API = requests.get("https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/drinking-fountains/records?limit=20")
    data_text = API.text
    data = json.loads(data_text)
    data = data["results"]
    conn = connectDatabase()

    with conn.cursor() as cur:

        for fountain in data:
            coord = fountain["geom"]["geometry"]["coordinates"]
            lon = coord[0]
            lat = coord[1]
            sql = """INSERT INTO Locations(lon, lat) VALUES (%s, %s);"""
            cur.execute(sql, (lon, lat))
    
def connectDatabase():
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres")
    conn.autocommit = True
    return conn
        

if __name__ == "__main__":
    main()



