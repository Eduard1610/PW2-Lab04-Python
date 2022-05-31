from interpreter import draw 
from chessPictures import *

#Se generan  dos lineas en "blanco"
filasCasillo1 = square.negative().join(square)
filasCasillo1 = filasCasillo1.horizontalRepeat(4);
filasCasilla2 = filasCasillo1.negative()
filasCompletasB = filasCasillo1.under(filasCasilla2);

draw(filasCompletasB.under(filasCompletasB))