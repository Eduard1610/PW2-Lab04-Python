from interpreter import draw 
from chessPictures import *

tableroA = [] #En este tablero se almacenaran cada objeto Picture con el color de fondo correspondiente
casilla = square; 
mod= 'even'; #Para pintar de color oscuro los que son modulo 0
arreglo = [rock, knight,bishop, queen , king , bishop , knight, rock]
#Lleno el tablero con las figuras iniciales
i = 0;
while i < len(arreglo):
    if(mod == 'even'): #Para alterar el color de fondo
        if(i % 2 == 0):
            casilla = casilla.negative()
        else:
            casilla = square
    if(mod == 'odd'):  #Para alterar el color de fondo
        if(i % 2 == 0):
            casilla = square
        else:
            casilla = casilla.negative()

    pieza = casilla.__eq__(arreglo[i])
    tableroA.append(pieza)
    i += 1

i = 1;#Lo reseteo
#Con el tablero ya llenado realizo el dibujo uniendo cada objeto Picture
dibujoA = tableroA[0]
while i < len(tableroA):
    dibujoA = dibujoA.join(tableroA[i])
    i += 1

#Mismo procediiento de arriba pero esta vez se pintaran de color clar
tableroB = []
casilla = square;
mod= 'odd'
arregloB = [pawn , pawn , pawn , pawn , pawn , pawn , pawn ,pawn]
#Lleno el tablero con las figuras iniciales
i = 0;
while i < len(arregloB):
    if(mod == 'even'): #Para alterar el color de fondo
        if(i % 2 == 0):
            casilla = casilla.negative()
        else:
            casilla = square
    if(mod == 'odd'):  #Para alterar el color de fondo
        if(i % 2 == 0):
            casilla = square
        else:
            casilla = casilla.negative()

    pieza = casilla.__eq__(arregloB[i])
    tableroB.append(pieza)
    i += 1

i = 1;#Lo reseteo
#Con el tablero ya llenado realizo el dibujo
dibujoB = tableroB[0]
while i < len(tableroB):
    dibujoB = dibujoB.join(tableroB[i])
    i += 1


draw(dibujoA.under(dibujoB))
