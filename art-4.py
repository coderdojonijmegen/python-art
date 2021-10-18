from turtle import *

colors = ["red", "cyan", "green", "yellow", "purple", "orange", "blue"]
bgcolor("black")

speed(0)
colormode(255)

for i in range(30):
    for j in range(30):
        circle(j)
        pencolor(colors[i % len(colors)])
        # pencolor((int(j * 256/40), (i + 40) % 256, (i + 80) % 256))
        left(j)
        forward(i % 10 + 10)

done()
