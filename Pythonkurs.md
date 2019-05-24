# Introduksjonskurs

## Behandling av geografiske data i Python

4 moduler. 8 timer totalt.

Det er litt knapt med tid så kurset kommer til å gå relativt raskt og enkelte komponenter får ikke den fulle forklaringen de egentlig trenger. Det oppfordres til å eksperimentere på egenhånd dersom du ligger litt foran.

Vi bruker forhåndsoppsatte jupyter notebooks for å gjøre oppstartsprosessen enkel. Dette gjør og at vi på forhånd kan installere modulene som kreves og legge inn startmaler til oppgaver.

Alle oppgavene og koden du skriver blir liggende i skyen slik at du kan jobbe videre med det etter fullført kurs. På slutten har vi og lagd ved noen lenker og instruksjoner til hvordan du kan komme igang på lokal maskin.

---

## Kursoversikt

### 1. Introduksjon til Python og miljøet (1 time)

- Jupyter
  
  Hva er jupyter notebooks? Hvilke fordeler gir det meg? Hvordan brukes de?

- “Hello World!”
  
  Testkjøring av enkelt script og forklaring av hvordan python fungerer og tolker koden

### 2. Programmeringskonsepter (2+ timer)

- Variabler
  
  Hva er variabler? Hvordan bruke dem? Hvorfor bruke dem?

- Datatyper
  
  Forskjellen mellom datatyper

- Aritmetikk
  
  Enkle beregninger i Python

- Bruk av forhåndslagde og innebygde funksjoner
  
  Fordeler. Hvordan bruke.

- Input

  Hva kan det brukes til. Fordeler med interaksjon mens et script kjører

- Lister
  
  Hva er lister? Hvordan bruke dem? Hvilke fordeler gir det å lagre verdier i lister?

- Betingelser
  
  Logiske valg og gjentakelser. "If-setning" og "for-løkker".

- Imports
  
  Overordnet forklaring av imports. Ingen dypdykk i hvordan man selv kan lage. Kun bruk.

### 3. Geometri (2 timer)

- Punkter
  
  Hvordan lage punkter og vise de i et plot.

- Kalkulering av distanse mellom punkter
  
  Lage flere punkter. Tegner linjer mellom og kalkulere distanser.

- Polygoner
  
  Lage polygoner som består av flere punkter og vise de i plot.

### 4. Kart med OpenStreetMap (3 timer)

- Geokoding
  
  Geokoding ved hjelp av webtjenester.

- Dynamiske kart med Folium
  
  Hvordan vise et kart.

- Markers og Shapes
  
  Legge inn enkle elementer i kartet og vise dem.

---

## Introduksjon til Python og Jupytermiljøet

5 gode grunner til å bruke Python i GIS-hverdagen din:

- Automatisering av oppgaver
- Enkelt å komme i gang
- Gode moduler som kan plugges rett inn
- Støttet av de fleste store GIS verktøy
- Python passerte nylig Java i popularitet og er nå #1

(Vise noen bruksområder for Python i vår hverdag?)

## Jupyter Notebooks

Jupyter Notebooks gir muligheten for å kjøre pythonkode direkte i nettleseren uten at du trenger å installere noe. Det gir også mulighter for en visuell fremstilling og endring av deler av koden kan gjøres fort. Det finnes flere måter å kjøre Jupyter Notebooks på.

I dette kurset skal vi bruke **Google Colaboratory**.

### Opprett eget Jupytermiljø

- Gå til <https://colab.research.google.com/notebooks/welcome.ipynb>
- Trykk deg inn på _File_ > _New Python 3 Notebook_

Python inneholder det aller meste av basis funksjonalitet uten at du trenger gjøre noe særlig mer.

_I dette kurset brukes Python 3. Det finnes noen små syntaxforskjeller sammenlignet med Python 2. Blant annet kreves ikke parenteser i print i Python 2._

Start med å skrive følgende inn i linjen som er markert.

```python
print("Hei verden!")
```

Deretter kan du klikke på knappen `Run cell`, eller trykke _Ctrl+Enter_.

![Run]

[Run]:./images/Runcapture.JPG

Kodesnutten du har skrevet inn blir nå kjørt og resultatet vil vises nedenfor ruten.

