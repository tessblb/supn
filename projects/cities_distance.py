from math import radians, cos, sin, asin, sqrt
from urllib.request import urlopen
import ssl

URL = "https://devw.github.io/supn/data/laposte_hexasmal.small.csv"


def get_raw_data(url=URL):
    response = urlopen(url, context=ssl._create_unverified_context())
    data = response.read().decode('utf-8')
    return data


def get_city_dict(url=URL):
    raw_data = get_raw_data(url)
    lines = [line.split(";") for line in raw_data.split("\r\n")][1:-1]
    return {line[1]: line[5] for line in lines}


def get_distance(lonLat_1, lonLat_2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1 = lonLat_1.split(",")
    lon2, lat2 = lonLat_2.split(",")
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(
        radians, [float(lon1), float(lat1), float(lon2), float(lat2)])

    # haversine formula
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    r = 6371
    return c * r


def get_distances_from(city):
    city_dict = get_city_dict()
    city_distances = dict()
    lonLat_1 = city_dict[city]
    for city in city_dict:
        lonLat_2 = city_dict[city]
        city_distances[city] = get_distance(lonLat_1, lonLat_2)
    return city_distances


def get_sorted_distance(distances):
    return {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}


def get_nearest_city(distances):
    distances_list = list(distances)
    return distances_list[1]


def get_furthest_city(distances):
    distances_list = list(distances)
    return distances_list[-1]


def get_median_city(distances):
    distances_list = list(distances)
    return distances_list[len(distances_list) // 2]


distances = get_distances_from('ALLAN')
print(distances)

distancesSorted = get_sorted_distance(distances)
print(distancesSorted)

nearest_city = get_nearest_city(distancesSorted)
print(nearest_city)

furthest_city = get_furthest_city(distancesSorted)
print(furthest_city)

median_city = get_median_city(distancesSorted)
print(median_city)
