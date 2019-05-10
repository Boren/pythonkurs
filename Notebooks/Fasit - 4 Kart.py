#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Notebooks'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Kart med OpenStreetMap
# ## Geokoding
# Geokoding er en kjent del av GIS-hverdagen. Fordelen med Python og koding er at du kan automatisere geokoding av store datasett.
# Vi har jukset litt og forhåndlags noen små funksjoner som tar seg av arbeidet. Denne bruker Geodata sin geokodingstjeneste, men det finnes flere åpne tjenester som også kan brukes.
#%%
import requests

brukernavn = "fredrikb"
passord = "bB6nR9z&14v$%$Xx8I5O"

# Henter token fra ArcGIS Server
tokenparametre = {'username': brukernavn, 'password': passord, 'f': 'pjson', 'client': 'requestip'}
tokenforespørsel = requests.get("https://services.geodataonline.no/arcgis/tokens/generateToken", params=tokenparametre)

token = tokenforespørsel.json()['token']
#%%
def geokoding(søketekst: str, koordinatsystem = 25833):
    """
    Geokod ved hjelp av fritekst søk
    Standard koordinatsystem er UTM-33
    For bruk av WGS 84 bruk ID: 4326
    """
    endepunkt = "https://services.geodataonline.no/arcgis/rest/services/Geosok/GeosokLokasjon2/GeocodeServer/findAddressCandidates"
    parametre = {'SingleLine': søketekst, 'outSR': koordinatsystem, 'f': 'pjson', 'token': token}
    forespørsel = requests.get(endepunkt, params=parametre)
    return forespørsel.json()['candidates'][0]['location']

def revers_geokoding(breddegrad, lengdegrad, koordinatsystem = 25833):
    endepunkt = "https://services.geodataonline.no/arcgis/rest/services/Geosok/GeosokLokasjon2/GeocodeServer/reverseGeocode"
    parametre = {'location': f"{breddegrad}, {lengdegrad}", 'outSR': koordinatsystem, 'f': 'pjson', 'token': token}
    forespørsel = requests.get(endepunkt, params=parametre)
    return forespørsel.json()['address']
#%% [markdown]
# Prøv å kjøre funksjonen `geokoding()` med en valgfri norsk addresse som parameter. For eksempel der du bor eller der du jobber. Lagre resultatet i en variabel.
#%% [markdown]
# Det er selvfølgelig mulig å gjøre motsatt. Prøv nå å bruke funksjonen `revers_geokoding()` med koordinatene du fikk som resultat i forrige rute.
#%% [markdown]
# Prøv nå å kjøre geokoding igjen, men denne gangen spesifiserer du `4326` som koordinatsystem slik at vi får koordinater i WGS84. Lagre disse i en ny variabel slik at du kan bruke den senere til å plotte i et kart.
#%% [markdown]
# ## Visning av kart
# For å vise kart skal vi bruke et hjelpebibliotek som heter `folium`. Dette baserer seg på `leaflet` som noen kanskje er kjent med.
#%%
import folium
#%% [markdown]
# For å vise et kart kjører du enkelt følgende kommando:
# (Sett gjerne inn dine egne koordinater her)
#%%
m = folium.Map(location = [ 58.7692591, 5.6675446 ])
m
#%% [markdown]
# _`m` helt alene brukes for å vise kartet i en Jupyter notebook_
#%% [markdown]
# Man kan og enkelt velge mellom flere forskjellige tiles. Her er ek
#%%
m = folium.Map(location = [ 58.7692591, 5.6675446 ], tiles = 'Stamen Terrain')
m