`Hei verden!`

Flere fordeler i Jupyter/Google Colaborator:

![Run2]

[Run2]:./images/Runcapture2.JPG

Systemet inneholder innebygd funksjonalitet for om cellen har blitt kjørt siden de siste endringene, hvem den ble kjørt av (mulig å dele kode, og jobbe sammen på kode), når den ble kjørt, og hvor lang tid det tok å kjøre den.

**TODO**
Hvordan tolkes Python koden? Hva er celler i Notebooks? Hva skjer dersom jeg kjører en celle? Har rekkefølgen noe å si? Hva er fordelen med celler kontra et langt script?
Vise _Runtime_ > _Run All_. Forklare forskjell på _Runtime_ > _Run All_ vs. _Runtime_ > _Restart and Run All_
Celler lar oss enkelt teste små deler av koden, i stedet for å kjøre alt hver gang (stor fordel med tanke på debug, learning-by-doing).
Innebygde code snippets man kan hente (f.eks Camera Capture)

#### Syntax Errors i Notebooks (spesielt i Google Colaborator)

La oss prøve å printe `Hei verden!` på to linjer.

```text
Hei
verden!
```

Et forsøk kan for eksempel være:

![SyntaxError]

[SyntaxError]:./images/Error.JPG

Kommer direkte med en knapp til _Stack Overflow_ (fungerer ikke som den skal akkurat nå?)

Enkelt vist ved første resultat (Google Syntax Erroren). Slike feilmedlinger vil komme dersom cellen krasjer av en eller annen grunn. Det betyr at en tom output ikke nødvendigvis betyr at koden ikke fungerte.

#### Oppgave 1.1

Skriv `Hei Verden!` på to linjer.
<details><summary>Løsning Oppgave 1.1</summary>
<p>

```python
print("""Hei
verden!""")
```

eller

```python
print("Hei")
print("verden!")
```

</p>
</details>

---

Hvert kapittel vil ha en fasit med en Notebook som inneholder all koden.
<https://colab.research.google.com/drive/1M0a-4eERWaMNPOXjTBMnRHs9xUKvHajq>
Du kan trykke på _OPEN IN PLAYGROUND_ for å skrive og gjøre endringer selv. Du kan også bruke _File_ > _Save a copy..._ for å lagre Notebooken selv.

---

## Programmeringskonsepter

Denne modulen gjennomgår grunnleggende programmeringskonsepter.
Åpne filen `2 Programmeringskonsepter`

### Variabler

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `2.1 Variabler`_
En variabel er et sted hvor du kan lagre data for senere bruk.
De gir oss og muligheten til å gi beskrivende navn til dataen vi lagrer.

Lag en variabel som heter `navn` som har verdien til navnet ditt:

```python
navn = "Fredrik"
```

