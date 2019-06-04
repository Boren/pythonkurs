from typing import List

from matplotlib import pyplot as plt
from shapely.geometry import Point


def plot_punkt(punkt: Point):
    """
    Plot et enkelt punkt på en graf
    """
    fig = plt.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.scatter(punkt[0], punkt[1])
    ax.set_title('Punkt')


def plot_punkter(punkter: List[Point]):
    """
    Plot flere punkter på samme plot
    """
    x = [punkt[0] for punkt in punkter]
    y = [punkt[1] for punkt in punkter]
    fig = plt.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    ax.set_title('Punkter')

def plot_linje(linje):
    """
    Plot en linje
    """
    x = [punkt[0] for punkt in linje]
    y = [punkt[1] for punkt in linje]
    fig = plt.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.plot(x, y, '-')
    ax.set_title('Linje')

def plot_polygon(linje):
    """
    Plot en polygon
    """
    polygon = plt.Polygon(linje, alpha=0.5)
    fig = plt.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.add_patch(polygon)
    plt.autoscale(enable=True, axis='both', tight=None)
    ax.set_title('Polygon')

import requests

brukernavn = ""
passord = ""
# Henter token fra ArcGIS Server
tokenparametre = {'username': brukernavn, 'password': passord, 'f': 'pjson', 'client': 'requestip'}
tokenforespørsel = requests.get("https://services.geodataonline.no/arcgis/tokens/generateToken",
                                params=tokenparametre)

token = tokenforespørsel.json()['token']

def geokoding(søketekst: str, koordinatsystem = 4326):
    """
    Geokod ved hjelp av fritekst søk
    Standard koordinatsystem er UTM-33
    For bruk av WGS 84 bruk ID: 4326
    """

    endepunkt = "https://services.geodataonline.no/arcgis/rest/services/Geosok/GeosokLokasjon2/GeocodeServer/findAddressCandidates"
    parametre = {'SingleLine': søketekst, 'outSR': koordinatsystem, 'f': 'pjson', 'token': token}

    forespørsel = requests.get(endepunkt,
                               params=parametre)

    return (forespørsel.json()['candidates'][0]['location']['y'],
            forespørsel.json()['candidates'][0]['location']['x'])   
