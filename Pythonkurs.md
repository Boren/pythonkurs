# Introduksjonskurs

## Behandling av geografiske data i Python

4 moduler. 9 timer totalt.

Kurset kommer til å gå relativt raskt for å rekke alt på en dag. Det oppfordres til å eksperimentere på egenhånd dersom du ligger litt foran.

Vi bruker forhåndsoppsatte jupyter notebooks i Google Colaboratory for å gjøre oppstartsprosessen enkel. Dette gjør og at det på forhånd er installert moduler som kreves.

Alle oppgavene og koden du skriver blir liggende i skyen på din egen Googlekonto slik at du kan jobbe videre med det etter fullført kurs.

---

## Kursoversikt

### 1. Introduksjon til Python og miljøet (1 time)

#### Jupyter

Hva er jupyter notebooks? Hvilke fordeler gir det meg? Hvordan brukes de?

#### “Hello World!”

Testkjøring av enkelt script og forklaring av hvordan python fungerer og tolker koden

### 2. Programmeringskonsepter (3 timer)

#### Variabler

Hva er variabler? Hvordan bruke dem? Hvorfor bruke dem?

#### Datatyper

Forskjellen mellom datatyper

#### Aritmetikk

Enkle beregninger i Python

#### Bruk av forhåndslagde og innebygde funksjoner

Fordeler. Hvordan bruke.

#### Input

Hva kan det brukes til. Fordeler med interaksjon mens et script kjører

#### Lister

Hva er lister? Hvordan bruke dem? Hvilke fordeler gir det å lagre verdier i lister?

#### Betingelser

Logiske valg og gjentakelser. `if`-setninger og `for`-løkker.

#### Imports

Overordnet forklaring av imports. Ingen dypdykk i hvordan man selv kan lage. Kun bruk.

### 3. Geometri (2 timer)

#### Punkter

Hvordan lage punkter og vise de i et plot.

#### Linjer

Lage lister med flere punkter. Tegne linjer.

#### Polygoner

Lage polygoner som består av flere punkter og vise de i plot.

### 4. Kart med OpenStreetMap (3 timer)

#### Geokoding

Geokoding ved hjelp av webtjenester.

#### Dynamiske kart med Folium

Hvordan vise et kart.

#### Markers og Shapes

Legge inn enkle elementer i kartet og vise dem.

<div style="page-break-after: always;"></div>

## Introduksjon til Python og Jupytermiljøet

5 gode grunner til å bruke Python i GIS-hverdagen din:

- Automatisering av oppgaver
- Enkelt å komme i gang
- Gode moduler som kan plugges rett inn
- Støttet av de fleste store GIS verktøy
- Python passerte nylig Java i popularitet og er nå #1

## Jupyter Notebooks

Jupyter Notebooks gir muligheten for å kjøre pythonkode direkte i nettleseren uten at du trenger å installere noe. Det gir også mulighter for en visuell fremstilling og endring av deler av koden kan gjøres fort. Det finnes flere måter å kjøre Jupyter Notebooks på.

I dette kurset skal vi bruke **Google Colaboratory** som inneholder de aller meste du trenger av pakker. Det er enkelt å lagre og dele kode her.

### Opprett eget Jupytermiljø

- Gå til <https://colab.research.google.com>
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

Kommer direkte med en knapp til _Stack Overflow_ (Gjør Googlesøk på feilen)

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

<div style="page-break-after: always;"></div>

## Programmeringskonsepter

Denne modulen gjennomgår grunnleggende programmeringskonsepter.

### Variabler

En variabel er et sted hvor du kan lagre data for senere bruk.
De gir oss og muligheten til å gi beskrivende navn til dataen vi lagrer.

Lag en variabel som heter `navn` som har verdien til navnet ditt:

```python
navn = "William"
```

Kjør ruten. De vil nå ikke komme noe resultat siden vi ikke bruker `print`.
Legg inn en `print` i samme rute slik at vi kan se hva verdien av variabelen er:

```python
navn = "William"
print(navn)
```

Nå skal navnet ditt vises under ruten.

#### Oppgave 2.1

Lag to variabler med ditt _fornavn_ og _etternavn_. Print disse på to linjer.
<details><summary>Løsning Oppgave 2.1</summary>
<p>

```python
fornavn = "William"
etternavn = "Wisting"
print(fornavn)
print(etternavn)
```

</p>
</details>

---

### Datatyper

Programmeringsspråk skiller mellom forskjellige typer data.
Hovedtypene som blir brukt i python er:

- Tekststreng
  - Navn ("William")
  - Steder ("Larvik")
- Heltall
  - Alder (61)
  - Årstall (2019)
- Flyttall
  - Høyde (1.91)
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