Kjør ruten. De vil nå ikke komme noe resultat siden vi ikke bruker `print`.
Legg inn en `print``i samme rute slik at vi kan se hva verdien av variabelen er:

```python
navn = "Fredrik"
print(navn)
```

Nå skal navnet ditt vises under ruten.

#### Oppgave 2.1

Lag to variabler med ditt _fornavn_ og _etternavn_. Print disse på to linjer.
<details><summary>Løsning Oppgave 2.1</summary>
<p>

```python
fornavn = "Fredrik"
etternavn = "Bore"
print(fornavn)
print(etternavn)
```

</p>
</details>

---

### Datatyper

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `2.2 Datatyper`_

Programmeringsspråk skiller mellom forskjellige typer data.
Hovedtypene som blir brukt i python er:

- Tekststreng
  - Navn ("Fredrik")
  - Steder ("Oslo")
- Heltall
  - Alder (25)
  - Årstall (2019)
- Flyttall
  - Høyde (1.75)
- Boolean
  - _True_ | _False_

Python er som regel smart nok til å vite hvilken datatype som er riktig basert på innholdet.

Legg merke til at tekst blir skrevet med anførselstegn mens tall blir skrevet uten.
Det er for eksempel mulig å lagre tall som tekst hvis det skrives i anførselstegn: `tall_som_tekst = "15"`. Hvorfor er det viktig å lagre variabler med riktig datatype?

La oss legge inn noen flere variabler som bruker noen av disse datatypene.

#### Oppgave 2.2

Skriv inn følgende og kjør koden

```python
print(2 + 2)
```

```python
print('2' + 2)
```

```python
print('2' + '2')
```

```python
print('2 + 2')
```

Kan du forklare hva som skjer? (_En av de vil gi feilmelding_)

<details><summary>Løsning Oppgave 2.2</summary>
<p>

`4` - Plusset sammen to heltall

`TypeError` - Forsøkte å plusse sammen en streng og et heltall (Det går ikke)

`22` - Satt sammen to tekststrenger

`2 + 2` - Printet en hel sammenhengende tekststrengen

</p>
</details>

#### Oppgave 2.3

Lag variabler for _navn_, _alder_, _årstall_ og _høyde_.

- `navn` skal inneholder ditt navn som tekststreng
- `fødselsår` skal inneholde året du ble født som heltall
- `årstall` skal inneholde året vi er i som heltall
- `høyde` skal inneholde din høyde som flyttall

<details><summary>Løsning Oppgave 2.3</summary>
<p>

```python
navn = "Fredrik"
fødselsår = 1993
årstall = 2019
høyde = 1.75
```

</p>
</details>

---

### Aritmetikk

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `2.3 Aritmetikk`_

Matematikk er viktig i dataverdenen og ikke minst når du koder.
Heldigvis er det veldig enkelt.
Matematiske operasjoner utføres rett frem akkurat som på en vanlig kalkulator.

Lag en ny rute og skriv inn følgende:

```python
30 + 12
```

Trykk deretter run. Resultatet av kalkulasjonen vises nå under ruta.
Symbolene i Python for de vanligste operasjonene er (Arithmetic Operators):

- `+` - Addisjon
- `-` - Subtraksjon
- `*` - Multiplikasjon
- `/` - Divisjon
- `**`- Potens
- `%` - Modulo

Bytt gjerne regneart i eksemplet og se hvordan resultatet endrer seg.

Resultatet av en kalkulasjon kan og lagres i en variabel slik at du kan bruke den senere.

Du kan også bruke variablene du har definert tidligere til å beregne nye variabler. For eksempel kan du regne ut hvor mange år du fyller i år på følgende måte:

```python
alder = årstall - fødselsår
print(alder)
```

`26`

#### Oppgave 2.4

1. Beregn og print ut hvor mange centimeter du har igjen til 2 meter ved å bruke variablen `høyde` fra Oppgave 2.3

2. Kan man bruke noen aritmetiske operasjoner...

    1. mellom to tekststrenger?
    2. mellom en tekststreng og et heltall?

<details><summary>Løsning Oppgave 2.4</summary>
<p>

- Deloppgave 1

```python
høyde = 1.75

høydeimeter = 2 - høyde
print(høydeimeter * 100)
```

- Deloppgave 2.1
Ja, man kan plusse sammen to strenger

```python
print("Streng1 " + "Streng2")
```

`Streng1 Streng2`

- Deloppgave 2.2

```python
print("Streng1 " * 3)
```

`Streng1 Streng1 Streng1 `
</p>
</details>

---

### Bruk av forhåndlagde og innebygde funksjoner

**TODO**
Funksjoner er et viktig konsept i Python og de fleste andre programmeringsspråk. Enhver funksjon vil alltid ha en input og en output. Python har massevis av innebygde funksjoner, som hjelper deg med enkel funksjonalitet. Noen viktige eksempler:

- `print()`
  
  Tar en variabel som input, og printer dette til output

- `str()`
  
  Gjør om et tall til en tekststreng

- `int()`

  Gjør om en tekststreng til et heltall

- `len()`
  
  Gir deg lengden på variabelen du sender inn

- `input()`

  Gir deg mulighet til å skrive inn en input

Vi har allerede brukt den innebygde `print()` funksjonen, med en input av det vi ønsker å printe. Man kan også lage og definere egne funksjoner. En enorm fordel med dette er at funksjonalitet på denne måten kan gjenbrukes, og kode som du ellers ville skrevet om og om igjen kan kalles med en enkel funksjon.

#### Oppgave 2.4

Print `Året er: 2019` ved å:

1. Lage en ny tekststreng variabel ("Året er: ")
2. Bruke variabelen `årstall` fra Oppgave 2.2 og gjør den om til en tekststreng
3. Legge sammen strengene, og printe disse

<details><summary>Løsning Oppgave 2.4</summary>
<p>

```python
årstall = 2019

