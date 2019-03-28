# Introduksjonskurs

## Behandling av geografiske data i Python

4 moduler. 8 timer totalt.

Det er litt knapt med tid så kurset kommer til å gå relativt raskt og enkelte komponenter får ikke den fulle forklaringen de egentlig trenger. Det oppfordres og til å eksperimentere på egenhånd dersom du ligger litt foran. Skulle noe gå galt har vi ferdiglagde sjekkpunkter du enkelt kan åpne.

Vi bruker forhåndsoppsatte jupyter notebooks for å gjøre oppstartsprosessen enkel. Dette gjør og at vi på forhånd kan installere modulene som kreves og legge inn startmaler til oppgaver.

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

- Lister
  Hva er lister? Hvordan bruke dem? Hvilke fordeler gir det å lagre verdier i lister?

- Betingelser
  I all hovedsak enkle «if», «and» og «or».

- Imports?
  Overordnet forklaring av imports. Ingen dypdykk i hvordan man selv kan lage. Kun bruk.

- Bruk av forhåndlagde funksjoner
  Fordeler. Hvordan bruke.

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

- Markers
  Legge inn punkter i kartet og vise dem.

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

### Oppgave

- Gå til https://colab.research.google.com/notebooks/welcome.ipynb
- Trykk deg inn på _File_ > _New Python 3 Notebook_

Python inneholder det aller meste av basis funksjonalitet uten at du trenger gjøre noe særlig mer.
Start med å skrive følgende inn i linjen som er markert.

```python
print("Hei verden!")
```

Deretter kan du klikke på knappen `Run cell`, eller trykke _Ctrl+Enter_.
![Run]

[Run]:./images/Runcapture.JPG

Kodesnutten du har skrevet inn blir nå kjørt og resultatet vil vises nedenfor ruten.

`Hei verden!`

**TODO**
Hvordan tolkes Python koden? Hva er celler i Notebooks? Hva skjer dersom jeg kjører en celle? Har rekkefølgen noe å si? Hva er fordelen med celler kontra et langt script?
Vise _Runtime_ > _Run All_. Forklare forskjell på _Runtime_ > _Run All_ vs. _Runtime_ > _Restart and Run All_
Celler lar oss enkelt teste små deler av koden, i stedet for å kjøre alt hver gang (stor fordel med tanke på debug, learning-by-doing). 

Syntax Errors i Notebooks (spesielt Google Colaborator)

![SyntaxError]

[SyntaxError]:./images/Error.JPG

Kommer direkte med en knapp til _Stack Overflow_ (fungerer ikke som den skal akkurat nå?)
I dette tilfellet vil løsningen vil være å bruke 
```python
print("""Hei 
verden!""")
```
```
Hei
verden!
```


 i stedet. 
 Enkelt vist ved første resultat (Google Syntax Erroren). Slike feilmedlinger vil komme dersom cellen krasjer av en eller annen grunn. Det betyr at en tom output ikke nødvendigvis betyr at koden ikke fungerte.

 Hvert kapittel vil ha en fasit med en Notebook som inneholder all koden.
 https://colab.research.google.com/drive/1M0a-4eERWaMNPOXjTBMnRHs9xUKvHajq
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

### Datatyper

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `2.2 Datatyper`_

Programmeringsspråk skiller mellom forskjellige typer data.
Hovedtypene som blir brukt i python er:

- Tekst
  - Navn (Fredrik)
  - Steder (Oslo)
  - Stjernetegn (Skytten)
- Heltall
  - Alder (25)
  - Årstall (2019)
- Flyttall
  - Breddegrad (59.2345) _ENDRE_
  - Lengdegrad (6.2335) _ENDRE_

Python er som regel smart nok til å vite hvilken datatype som er riktig basert på innholdet.

La oss legge inn noen flere variabler som bruker noen av disse datatypene.

- `alder` skal inneholde din alder
- `årstall` skal inneholde året vi er
- `høyde` skal inneholde høyde

For meg blir det slik:

```python
navn = "Fredrik"
alder = 25
årstall = 2019
høyde = 1.75
```

Legg merke til at tekst blir skrevet med anførselstegn mens tall blir skrevet uten.
Det er for eksempel mulig å lagre tall som tekst hvis det skrives i anførselstegn: `tall_som_tekst = "15"`.

### Aritmetikk

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `2.3 Aritmetikk`_

Matematikk er viktig i dataverdenen og ikke minst når du koder.
Heldigvis er det veldig enkelt.
Matematiske operasjoner utføres rett frem akkurat som på barneskolen.

Lag en ny rute og skriv inn følgende:

```python
12 + 30
```

Trykk deretter run. Resultatet av kalkulasjonen vises nå under ruta.
Erstatt `+` med `-` (subtrasjon), `*` (multiplikasjon) og `/` (divisjon) og se hvordan resultatet endrer seg.

