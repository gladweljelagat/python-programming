#!/usr/bin/python3

from task11 import delete_key
cities = {"Nairobi": 1, "Kisumu": 2}
delete_key(cities, "Nairobi")
delete_key(cities, "Eldoret")
print(cities)
