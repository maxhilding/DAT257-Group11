import requests
import json
import psycopg2
from geopy.geocoders import Nominatim

def main():

    API = requests.get("https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/drinking-fountains/records?limit=20")
    data_text = API.text
    data = json.loads(data_text)
    data = data["results"]

    geolocator = Nominatim(user_agent="my_app_name")
    try:
        conn = connectDatabase()
        print("Connected successfully")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error connecting to the database:", error)

    with conn.cursor() as cur:

        for fountain in data:
            coord = fountain["geom"]["geometry"]["coordinates"]
            lon = coord[0]
            lat = coord[1]
            location = geolocator.reverse(f"{lat}, {lon}")
            sql = """INSERT INTO Locations(lon, lat, address) VALUES (%s, %s, %s);"""
            cur.execute(sql, (lon, lat, location.address))
    
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