tekststreng = "Året er: "
årstallstreng = str(årstall)
print(tekststreng + årstallstreng)
```

</p>
</details>

---

### TODO Input

Input-funksjonen er viktig for interaksjon med programmet mens det kjører...
`input()` returnerer det man oppgir som streng. Viktig å gjøre om dersom 

#### TODO Oppgave 2.x

1. Lag et inputfelt hvor brukeren skriver skal inn et tall (Hint: bruk `int()` sammen med `input()`).
2. Print ut det dobbelte av tallet brukeren har oppgitt.

<details><summary>Løsning Oppgave 2.x</summary>
<p>

TODO Løsning

</p>
</details>

---

### Lister

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `2.4 Lister`_

Det kan noen ganger være lurt å lagre data i lister for å ha bedre struktur på dataene.

Se for deg at du skal lage en oversikt over byer du har vært i.
Du lagrer byene i variabler slik at det er lett å holde oversikt. _eller..._

```python
by1 = "Oslo"
by2 = "Stockholm"
by3 = "Wien"
by4 = "Berlin"
...
```

Dette blir fort veldig rotete når du begynner å få mange byer. Tenk deg at skal lagre 10.000 linjer med steder du har besøkt.
Løsningen på problemet er å lagre dataene i en liste.
_Legg gjerne inn byer du selv har besøkt_

```python
byer = ["Oslo", "Stockholm", "Wien", "Berlin"]
print(byer)
```

`['Oslo', 'Stockholm', 'Wien', 'Berlin']`

Dette gir og muligheten for enkelt å fjerne eller legge til byer i listen. Det kan gjøres ved hjelp av noen listefunksjoner som er innebygd i Python.

```python
byer.append("Trondheim")
byer.remove("Oslo")
print(byer)
```

`['Stockholm', 'Wien', 'Berlin', 'Trondheim']`

Den innebygde funksjonen `len()` kan brukes på lister for å sjekke hvor mange objekter som ligger i listen. Vi kan sjekke hvor mange byer vi har besøkt ved å skrive

```python
len(byer)
```

`4`

Sortering kan gjøres kjapt ved bruk av funksjonen ```.sort()```. Så vi må skrive følgende

```python
byer.sort()
print(byer)
```

`['Berlin', 'Stockholm', 'Trondheim', 'Wien']`

_En liste med tekstelementer vil bli sortert alfabetisk, mens en liste med tall blir sortert i stigende rekkefølge. ```.sort()``` vil ikke fungere i lister som er blandet._

**TODO** Indekser i lister, hente spesifikke elementer
I tillegg er det i mange tilfeller interessant å finne ut av hva en liste inneholder på et spesielt sted (for eksempel hva det første elementet i listen er). Vi kan bruke indekser til dette. Indeksen til et element er plasseringen i listen.

```python
førsteby = byer[0]
print(førsteby)
```

`Berlin`

**NB!** _Python har null-basert indeksering, noe som betyr at det første elementet ligger på indeks [0], det andre elementet ligger på indeks [1] osv._

**Oppgave 2.5**
**TODO** Legg til en oppgave om .append() og .remove()

1. Lag en liste med 10 forskjellige heltall mellom 0 og 100 i tilfeldig rekkefølge.
2. Print listen du har laget.
3. Finn ut hva det 6. laveste tallet i din liste er ved å sortere listen og bruke indekser.

<details><summary>Løsning Oppgave 2.5</summary>
<p>

```python
talliste = [11,2,84,72,36,90,15,82,10,55]
print(talliste)
talliste.sort()
sjettetallet = talliste[5]
print(sjettetallet)
```

`[11, 2, 84, 72, 36, 90, 15, 82, 10, 55]`

`55`

Husk at Python har null-basert indeksering, så det sjette tallet er på indeks _[5]_.

</p>
</details>

---

### Betingelser

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `2.5 Betingelser`_

Betingelser er et av de viktigste konseptene å forstå.
Det er heldigvis veldig enkelt og logisk i Python.

Betingelser handler om å utføre en handling hvis et utsagn er sant og eventuelt utføre en annen handling dersom det er usant.

Se for deg at du vil printe `Du har besøkt byen` dersom en by befinner seg i lista og motsatt skrive `Du har ikke besøkt byen` dersom den ikke er i lista over byer du har besøkt.
Hvis vi skulle skrevet dette på klart språk hadde det sett ca slik ut:

```plaintext
Hvis by finnes i listen over byer jeg har besøkt:
  print("Du har besøkt byen")
