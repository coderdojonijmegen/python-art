from turtle import *
import random

speed(0)
penup()
colors = ["red", "cyan", "green", "yellow", "purple", "orange", "blue"]


def vorm(x, y, rib, hoeken, rotatie=0):
    goto(x, y)
    right(rotatie)
    pendown()
    for _ in range(hoeken):
        forward(rib)
        right(180 - ((hoeken - 2) * 180 / hoeken))
    penup()
    right(-rotatie)


for i in range(int(360 / 15)):
    vorm(0, 0, 10, 40, 15 * i)

for _ in range(100):
    fillcolor(colors[random.randint(0, len(colors) - 1)])
    begin_fill()
    vorm(random.randint(-200, 200), random.randint(-200, 200), random.randint(10, 100), 4)
    end_fill()

done()
