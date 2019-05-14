#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Notebooks'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Geometri
# Vi skal jobbe med biblioteket som heter `Shapely` som er et åpent bibliotek for manipulering og analyse av geometri.
# Biblioteket er her ferdig installert, men må i egen python installasjon manuelt.
#%% [markdown]
# Vi har lagd noen hjelpefunksjoner slik at det blir lettere. Kjør ruten under så får du tilgang til de senere

#%%
get_ipython().run_line_magic('matplotlib', 'inline')

from typing import List

from matplotlib import pyplot as plt
from shapely.geometry import Point


def plot_punkt(punkt: Point):
    """
    Plot et enkelt punkt på en graf
    """
    fig = plt.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.scatter(punkt.x, punkt.y)
    ax.set_title('Punkt')


def plot_punkter(punkter: List[Point]):
    """
    Plot flere punkter på samme plot
    """
    x = [punkt.x for punkt in punkter]
    y = [punkt.y for punkt in punkter]
    fig = plt.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    ax.set_title('Punkter')

#%% [markdown]
# For å definere et punkt lager vi et nytt `Point` objekt og lagrer objektet i en variabel slik at vi senere kan manipulere det.

#%%
punkt = Point(2,2)

#%% [markdown]
# Dersom du ønsker å se informasjon om objektet som ble opprettet kan du bruke `print()` funksjonen og sette punktobjektet som parameter

#%%
print(punkt)

#%% [markdown]
# Det er veldig enkelt å plotte punkter. Vi har lagd en liten hjelpefunksjon som tar seg av oppretting av figur, valg av tittel og litt sånne småting. Denne kan du se på etterpå for å lære mer. For å bruke denne sender du enkelt punktobjektet ditt inn som parameter i funksjonen `plot_punkt()`

#%%
plot_punkt(punkt)

#%% [markdown]
# Ett punkt er kanskje gøy, men vi kan enkelt lage så mange punkt vi bare vil!
# Lag en variabel som inneholder en tom liste.
# Deretter kan du legge til punkter i listen ved hjelp av `append` funksjonen du lærte om i forrige modul.
# 
# Når lista inneholder noen punkter kan du enkelt plotte ved å sende listen som parameter inn i `plot_punkter()`

#%%
punkter = []
punkter.append(Point(1,1))
punkter.append(Point(-1,10))
punkter.append(Point(5,7))
punkter.append(Point(3,2))

plot_punkter(punkter)