Dersom den ikke finnes:
  print("Du har ikke besøkt byen")
```

I Python er det veldig lett å oversette en slik setning til kode. Det kan også være anbefalt å først skrive utsagnet i klartekst for så å gjøre det om til kode.

```python
by = "Oslo"

if by in byer:
  print("Du har besøkt byen")
else:
  print("Du har ikke besøkt byen")
```

Prøv å bytte ut `by` med en by du har besøkt og en du ikke har besøkt og se hvordan resultatet endrer seg.

#### Oppgave 2.6

1. Lag en liste over 3 land du har besøkt
2. Lag en ny variabel med et land du har besøkt (Det kan være et land som ligger i listen, eller et nytt land)
3. Lag logikk for

```plaintext
Hvis landet finnes i listen over land jeg har besøkt:
  print("Landet ligger allerede i listen")
Dersom den ikke finnes:
  Legg til landet i listen (Hint: Bruk .append())
  Print listen over land
```

<details><summary>Løsning Oppgave 2.6</summary>
<p>

```python
land = ["Canada","Brasil","Italia"]
nyttland = "Sveits"

if nyttland in land:
  print("Landet ligger allerede i listen")
else:
  land.append(nyttland)
  print(land)
```

</p>
</details>

---

### Imports

Veldig mye av det vi programmerer, er standard funksjonalitet som andre har utviklet før oss. Det er viktig å kunne bruke funksjonalitet som allerede finnes. I Python, på lik linje med mange andre programmeringspråk, kan man importere biblioteker med funksjoner som andre har laget. Dette er diverse funksjonaliteter som du kan importere, og dermed ikke må skrive selv. Python har en rekke predefinerte bibliotek, som enkelt kan brukes ved å legge til en linje øverst i cellen.

F.eks:

```python
from math import pi
```

Denne vil importere funksjonalitet for å bruke _**pi**_ fra biblioteket _**math**_. Dette er et bibliotek for bruk av en rekke enkle matematiske funksjonaliteter. For å importere all funksjonalitet fra et bibliotek på en gang kan man bruke:

```python
from math import *
```

#### Oppgave 2.7

Importer funksjonaliteten _shuffle_ fra biblioteket _random_. Deretter kan du bruke funksjonen _shuffle()_. Bruk denne til å stokke om listen med tall fra Oppgave 2.5

<details><summary>Løsning Oppgave 2.7</summary>
<p>

```python
talliste = [11,2,84,72,36,90,15,82,10,55]

from random import shuffle
shuffle(talliste)
print(talliste)
```

</p>
</details>

---

## Geometri

Åpne filen `3 Geometri`

### Punkter

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `3.1 Punkter`_

Vi skal jobbe med biblioteket som heter `Shapely` som er et åpent bibliotek for manipulering og analyse av geometri.
Biblioteket er ferdig installert av oss.

Vi vil ha muligheten til å jobbe med punkter og skriver derfor følgende i første rute:

```python
from shapely.geometry import Point
```

Nå har vi tilgang til å bruke `Point`.
Punkter opprettes ved å lage et `Point` objekt og lagre det i en variabel.

```python
punkt = Point(2,2)
```

Vi har lagd klar noen funksjoner for å enkelt plotte dataene.

```python
plot_punkt(punkt)
```

Du vil nå få opp en graf tilsvarende denne:
_ENDRE DENNE_

Et enkelt punkt er jo ganske kjedelig så la oss legge inn en haug!
Opprett en liste og legg til så mange punkter du orker.

```python
punkter = []
punkter.append(Point(1,1))
punkter.append(Point(-1,10))
punkter.append(Point(5,7))
punkter.append(Point(3,2))

