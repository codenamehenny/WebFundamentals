import requests

#Task 2: Fetch Data from a Space API Write a Python script that makes a GET request to a space API (e.g., 
# [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)) to fetch data about planets.

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass = planet['mass']['massValue'] if planet.get('mass') else 'Unknown'
            orbit_period = planet.get('sideralOrbit', 'Unknown')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()


# Task 3: Data Presentation and Analysis - Perform a simple analysis, 
# such as finding the planet with the longest orbit period or the heaviest planet. 

def fetch_planet_mass():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_data = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet.get('mass') else None
            orbit_period = planet['sideralOrbit']
            planet_data.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })
    return planet_data

def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0
    # iterates over the planets to find the largest mass
    for planet in planets:
        if planet['mass'] and planet['mass'] > max_mass:
            max_mass = planet['mass']
            heaviest_planet = planet
    return heaviest_planet

planets = fetch_planet_mass()
heaviest_planet = find_heaviest_planet(planets)
if heaviest_planet:
    print(f"\nThe heaviest planet is {heaviest_planet['name']} with a mass of {heaviest_planet['mass']} kg.")