`2 + 2` - Printet en hel sammenhengende tekststreng

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
navn = "William"
fødselsår = 1958
årstall = 2019
høyde = 1.91
```

</p>
</details>

---

### Aritmetikk

Matematikk er viktig i dataverdenen og ikke minst når du koder.
Heldigvis er det veldig enkelt.
Matematiske operasjoner utføres rett frem akkurat som på en vanlig kalkulator.

Lag en ny rute og skriv inn følgende:

```python
30 + 12
```

Trykk deretter run. Resultatet av kalkulasjonen vises nå under ruta.
Symbolene i Python for de vanligste operasjonene er:

- `+` - Addisjon
- `-` - Subtraksjon
- `*` - Multiplikasjon
- `/` - Divisjon
- `**` - Potens
- `%` - Modulo

Bytt gjerne regneart i eksemplet og se hvordan resultatet endrer seg.

Resultatet av en kalkulasjon kan lagres i en variabel slik at du kan bruke den senere.

Du kan også bruke variablene du har definert tidligere til å beregne nye variabler. For eksempel kan du regne ut hvor mange år du fyller i år på følgende måte:

```python
alder = årstall - fødselsår
print(alder)
```

`26`

#### Oppgave 2.4

Beregn og print ut hvor mange *centimeter* du har igjen til 2 meter ved å bruke variablen `høyde` fra Oppgave 2.3

<details><summary>Løsning Oppgave 2.4</summary>
<p>

```python
høyde = 1.91

høydeimeter = 2 - høyde
print(høydeimeter * 100)
```

</p>
</details>

#### Oppgave 2.5

Kan man bruke noen aritmetiske operasjoner...

  1. mellom to tekststrenger?
  2. mellom en tekststreng og et heltall?

Test det gjerne i notebooken!

<details><summary>Løsning Oppgave 2.5</summary>
<p>

1. Ja, man kan plusse sammen to strenger

```python
print("Streng1 " + "Streng2")
```

```plaintext
Streng1 Streng2
```

2. Ja, man kan multiplisere en streng slik at den repeterer

```python
print("Streng1 " * 3)
```

```plaintext
Streng1 Streng1 Streng1
```

</p>
</details>

---

### Bruk av forhåndlagde og innebygde funksjoner

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

#### Oppgave 2.6

Print `Året er: 2019` ved å:

1. Lage en ny tekststreng variabel ("Året er: ")
2. Bruke variabelen `årstall` fra Oppgave 2.3 og gjør den om til en tekststreng
3. Legge sammen strengene, og printe disse

<details><summary>Løsning Oppgave 2.6</summary>
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

### Input

Input-funksjonen er viktig for interaksjon med programmet mens det kjører.
Etter at en linje som inneholder funksjonen har kjørt venter programmet på at brukeren skriver inn noe og trykker `Enter`.

![InputCapture]

[InputCapture]:./images/InputCapture.JPG

`input()` returnerer det brukeren oppgir som en streng. Viktig å gjøre om til andre datatyper manuelt dersom det er behov.

#### Oppgave 2.7

1. Lag et inputfelt hvor brukeren skriver inn et tall (Hint: bruk `int()` sammen med `input()`).
2. Print ut det dobbelte av tallet brukeren har oppgitt.

<details><summary>Løsning Oppgave 2.7</summary>
<p>

```python
tallstreng = input("Skriv inn et tall: ")
tall = int(tallstreng)
print(2 * tall)
```

</p>
</details>

#### Oppgave 2.8 (Vanskelig)

Du jobber i en barnehage og ungene er veldig opptatt av at ting skal være rettferdig fordelt.
Lag et program som leser inn antall barn og antall epler.
Skriv ut hvor mange epler alle barna før og hvor mange som blir til overs dersom alle barna skal få et likt antall epler.

Du kan bruke `//` istedenfor `/` for å få heltallsdivisjon.

<details><summary>Løsning Oppgave 2.8</summary>
<p>

```python
barn = int(input("Hvor mange sultne barn? "))
epler = int(input("Hvor mange saftige epler? "))
print("Hver barn får ", epler // barn, " eple")
print("Det blir ", epler % barn, " til overs")
```

</p>
</details>

---

### Lister

Det kan noen ganger være lurt å lagre data i lister for å ha bedre struktur på dataene.

Se for deg at du skal lage en oversikt over byer du har vært i.
Du lagrer byene i variabler slik at det er lett å holde oversikt. _eller..._

```python
by1 = "Oslo"
by2 = "Bergen"
by3 = "Trondheim"
by4 = "Arendal"
...
```

Dette blir fort veldig rotete når du begynner å få mange byer. Tenk deg at skal lagre 10.000 linjer med steder du har besøkt.
Løsningen på problemet er å lagre dataene i en liste.
_Legg gjerne inn byer du selv har besøkt_