plot_punkter(punkter)
```

_Legg merke til at funksjonen nå heter `plot_punkter` og ikke `plot_punkt`_

**TODO** Oppgave 3.1

### Kalkulering av distanse mellom punkter

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `3.2 Kalkulering av distanse`_
**TODO**
Lage flere punkter. Tegner linjer mellom og kalkulere distanser.

**TODO** Oppgave 3.2

### Polygoner

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `3.3 Polygoner`_
**TODO**
Lage polygoner som består av flere punkter og vise de i plot.

**TODO** Oppgave 3.3

---

## Kart med OpenStreetMap

Åpne filen `4 Kart`, eller manuelt kopier geokoding funksjonene:

<details><summary> Geokoding funksjoner </summary>
<p>

```python
import requests

brukernavn = ""
passord = ""
# Henter token fra ArcGIS Server
tokenparametre = {'username': brukernavn, 'password': passord, 'f': 'pjson', 'client': 'requestip'}
tokenforespørsel = requests.get("https://services.geodataonline.no/arcgis/tokens/generateToken",
                                params=tokenparametre)

token = tokenforespørsel.json()['token']

def geokoding(søketekst: str, koordinatsystem = 25833):
    """"
    Geokod ved hjelp av fritekst søk
    Standard koordinatsystem er UTM-33
    For bruk av WGS 84 bruk ID: 4326
    """

    endepunkt = "https://services.geodataonline.no/arcgis/rest/services/Geosok/GeosokLokasjon2/GeocodeServer/findAddressCandidates"
    parametre = {'SingleLine': søketekst, 'outSR': koordinatsystem, 'f': 'pjson', 'token': token}

    forespørsel = requests.get(endepunkt,
                               params=parametre)

    return (forespørsel.json()['candidates'][0]['location']['x'],
            forespørsel.json()['candidates'][0]['location']['y'])

def revers_geokoding(breddegrad, lengdegrad, koordinatsystem = 25833):
    """"Revers geokod"""

    endepunkt = "https://services.geodataonline.no/arcgis/rest/services/Geosok/GeosokLokasjon2/GeocodeServer/reverseGeocode"
    parametre = {'location': f"{breddegrad}, {lengdegrad}", 'outSR': koordinatsystem, 'f': 'pjson', 'token': token}

    forespørsel = requests.get(endepunkt,
                               params=parametre)

    return forespørsel.json()['address']
```

</p>
</details>

Fyll deretter inn brukernavn og passord.

---

### Geokoding

Geokoding er en kjent del av GIS-hverdagen. Fordelen med Python og koding er at du kan automatisere geokoding av store datasett.
Vi har jukset litt og forhåndlaget en liten funksjon `geokoding()` som tar seg av arbeidet.

```python
lengdegrad, breddegrad = geokoding("Schweigaardsgate 28, Oslo")
print((lengdegrad, breddegrad))
```

```text
(263158.4893784048, 6649002.460467065)
```

Revers geokoding er og mulig:

```python
plassering = revers_geokoding(59.91029, 10.76337)
print(plassering)
```

```text
{
  'Adresse': 'Schweigaards gate 28',
  'Stedsnavn': None,
  'Postnummer': '0191',
  'Poststed': 'Oslo',
  'Kommune': 'Oslo',
  'GNR': None,
  'BNR': None,
  'FNR': None,
  'SNR': None,
  'Loc_name': 'Adresse'
}
```

Vi kan og bruke en liste med adresser og geokode disse:

```python
adresser = ["Schweigaardsgate 28, Oslo", "Gabels Gate 21, Oslo", "Austhallet 17, Klepp Stasjon"]

koordinater = []

for adresse in adresser:
    koordinater.append(geokoding(adresse))

print(koordinater)
```

```text
[(263158.4893784048, 6649002.460467065),
 (260215.4204419753, 6649640.687409842),
 (-38516.53384195722, 6551979.74641538)]
