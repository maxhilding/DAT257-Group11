import unittest
from website import *
from Database.DatabaseConnector import *


class Tests(unittest.TestCase):

    #tests a few coordinates
    def test_coordinate_search(self):
        coordinate_list = ['12.57, 57.34', '11.21, 78.90', '20.67, 49.76']
        for coordinate in coordinate_list:
            self.assertEqual((search_helper(coordinate)), (float(coordinate[0:5]), float(coordinate[7:])))

    def test_city_search(self):
        geolocator = Nominatim(user_agent="my_app_name")
        geocode = partial(geolocator.geocode, language="es")
        city_coordinates = {'Gothenburg': None, 'Stockholm': None}
        for city in city_coordinates:
            city_coordinates[city] = (geocode(city).latitude, geocode(city).longitude)
            lat, lon = search_helper(city)
            self.assertEqual((lat,lon), city_coordinates[city])
            

    def test_search_error(self):
        geolocator = Nominatim(user_agent="my_app_name")
        geocode = partial(geolocator.geocode, language="es")
        city_coordinates = {'skibidi toilet': None}
        for city in city_coordinates:
            with self.assertRaises(AttributeError):
                search_helper(city)


    def test_data_helper(self):
        res = [({'idnr': 123, 'location': {'lon': 1.1, 'lat': 2.2, 'address': '', 'working': True}}, ''), ({'idnr': 4, 'location': {'lon': 3.3, 'lat': 4.4, 'address': 'A', 'working': False}}, '')]
        correct_outdict = {'idnumbers':[123, 4], 'lon':[1.1, 3.3], 'lat':[2.2, 4.4], 'address':['', 'A'], 'working': [True, False]}
        self.assertEqual(data_helper(res), correct_outdict)




if __name__ == '__main__':
    unittest.main()