```python
byer = ["Oslo", "Bergen", "Trondheim", "Arendal"]
print(byer)
```

`['Oslo', 'Bergen', 'Trondheim', 'Arendal']`

Dette gir og muligheten for enkelt å fjerne eller legge til byer i listen. Det kan gjøres ved hjelp av noen listefunksjoner som er innebygd i Python.

```python
byer.append("Grimstad")
byer.remove("Oslo")
print(byer)
```

`['Bergen', 'Trondheim', 'Arendal', 'Grimstad']`

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

`['Arendal', 'Bergen', 'Grimstad', 'Trondheim']`

_En liste med tekstelementer vil bli sortert alfabetisk, mens en liste med tall blir sortert i stigende rekkefølge. ```.sort()``` vil ikke fungere i lister som er blandet._

I tillegg er det i mange tilfeller interessant å finne ut av hva en liste inneholder på et spesielt sted (for eksempel hva det første elementet i listen er). Vi kan bruke indekser til dette. Indeksen til et element er plasseringen i listen.

```python
førsteby = byer[0]
print(førsteby)
```

`Arendal`

**NB!** _Python har null-basert indeksering, noe som betyr at det første elementet ligger på indeks [0], det andre elementet ligger på indeks [1] osv._

#### Oppgave 2.9

1. Start med en tom liste ved å bruke `talliste = []`
2. Legg til 10 forskjellige heltall mellom 0 og 100 ved bruk av `.append()`
3. Print listen du har laget
4. Finn ut hva det 6. laveste tallet i din liste er ved å sortere listen og bruke indekser

<details><summary>Løsning Oppgave 2.9</summary>
<p>

```python
talliste = [11, 2, 84, 72, 36, 90, 15, 82, 10, 55]
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

Legg merke til at linjene som kommer etter `if` og `else` har et lite innrykk. Dette er for å vise at de tilhører `if` betingelsen.

Prøv å bytte ut `by` med en by du har besøkt og en du ikke har besøkt og se hvordan resultatet endrer seg.

#### Oppgave 2.10

1. Lag en liste over 3 land du har besøkt
2. Les inn en navnet på et nytt land fra brukeren ved hjelp av `input()`
3. Skriv følgende logikk:

```plaintext
Hvis landet finnes i listen over land jeg har besøkt:
  Skriv ut teksten: "Landet ligger allerede i listen"
Dersom den ikke finnes:
  Legg til landet i listen (Hint: Bruk .append())
  Skriv ut listen over land
```

<details><summary>Løsning Oppgave 2.10</summary>
<p>

```python
land = ["Canada", "Brasil", "Italia"]
nyttland = input("Skriv inn land: ")

if nyttland in land:
  print("Landet ligger allerede i listen")
else:
  land.append(nyttland)
  print(land)
```

</p>
</details>

#### Oppgave 2.11 (Vanskelig)

Du skal skrive et program som finner ut hvor mye en reisende skal betale i billettpris ut fra alderen til vedkommende.

Ta utgangspunkt i følgende tabell:

| Alder      | Pris   |
|------------|--------|
| Under 6 år | Gratis |
| 6-12       | 25 kr  |
| 13-17      | 35 kr  |
| 18-66      | 45 kr  |
| 67 og over | 30 kr  |

Tips: Istedenfor å bruke masse [`if`](https://docs.python.org/3/tutorial/controlflow.html#if-statements) kan du bruke [`elif`](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

| == | Er lik |
| != | Ikke lik |
| < | Mindre enn |
| > | Større enn |
| <= | Mindre enn eller lik |
| >= | Større enn eller lik |

Les inn alderen til brukeren ved hjelp av `input()`

<details><summary>Løsningsforslag Oppgave 2.11</summary>
<p>

```python
alder = int(input("Hvor gammel er du? "))

if alder < 6:
  print("Du slipper å betale")
elif alder <= 12:
  print("Du må betale 25 kr")
elif alder <= 17:
  print("Du må betale 35 kr")
elif alder <= 66:
  print("Du må betale 45 kr")
else:
  print("Du må betale 30 kr")
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

Denne vil importere funksjonalitet for å bruke `pi` fra biblioteket `math`. Dette er et bibliotek for bruk av en rekke enkle matematiske funksjonaliteter. For å importere all funksjonalitet fra et bibliotek på en gang kan man bruke:

```python
from math import *
```

eller

```python
import math
```

_*NB! Hvis bibloteket blir importert på denne måten brukes navnet på biblioteket foran: `math.pi`*_

#### Oppgave 2.12

Importer funksjonaliteten `shuffle` fra biblioteket `random`. Deretter kan du bruke funksjonen `shuffle()`. Bruk denne til å stokke om listen med tall fra Oppgave 2.7

<details><summary>Løsning Oppgave 2.12</summary>
<p>

