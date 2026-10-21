#!/usr/bin/env python3
"""Fetch starships that can hold a given number of passengers from SWAPI."""
import requests


def availableShips(passengerCount):
    """Return the list of ships that can hold passengerCount passengers."""
    ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"
    while url:
        data = requests.get(url).json()
        for ship in data["results"]:
            passengers = ship["passengers"].replace(",", "")
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship["name"])
        url = data["next"]
    return ships
