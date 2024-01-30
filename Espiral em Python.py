from turtle import *

# Define a velocidade da tartaruga
speed(15)
# Define a cor da linha
color('white')
# Define a cor de fundo
bgcolor('gray')
# Desenha a espiral
contador = 0

while contador < 3:
    contador += 1

    b = 200
    c = 200
    d = 200

    while b > 0:
        left(b)
        forward(b * 1)
        b -= 1

    while c > 0:
        left(c)
        forward(c * 2)
        c -= 1

    while d > 0:
        left(d)
        forward(d * 3)
        d -= 1