```python
from random import shuffle

talliste = [11, 2, 84, 72, 36, 90, 15, 82, 10, 55]

shuffle(talliste)
print(talliste)
```

</p>
</details>

---

### For-løkker

For-løkker brukes for å repetere handlinger uten at vi må skrive eller kopiere kodelinger mange ganger. Det gir oss muligheten til for eksempel utføre en kalkulasjon på alle tallene i en liste eller geokode alle adressene i en liste.

En for-løkke ser slik ut:

```python
liste = ["a", "b", "c", "d"]

for bokstav in liste:
  print(bokstav)
```

```plaintext
a
b
c
d
```

Dersom du skulle utført en kalkulasjon på alle elementene i en liste manuelt ville det kanskje sett sånn ut:

```python
talliste = [11, 2, 84, 72, 36, 90, 15, 82, 10, 55]
sum = 0

tall1 = tallliste[0]
tall1 = tall1 * 2
sum = sum + tall1

tall2 = tallliste[0]
tall2 = tall2 * 2
sum = sum + tall2

tall3 = tallliste[0]
tall3 = tall3 * 2
sum = sum + tall3

...

print(sum)
```

Når du endrer denne til en for-løkke vil den se sånn ut:

```python
talliste = [11, 2, 84, 72, 36, 90, 15, 82, 10, 55]
sum = 0

for tall in talliste:
  tall = tall * 2
  sum = sum + tall

print(sum)
```

#### Oppgave 2.13

Tenk gjennom og noter noen fordeler for-løkke metoden gir.

<details><summary>Løsning Oppgave 2.13</summary>
<p>

- Umulig å vite hvor mange elementer som finnes i listen.
- Tar mye plass. Lengden på koden multipliseres med antall elementer.
- Dersom kalkulasjonen skal endres (for eksempel til `* 3`) må det endres i alle kopiene

</p>
</details>

#### Oppgave 2.14 (Vanskelig)