Resultatet av en kalkulasjon kan og lagres i en variabel slik at du kan bruke den senere.
Du kan for eksempel regne ut årstallet du ble født i på følgende måte:

```python
fødselsår = årstall - alder
print(fødselsår)
```

`1993`

Det er ikke sikkert resultat av denne stemmer siden den ikke bruker full dato.

Prøv nå å regne ut hvor mange centimeter du mangler for å bli 2 meter.

### Lister

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `2.4 Lister`_

Det kan noen ganger være lurt å lagre data i lister for å holde bedre struktur på dataene.

Se for deg at du skal lage en oversikt over byer du har vært i.
Du lagrer byene i variabler slik at det er lett å holder oversikt. _eller..._

```python
by1 = "Oslo"
by2 = "Stockholm"
by3 = "Wien"
by4 = "Berlin"
...
```

Dette blir fort veldig rotete når du begynner å få mange byer. Se for deg 10.000 linjer med steder du har besøkt.
Løsningen på problemet er å lagre dataene i en liste.
_Legg gjerne inn byer du selv har besøkt_

```python
byer = ["Oslo", "Stockholm", "Wien", "Berlin"]
print(byer)
```

`['Oslo', 'Stockholm', 'Wien', 'Berlin']`

Dette gir og muligheten for enkelt å fjerne eller legge til byer i listen. Det kan gjøres ved hjelp noen listefunksjoner som er innebygd i Python.

```python
byer.append("Trondheim")
byer.remove("Oslo")
print(byer)
```

`['Stockholm', 'Wien', 'Berlin', 'Trondheim']`

Vi kan og sjekke hvor mange byer vi har besøkt ved å skrive

```python
len(byer)
```

`4`

Sortering kan gjøres kjapt ved bruk av funksjonen ```.sort() ```. Så vi må skrive følgende

```python
byer.sort()
print(byer)
```

`['Berlin', 'Stockholm', 'Trondheim', 'Wien']`

_En liste med tekstelementer vil bli sortert alfabetisk, mens en liste med tall blir sortert i stigende rekkefølge. ```.sort()``` vil ikke fungere i lister som er blandet._

**TODO** Indexer i lister, hente spesifikke elementer

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

### Imports

**TODO**
Overordnet forklaring av imports. Ingen dypdykk i hvordan man selv kan lage. Kun bruk.
I Python, på lik linje med mange andre programmeringspråk, kan man importere biblioteker som andre har laget. Dette er diverse funksjonaliteter som du kan importere, og dermed ikke må skrive selv. Python har en rekke predefinerte bibliotek, som enkelt kan brukes ved å legge til en linje øverst i cellen.
F.eks:
```python
from math import pi
```
Denne vil importere funksjonalitet for å bruke _**pi**_ fra biblioteket _**math**_. For å importere all funksjonalitet fra et bibliotek på en gang kan man bruke
```python
from math import *
```

### Bruk av forhåndlagde funksjoner

**TODO**
Fordeler. Hvordan bruke.

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

### Kalkulering av distanse mellom punkter

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `3.2 Kalkulering av distanse`_
**TODO**
Lage flere punkter. Tegner linjer mellom og kalkulere distanser.

### Polygoner

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `3.3 Polygoner`_
**TODO**
Lage polygoner som består av flere punkter og vise de i plot.

---

## Kart med OpenStreetMap

Åpne filen `4 Kart`

### Geokoding

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `4.1 Geokoding`_

Geokoding er en kjent del av GIS-hverdagen. Fordelen med Python og koding er at du kan automatisere geokoding av store datasett.
Vi har jukset litt og forhåndlags en liten funksjon som tar seg av arbeidet.

```python
lengdegrad, breddegrad = geokoding("Schweigaardsgate 28, Oslo")
print((lengdegrad, breddegrad))
##TODO Sjekk at print stemmer
```

Revers geokoding er og mulig:

```python
plassering = revers_geokoding(59.91029, 10.76337)
print(plassering)
```

Vi kan og bruke en liste med adresser og geokode disse:

```python
adresser = ["Schweigaardsgate 28, Oslo", "Gabels Gate 21, Oslo", "Austhallet 17, Klepp Stasjon"]

koordinater = []
for adresse in adresser:
    koordinater.append(geokoding(adresse))

print(koordinater)
```

På denne måten kan vi enkelt plotte punktene i et kart ved en senere anledning.

### Dynamiske kart med Folium

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `4.2 Dynamiske Kart`_
**TODO**
Hvordan vise et kart.

### Markers

_Dersom du henger etter eller trenger å rydde opp i filen din fort kan du åpne `4.3 Markers`_
**TODO**
Legge inn punkter i kartet og vise dem.
