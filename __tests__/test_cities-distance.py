import pytest
from projects.cities_distance import *


@pytest.mark.parametrize('url', [
    ("https://devw.github.io/supn/data/laposte_hexasmal.small.csv"),
])
def test_get_raw_data(url):
    raw_data = get_raw_data(url)
    print(f"\n**raw_data output**: {raw_data}")
    assert type(raw_data) == type("")
    assert raw_data[:12] == "Code_commune"
    assert raw_data[-10:] == "54954155\r\n"


@pytest.mark.parametrize('url', [
    ("https://devw.github.io/supn/data/laposte_hexasmal.small.csv"),
])
def test_get_city_dict(url):
    city_dict = get_city_dict(url)
    print(f"\n** city_dict output **: {city_dict}")
    assert type(city_dict) == dict
    assert len(city_dict) == 28
    assert city_dict['CLAVEYSON'] == '45.173018025,4.933788902'


@pytest.mark.parametrize('lonLat_1, lonLat_2, result', [
    ("44.474916997,5.23866199", "45.103660246,4.924426332", 77.91),
])
def test_get_distance(lonLat_1, lonLat_2, result):
    distance = get_distance(lonLat_1, lonLat_2)
    print(
        f"\n** Actual result {round(distance, 2)} km, Expected result {round(distance, 2)}km ±1 km")
    assert distance > result - 1 and distance < result + 1


@pytest.mark.parametrize('city', [
    ("ALLAN"),
])
def test_get_distances_from(city):
    distances_from = get_distances_from(city)
    print(f"\n**Distances_from {city}:\n {distances_from} ")
    assert type(distances_from) == dict
    assert distances_from['ARNAYON'] < distances_from['AULAN']


@pytest.mark.parametrize('city', [
    ("ALLAN"),
])
def test_get_sorted_distance(city):
    distances_from = get_distances_from(city)
    sorted_distance = get_sorted_distance(distances_from)
    city_list = list(sorted_distance)
    assert type(sorted_distance) == dict
    assert sorted_distance[city_list[1]] < sorted_distance[city_list[2]]
    assert sorted_distance[city_list[-2]] < sorted_distance[city_list[-1]]


@pytest.mark.parametrize('city, expected', [
    ("ALLAN", "CHATEAUNEUF DU RHONE"),
])
def test_get_nearest_city(city, expected):
    distances_from = get_distances_from(city)
    sorted_distance = get_sorted_distance(distances_from)
    nearest_city = get_nearest_city(sorted_distance)
    assert type(sorted_distance) == dict
    assert nearest_city == expected
