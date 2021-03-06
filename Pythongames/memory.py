"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from random import *
from turtle import *
from typing import Counter
from freegames import path
from string import hexdigits, punctuation
import string # Necessary library since the numbers were changed to letters

car = path('car.gif')
#tiles = list(range(32)) * 2  --> change to "Use letters instead of tiles"
tiles = list(string.ascii_lowercase)*2 #swap tiles by letters
state = {'mark': 0}
hide = [True] * 32

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    # notify when a new pair is found 
    points = 0
    if mark == None:  
        newPoints = points + 1  
        print(newPoints, " nueva pareja encontrada")

def draw():
    "Draw image and tiles."
    clear()
    goto(0, -200)
    shape(car)
    stamp()
    

    for count in range(32):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    
    if mark <9:
        if mark is not None and hide[mark]:
            x, y = xy(mark)
            up()
            goto(x + 18, y + 5)#numeros sencillos
            color('black')
            write(tiles[mark], font=('Arial', 30, 'normal'))
    else:
        if mark is not None and hide[mark]:
            x, y = xy(mark)
            up()
            goto(x + 12, y + 11)#numeros dobles
            color('black')
            write(tiles[mark], font=('Arial', 30, 'normal'))
    


    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(430, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
"""
flip = 0

def count(flip):
    cardsLeft = 64
    cardsLeft >0:
        flip += 1
        onscreenclick(tap)
    #print("El juego termino con: ", {flip}, "intentos.")
"""

draw()
done()
