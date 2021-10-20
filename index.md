---
title: "Python - Art"
date: 2021-10-18T21:07:47+02:00
draft: false
toc: true
headercolor: "teal-background"
taal: Python
---

We gaan kunst maken met Python Turtle.

<!--more-->

## Introductie

We gebruiken voor deze instructies Thonny, een eenvoudige editor voor Python scripts.  
Je kunt deze [hier](https://thonny.org/) downloaden en vervolgens installeren.

Mocht je nog geen ervaring hebben met Thonny en Turtle, kijk dan ook eens naar onze 
[Python Turtle](/instructies/python-turtle/) instructies.

Je kunt ook kunst maken met Scratch. Kijk daarvoor naar de [Scratch Art](/instructies/scratch-art/) instructies.

In deze instructie behandelen we kunst met lijnen, cirkels, polygonen (zoals een driehoek en vierkant) en een lissajous.

## Lijnen

### Een lijn

We beginnen eenvoudig met het tekenen van een enkele lijn:

{{< highlight python "linenos=table,linenostart=1" >}}
from turtle import *

forward(100)

done()
{{< /highlight >}}

Op regel 1 wordt Turtle geladen. Deze regel is nodig om de Turtle commando's te kunnen gebruiken.  
Op de 3e regel wordt met Turtle commando `forward` een lijn getrokken met lengte 100.  
Tenslotte zorgt `done` op regel 5 er voor dat het scherm waarop getekend is, open blijft.

### Een driehoek
![driehoek](imgs/driehoek.png)

Met drie lijnen kun je een driehoek tekenen. Dit kan er als volgt uit zien:

{{< highlight python "linenos=table,hl_lines=3-8,linenostart=1" >}}
from turtle import *

forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)

done()
{{< /highlight >}}

Het commando `right` op regels 4, 6 en 8 zorgt ervoor dat de pen naar rechts draait en wel met 120 graden.

**Opdracht 1**: Voeg regels 3 tot en met 8 eens stap voor stap toe en zie wat elke stap doet.

#### Herhalingen

In het vorige voorbeeld zag je 3 keer een herhaling van een `forward` en `right` command. Dit kun je ook met een
herhaling beschrijven in Python:

{{< highlight python "linenos=table,hl_lines=3-5,linenostart=1" >}}
from turtle import *

for i in range(3):
    forward(100)
    right(120)

done()
{{< /highlight >}}

Op regel 3 zorgt command `for i in range(3)` ervoor dat regels 4 en 5 driemaal herhaald worden.

**Opdracht 2**: Verander de range (het getal 3) eens naar 1, 2, 3 of 4? Wat gebeurd er?  
**Opdracht 3**: Maak de hoek (het getal 120) eens groter of kleiner en kijk wat er gebeurd.

## Cirkels

Naast rechte lijnen, kun je met Turtle ook cirkels tekenen. Daarvoor is het commando `circle`:

{{< highlight python "linenos=table,hl_lines=3,linenostart=1" >}}
from turtle import *

circle(100)

done()
{{< /highlight >}}

Het getal 100 op lijn 3 staat voor de diameter van de cirkel. 

**Opdracht 4**: Maak de cirkel eens groter.


## Polygonen

## Lissajous


## Voorbeelden

Ter voorbereiding van deze instructie hebben we zelf ook wat kunst gemaakt. Probeer ze eens uit:
 * [art-1.py](art-1.py) gekleurde lijnen  
    ![art-1](imgs/art-1.png)
 * [art-2.py](art-2.py) gekleurde lijnen  
   ![art-2](imgs/art-2.png)
 * [art-3.py](art-3.py) gekleurde lijnen  
   ![art-3](imgs/art-3.png)
 * [art-4.py](art-4.py) gekleurde cirkels  
   ![art-4](imgs/art-4.png)
 * [art-5.py](art-5.py) gekleurde veelhoeken  
   ![art-5](imgs/art-5.png)
 * [art-6.py](art-6.py) gekleurde en gedraaide vierkanten  
   ![art-6](imgs/art-6.png)
 * [art-7.py](art-7.py) lissajous  
   ![art-7](imgs/art-7.png)
 * [art-8.py](art-8.py) willekeurige gekleurde vijf- en zevenhoeken  
   ![art-8](imgs/art-8.png)
 * [art-9.py](art-9.py) willekeurig gekleurde gedraaide negenhoeken  
   ![art-9](imgs/art-9.png)

{{< licentie rel="http://creativecommons.org/licenses/by-nc-sa/4.0/">}}