```

På denne måten kan vi enkelt plotte punktene i et kart ved en senere anledning.

#### Oppgave 4.1.1

Finn koordinatene til stedet du bor (eller et valgfritt annet sted) og print de.

<details><summary>Løsning Oppgave 4.1.1</summary>
<p>

```python
lengdegrad, breddegrad = geokoding("<DIN ADRESSE>")
print((lengdegrad, breddegrad))
```

</p>
</details>

#### Oppgave 4.1.2

Bruk revers geokoding på koordinatene du fant og analyser resultatet.
Stemmer alt av detaljer?

<details><summary>Løsning Oppgave 4.1.2</summary>
<p>

```python
plassering = revers_geokoding(lengdegrad, breddegrad)
print(plassering)
```

</p>
</details>

### Dynamiske kart med Folium

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `4.2 Dynamiske Kart`_

For å vise kart skal vi bruke et hjelpebibliotek som heter `folium`. Dette baserer seg på `leaflet` som noen kanskje er kjent med.

For å opprette et kart med folium trenger du bare skrive følgende:

```python
m = folium.Map(location = [ lengdegrad, breddegrad ])
m
```

Tips: `m` som står alene er for å vise kartet i notebooks.

![Kart]

[Kart]: ./images/kart.png

Det er enkelt å legge til ekstra valg som for eksempel forskjellige basemaps og zoomnivåer ved hjelp av følgende valg:

```text
tiles - Valg av basemap
zoom_start - Zoomnivå
```

Mulige Basemaps:

- 'openstreetmap',
- 'mapquestopen',
- 'MapQuest Open Aerial',
- 'Mapbox Bright',
- 'Mapbox Control Room',
- 'stamenterrain',
- 'stamentoner',
- 'stamenwatercolor',
- 'cartodbpositron',
- 'cartodbdark_matter'

Bruk `folium.LatLngPopup().add_to(m)` eller `m.add_child(folium.LatLngPopup())` for å finne ønsket posisjon.

**NB!** _Ikke alle bakgrunnskart fungerer på alle zoomnivåer._

Eksempel:

```python
m = folium.Map(location = [ 58.7692591, 5.6675446 ],
               tiles = 'Stamen Terrain',
               zoom_start = 15)
m
```

#### Oppgave 4.2

Bruk lengde- og breddegraden du geokodet i forrige oppgave til å opprette et nytt kart og vis det i notebooken. Sett eget zoomnivå og basemap.

Bonus: Lag egen basemap-velger ved å legge til flere basemaps med `folium.TileLayer(SETT INN BASEMAP HER).add_to(m)` og `folium.LayerControl().add_to(m)`


<details><summary>Løsning Oppgave 4.2</summary>
<p>

```python
m = folium.Map(location=[59.9103, 10.7634],
    tiles='Stamen Toner',
    zoom_start=16
)

folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('stamentoner').add_to(m)
folium.LayerControl().add_to(m)

m
```

</p>
</details>

### Markers og Shapes

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `4.3 Markers`_

**TODO**
Legge inn punkter i kartet og vise dem.

Marker med popup (kan bruke HTML tags her), tooltip, icon(folium.Icon), dynamisk `.add_to(m)`

Eksempel:

```python
folium.Marker(
    [59.9103, 10.7634],
    popup='Geodata AS'
).add_to(m)
```

Icon: Folium bruker glyphicon (<https://getbootstrap.com/docs/3.3/components/#glyphicons-glyphs>):

Eksempel:

`folium.Icon(color='lightgray', icon='step-backward', prefix='fa')`


Shapes: Circles veldig enkelt i Folium.

Eksempel:

```python
folium.Circle(
    radius=100,
    location=[59.9103, 10.7634],
    popup='Dette er en sirkel rundt Geodata AS',
    color='crimson',
    fill=True,
).add_to(m)
```

**TODO** Oppgave 4.3
Lag liste over byer du har besøkt. Bruk geokoder for å finne koordinater. Legg disse i ny liste. Lag et kart med markers for alle byene.

<details><summary>Løsning Oppgave 4.3</summary>
<p>

```python

```

</p>
</details>

**HVIS TID**
Plotting av linjer:
<https://deparkes.co.uk/2016/06/03/plot-lines-in-folium/>