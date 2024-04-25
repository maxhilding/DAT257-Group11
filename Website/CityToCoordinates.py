import csv

# takes in a city name as a string and returns the latitude and longitude in a tuple
def city2Coordinates(city: str, citiesFile):
    with open(citiesFile, 'r') as f:
        rows = csv.DictReader(f, delimiter=',')
        for row in rows:
            if row["city_ascii"].lower() == city.lower():
                return (float(row["lat"]), float(row["lng"]))