Lag et program som skriver `100` vers av sangen _Fiskebollen lengter etter havet_.
Bruk funksjonen [`range()`](https://docs.python.org/3/library/stdtypes.html#range) for å generere en liste.

```plaintext
Fiskebollen lengter etter havet,
for havet det er fiskebollens hjem!
Dette var det 1. verset,
nå er det bare 99 igjen...
```

<details><summary>Løsning Oppgave 2.14</summary>
<p>

```python
for tall in range(1, 101):
  print("Fiskebollen lengter etter havet,")
  print("for havet det er fiskebollens hjem!")
  print("Dette var det " + str(tall) + ". verset,")
  print("nå er det bare " + str(100 - tall) + " igjen...")
```

</p>
</details>

#### Oppgave 2.15 (Vanskelig)

Lag et program som leser inn `5` tall fra brukeren, summerer de sammen og printer summen.

<details><summary>Løsning Oppgave 2.15</summary>
<p>

```python
sum = 0

for i in range(1, 6):
  tall = input("Skriv inn tall nr " + str(i) + ":")
  sum += int(tall)

print(sum)
```

</p>
</details>

---

<div style="page-break-after: always;"></div>

## Geometri

Manuelt kopier plotting funksjonene:

<details><summary> Plotting funksjoner </summary>
<p>

```python
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
```

</p>
</details>

---

### Punkter

Et punkt har en x-koordinat og en y-koordinat. Vi kan dermed se på et punkt som en liste med to elementer

```python
punkt = [ 2, 2]
```

Vi har lagd klar noen funksjoner for å enkelt plotte dataene.

```python
plot_punkt(punkt)
```

Du vil nå få opp en graf tilsvarende denne:

![Punkt]

[Punkt]: ./images/punkt.png

Det er mulig å legge inn flere punkt i samme graf. Å bruke `plot_punkt()` for hvert enkelt punkt vil resultere i en advarsel, og er veldig lite praktisk.

Vi har derfor laget en funksjon for å plotte mange punkter sammen `plot_punkter()`. Denne funksjonen tar inn en liste som input, og plotter alle punktene i listen.

Vi kan opprette en liste og legge til så mange punkter du orker.

```python
punkter = []
punkter.append([ 1,  1])
punkter.append([-1, 10])
punkter.append([ 5,  7])
punkter.append([ 3,  2])

plot_punkter(punkter)
```

_Husk at funksjonen nå heter `plot_punkter` og ikke `plot_punkt`_

![Punkter]

[Punkter]: ./images/punkter.png

Denne typen geometri er ofte kjent som MultiPoint.

#### Oppgave 3.1.1

Lag en liste med 8 punkter ved å bruke `.append()` slik at de tilsvarer hjørnene i en oktogon. Plot deretter punktene med `plot_punkter()`.

<details><summary>Løsning Oppgave 3.1.1</summary>
<p>

```python
punkter = []
punkter.append([ 1,  2])
punkter.append([ 2,  1])
punkter.append([ 1,  3])
punkter.append([ 3,  1])
punkter.append([ 4,  2])
punkter.append([ 2,  4])
punkter.append([ 3,  4])
punkter.append([ 4,  3])

plot_punkter(punkter)
```

</p>
</details>

#### Oppgave 3.1.2

Finn distansen mellom punktene

```python
Punkt1 = [ 3, 2]
Punkt2 = [ 5, 7]
```

ved hjelp av Pytagoras. _Tips: Bruk `import math` og `math.sqrt()` for å finne roten_

<details><summary>Løsning Oppgave 3.1.2</summary>
<p>

```python
import math

Punkt1 = [ 3, 2]
Punkt2 = [ 5, 7]

distanse = math.sqrt((Punkt1[0] - Punkt2[0]) ** 2 + (Punkt1[1] - Punkt2[1]) ** 2)

print(distanse)
```

`5.385164807134504`

_Fungerer også med negative verdier i punkt-koordinatene._

</p>
</details>

#### Oppgave 3.1.3 (Vanskelig)

Plot 16 punkter jevnt fordelt i en sirkel ved hjelp av en `for`-løkke.
Tips: Bruk sinus (`math.sin`) og cosinus (`math.cos`) funksjonene i `math` biblioteket.

<details><summary>Løsningsforslag Oppgave 3.1.3</summary>
<p>

```python
import math

sirkelpunkter = []
antallPunkter = 16

for x in range(0, antallPunkter):
  punkt = [math.sin(x / antallPunkter * 2 * math.pi),
           math.cos(x / antallPunkter * 2 * math.pi)]
  
  sirkelpunkter.append(punkt)
  
plot_punkter(sirkelpunkter)
```

![Sirkel]

[Sirkel]: ./images/sirkel.png

</p>
</details>

---

### Linjer

Et linjestykke kan defineres med to punkter (start og sluttpunkt). Ved å legg til flere punkter kan vi lage en linje med flere linjestykker
Bruker `plot_linje()`. Input er en liste med punkter.

```python
punkter = []
punkter.append([ 1,  1])
punkter.append([-1, 10])
punkter.append([ 5,  7])
punkter.append([ 3,  2])

plot_linje(punkter)
```

![Linje]

[Linje]: ./images/linje.PNG

#### Oppgave 3.2

1. Har rekkefølgen på punktene du legger til noe å si?
2. Kan man lage linjer som krysser seg selv?
3. Forsøk å reprodusere denne linjen. Er det flere måter å gjøre dette på?

![Linje2]

[Linje2]: ./images/linje2.PNG

<details><summary>Løsning Oppgave 3.2</summary>
<p>

1. Ja, rekkefølgen har noe å si. Det første punktet i listen vil være starten av linjen, og linjen følger deretter punktene i den rekkefølgen de ligger i.
2. Ja, vi kan lage linjer som krysser seg selv. F.eks ved å endre på rekkefølgen på linjen fra eksempelet:

```python
punkter = []
punkter.append([ 1,  1])
punkter.append([ 5,  7])
punkter.append([ 3,  2])
punkter.append([-1, 10])

plot_linje(punkter)
```

3. Trikset er å legge inn det første punktet en gang til på slutten.

```python
punkter = []
punkter.append([ 1,  1])
punkter.append([-1, 10])
punkter.append([ 5,  7])
punkter.append([ 3,  2])
punkter.append([ 1,  1])

plot_linje(punkter)
```

Siden dette er en sluttet krets, kan vi selvfølgelig starte i hvilket som helst punkt på linjen.

</p>
</details>

---

### Polygoner

En polygon består av sammenhengende linjestykker. Siden linjer kan beskrives med en liste med punkter, har også polygoner denne egenskapen.

En polygon beskrives av en liste med tre eller flere punkter. Ved bruk av `plot_polygon()`:

```python
punkter = []
punkter.append([ 1,  1])
punkter.append([-1, 10])
punkter.append([ 5,  7])
punkter.append([ 3,  2])

plot_polygon(punkter)
```

![Polygon]

[Polygon]: ./images/polygon.PNG

#### Oppgave 3.3.1

1. Lag en polygon med 4 hjørner, og plott den. 
2. Hvorfor har rekkefølgen på punktene (hjørnene) noe å si? Opprett og plott to polygoner kun ved å endre rekkefølgen på punktene.

<details><summary>Løsning Oppgave 3.3.1</summary>
<p>

1.

```python
punkter = []
punkter.append([ 1,  1])
punkter.append([-1, 10])
punkter.append([ 5,  7])
punkter.append([ 3,  2])

plot_polygon(punkter)
```

2. Siden polygoner er definert med hjørnene sine og linjene mellom disse, er de definert med omkretsen sin. Dersom linjen (omkretsen) endres ved å endre rekkefølgen på punktene vil også polygonet endre seg. Man får to polygoner dersom man bruker en linje som krysser seg selv.

```python
punkter = []
punkter.append([ 1,  1])
punkter.append([ 3,  2])
punkter.append([-1, 10])
punkter.append([ 5,  7])

plot_polygon(punkter)
```

</p>
</details>

#### Oppgave 3.3.2 (Vanskelig)

Speil de to polygonene fra forrige oppgave om x-aksen ved hjelp av en for-løkke. _Tips: Speiling om x-aksen gjøres ved å endre fortegn i y-verdiene for hvert punkt_

<details><summary>Løsning Oppgave 3.3.2</summary>
<p>

```python
punkter1 = []
punkter1.append([ 1,  1])
punkter1.append([ 3,  2])
punkter1.append([-1, 10])
punkter1.append([ 5,  7])

plot_polygon(punkter1)

punkter2 = []

for punkt in punkter1:
  punkter2.append([punkt[0],punkt[1]*-1])

plot_polygon(punkter2)
```

![Polygon3]

[Polygon3]: ./images/polygon3.PNG

</p>
</details>

---

<div style="page-break-after: always;"></div>

## Kart med OpenStreetMap

Manuelt kopier geokoding funksjonene:

<details><summary> Geokoding funksjoner </summary>
<p>

```python
import requests

brukernavn = "Geoforum"
passord = "Python3!"
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
```

</p>
</details>

---

### Dynamiske kart med Folium

For å vise kart skal vi bruke et hjelpebibliotek som heter `folium`. Dette baserer seg på `leaflet` som noen kanskje er kjent med.

For å opprette et kart med folium trenger du bare skrive følgende:

```python
import folium
m = folium.Map(location = [ breddegrad, lengdegrad ])
m
```

Tips: `m` som står alene er for å vise kartet i notebooks.

_location_ er stedet kartet skal starte i når det åpnes. Denne verdien er en punktverdi med x,y-koordinater som breddegrad og lengdegrad.

![Kart]

[Kart]: ./images/kart.png

Det er enkelt å legge til ekstra valg som for eksempel forskjellige basemaps og zoomnivåer ved hjelp av følgende valg:

```text
tiles - Valg av basemap
zoom_start - Zoomnivå
```

Mulige Basemaps:

- 'openstreetmap',
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
import folium
m = folium.Map(location = [ 58.7692591, 5.6675446 ],
               tiles = 'stamenterrain',
               zoom_start = 15)
m
```

**NB!** _Husk å importere folium før du går igang med oppgavene._

#### Oppgave 4.1

Bruk en bredde- og lengdegraden som du fant med `folium.LatLngPopup().add_to(m)` til å opprette et nytt kart og vis det i notebooken. Sett eget zoomnivå og velg et basemap som du liker.

Bonus: Lag egen basemap-velger ved å legge til flere basemaps med `folium.TileLayer(SETT INN BASEMAP HER).add_to(m)` og `folium.LayerControl().add_to(m)`

<details><summary>Løsning Oppgave 4.1</summary>
<p>

```python
import folium

m = folium.Map(location=[59.9103, 10.7634],
    tiles='stamenterrain',
    zoom_start=16
)

folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('MapBox Bright').add_to(m)
folium.TileLayer('MapBox Control Room').add_to(m)
folium.TileLayer('stamentoner').add_to(m)
folium.TileLayer('stamenwatercolor').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.LayerControl().add_to(m)

m
```

</p>
</details>

---

### Geokoding

Geokoding er en viktig del av GIS-hverdagen som går ut på å knytte sammen adresser/steder og koordinater. Fordelen med Python og koding er at du kan automatisere geokoding av store datasett.

Vi har jukset litt og forhåndlaget en liten funksjon `geokoding()` som tar seg av arbeidet. Denne geokodingen vil kun fungere for steder i Norge.

```python
breddegrad, lengdegrad = geokoding("Schweigaardsgate 28, Oslo")
print((breddegrad, lengdegrad))
```

```text
(59.91029353312019, 10.763368458155954)
```

I tillegg til adresser fungerer det også å søke på stedsnavn og lignende. Geokoding-funksjonen returnerer det første resulatet det finner, så det finnes tilfeller hvor den kan finne et sted du ikke forsøkte å finne hvis søketeksten er for generell.

Vi kan også bruke en liste med adresser og ved hjelp av for-løkker geokode disse:

```python
adresser = ["Schweigaardsgate 28, Oslo", "Gabels Gate 21, Oslo", "Austhallet 17, Klepp Stasjon"]

koordinater = []

for adresse in adresser:
    koordinater.append(geokoding(adresse))

print(koordinater)
```

```text
[(59.91029353312019, 10.763368458155954),
(59.914308706660485, 10.710155016908361),
(58.76925371377823, 5.66974950236923)]
```

På denne måten kan vi enkelt plotte punktene i et kart ved en senere anledning.

#### Oppgave 4.2.1

Finn koordinatene til en adresse i Norge ved å bruke geokoding. Opprett deretter et kart med koordinatene som ble funnet. Verifiser at det var adressen du lette etter ved å se i kartet.

<details><summary>Løsning Oppgave 4.2.1</summary>
<p>

```python
import folium

breddegrad, lengdegrad = geokoding("<SETT INN DIN ADRESSE>")

m = folium.Map(location=[breddegrad, lengdegrad],
    tiles='openstreetmap',
    zoom_start=15
)

m
```

_Husk a tilpasse zoomnivået ditt basert på hva du søkte på_

</p>
</details>

#### Oppgave 4.2.2

Bruk en _**input()**_ funksjon slik at man kan skrive inn et sted eller en adresse. Bruk geokoderen med det som du har oppgitt i input. Opprett deretter et kart med koordinatene fra geokoderen.

<details><summary>Løsning Oppgave 4.2.2</summary>
<p>

```python
import folium

valgtsted = input("Gå til: ")

koordinater = geokoding(valgtsted)

m = folium.Map(location=koordinater,
    tiles='openstreetmap',
    zoom_start=12
)

m
```

</p>
</details>

---

### Markers og Shapes

Det er enkelt å legge til egendefinerte markers med masse forskjellige valg.
Dette gjøres ved hjelp av `folium.Marker()`.

- popup (Her kan man bruke HTML tags)
- tooltip
- icon
  - Folium bruker Glyphicons (<https://getbootstrap.com/docs/3.3/components/>) som default. Kan bruke f.eks Font Awesome (<https://fontawesome.com/icons>) med _**prefix='fa'**_
  - Du kan sette egendefinert farge ved hjhelp av `color`

For å faktisk legge markeren til i kartet bruker du følgende funksjon: `.add_to(m)`

Eksempel:

```python
import folium
m = folium.Map(location=[59.9103, 10.7634],
    tiles='openstreetmap',
    zoom_start=15
)
folium.Marker(
    [59.9103, 10.7634],
    popup='Geodata AS',
    tooltip='Dette er en Tooltip',
    icon=folium.Icon(color='red',icon='cloud'),
).add_to(m)

m
```

![MarkerIcon]

[MarkerIcon]: ./images/icon.png

Ikoner for markers på kartet kan man også gjøre mye selv på egenhånd. Blant annet kan man endre farge og symbolet. _**prefix**_ definerer hvor symbolet kommer fra, _**fa**_ brukes for **Font Awesome**.

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
    fill_color='crimson',
).add_to(m)
```

![SirkelMarker]

[SirkelMarker]: ./images/sirkelmarker.png

#### Oppgave 4.3.1

- Lag liste over noen byer i Norge du har besøkt.
  - Bruk geokoder for å finne koordinater.
  - Legg disse i ny liste.
- Lag et kart med markers for alle byene.

Bonus: Lag tooltip og popup med navnet på byen.

<details><summary>Løsning Oppgave 4.3.1</summary>
<p>

```python
import folium

m = folium.Map(location = [ 62, 6 ],
              zoom_start = 4)

byer = ["Oslo","Bergen","Trondheim","Stavanger"]
koordinater = []

for by in byer:
    koordinater.append(geokoding(by))

folium.Marker(
    koordinater[0],
    popup = 'Oslo',
    tooltip = 'Oslo',
    icon = folium.Icon(color='red',icon='map-marker'),
).add_to(m)
folium.Marker(
    koordinater[1],
    popup = 'Bergen',
    tooltip = 'Bergen',
    icon = folium.Icon(color='red',icon='map-marker'),
).add_to(m)
folium.Marker(
    koordinater[2],
    popup = 'Trondheim',
    tooltip = 'Trondheim',
    icon = folium.Icon(color='red',icon='map-marker'),
).add_to(m)
folium.Marker(
    koordinater[3],
    popup = 'Stavanger',
    tooltip = 'Stavanger',
    icon = folium.Icon(color='red',icon='map-marker'),
).add_to(m)

m
```

eller enda litt smartere

```python
import folium

m = folium.Map(location = [ 62, 6 ],
              zoom_start = 5)

byer = ["Oslo","Bergen","Trondheim","Stavanger"]

for by in byer:
    folium.Marker(
        geokoding(by),
        popup = by,
        tooltip = by,
        icon = folium.Icon(color='red',icon='map-marker'),
    ).add_to(m)

m
```

</p>
</details>

#### Oppgave 4.3.2

Besvar spørsmålene under ved prøving og feiling:

1. Hva skjer dersom du legger en Marker og en Circle i samme punkt? Har rekkefølgen de legges til noe å si?
2. Hva skjer dersom to sirkler overlapper?
3. Hva er forskjellen mellom `color` og `fill_color` i Circle? Er det mulig å  bruke noe annet enn tekststrenger som `'red'` eller `'green'` til å definere farge?
4. Hva har gått galt her?

![Save]

[Save]: ./images/Save.PNG

<details><summary>Løsning Oppgave 4.3.2</summary>
<p>

1. Det går helt fint å legge begge deler i samme punkt. Begge vil vises. Rekkefølgen som de legges til i har ikke noe å si (Markers alltid øverst).
2. To sirkler kan fint overlappe. Dersom begge har `fill=True` ser dette f.eks slikt ut: 
    
![ToSirkler]

[ToSirkler]: ./images/ToSirkler.PNG

3. `color` definerer kanten av sirkelen, `fill_color` alt som er inne i sirkelen. De to fargeverdiene kan godt være forskjellige fra hverandre. Default dersom du ikke setter noe farge er blå. Man kan sette hvilken som helst farge med HEX (f.eks `color='#c831e2'`) eller RGB (f.eks `color='rgb(200, 49, 226)'`).

4. Jorden er rundt, og det er ikke så enkelt å tegne korrekte sirkler i en 2D Projeksjon. Vær forsiktig med veldig store sirkler, spesielt i Polarregionene.

</p>
</details>

---

#### Oppgave 4.3.3 (Vanskelig)

Ta utgangspunkt i listen din over noen byer du har besøkt i Norge. Opprett også en ny (foreløbig) tom liste. Du skal så kunne skrive inn ny by (bruk _**input()**_). Skriv logikk med betingelser for

```plaintext
Hvis byen som ble skrevet inn er i bylisten:
  Lag en grønn sirkel med radius 10km rundt byen
Hvis byen ligger i den ny listen:
  Lag en rød sirkel med radius 20km rundt byen
Hvis byen ikke ligger i bylisten, og ikke i den nye listen:
  Legg til byen i den nye listen
  Lag en rød sirkel med radius 10km rundt byen
```

_Husk å bruke geokoder for å finne koordinatene når du trenger disse_

Legg input-funksjonen og hele logikken inn i en for-løkke slik at det hele kjøres ti ganger.

Vis deretter kartet.

<details><summary>Løsning Oppgave 4.3.3</summary>
<p>

```python
import folium

byliste = ["Oslo","Bergen","Trondheim","Stavanger"]
nyliste = []
m = folium.Map(location=[62, 10],
    tiles='openstreetmap',
    zoom_start=5
)
for i in range(0,10):  
  valgtsted = input("Gå til: ")
  if (valgtsted in byliste):
    folium.Circle(
      radius=10000,
      location=geokoding(valgtsted),
      popup=valgtsted,
      color='green',
      fill=True,
      fill_color='green',
    ).add_to(m)
  elif (valgtsted in nyliste):
    folium.Circle(
      radius=20000,
      location=geokoding(valgtsted),
      popup=valgtsted,
      color='red',
      fill=True,
      fill_color='red',
    ).add_to(m)
  else:
    nyliste.append(valgtsted)
    folium.Circle(
      radius=10000,
      location=geokoding(valgtsted),
      popup=valgtsted,
      color='red',
      fill=True,
      fill_color='red',
    ).add_to(m)

m
```

</p>
</details>

---

_**EKSTRA HVIS TID**_

1. Lag din egen dynamiske kartapplikasjon ved hjelp av Notebooks og Folium.

2. Vise GeoJSON med Folium. Kan enten hente GeoJSON fra fil eller bruke direkte som tekststreng. En GeoJSON kan også komme fra en url.

_NB! I GeoJSON brukes koordinater i omvendt rekkefølge (altså [lengdegrad, breddegrad])_

Eksempel:

```python
import folium
m = folium.Map(location = [ 60.4, 5.3 ])
folium.GeoJson("""{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [ 5.3, 60.4 ]
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [ 5.2, 60.4 ], [ 5.2, 60.3 ], [ 5.1, 60.4 ], [ 5.1, 60.3 ]
        ]
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [ 5.2, 60.2 ], [ 5.1, 60.15 ], [ 5.0, 60.2 ], [ 5.0, 60.3 ]
          ]
        ]
      }
    }
  ]
}""").add_to(m)
m
```

3. Plotting av linjer i Folium:
<https://deparkes.co.uk/2016/06/03/plot-lines-in-folium/>

4. Kahoot (felles)

---

<div style="page-break-after: always;"></div>

## Sette opp Jupyter Notebooks lokalt

<https://jupyter.readthedocs.io/en/latest/install.html>
