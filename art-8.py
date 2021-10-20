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
    vorm(0, 0, 150, 9, 15 * i)

# for j in range(400, -400, -50):
#     for i in range(-425, 425, 50):
#         fillcolor(colors[random.randint(0, len(colors) - 1)])
#         begin_fill()
#         # vorm(random.randint(-200, 200), random.randint(-200, 200), random.randint(10, 100), 5, random.randint(0, 90))
#         vorm(i, j, 45, 6)
#         end_fill()

done()
