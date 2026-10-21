#!/usr/bin/env python3
"""Fetch the home planets of all sentient species from the SWAPI API."""
import requests


def sentientPlanets():
    """Return the list of home planet names of all sentient species."""
    planets = []
    url = "https://swapi-api.hbtn.io/api/species/"
    while url:
        data = requests.get(url).json()
        for species in data["results"]:
            if (species.get("classification") == "sentient"
                    or species.get("designation") == "sentient"):
                homeworld = species.get("homeworld")
                if homeworld:
                    planet = requests.get(homeworld).json()
                    planets.append(planet["name"])
        url = data["next"]
    return planets
