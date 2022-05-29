from interpreter import draw
from chessPictures import *

caballoN = knight.negative()
caballosHorizontal1 = knight.join(caballoN)
#aqui se invierte a los caballos de la fila 1 con horizontalMirror
caballosHorizontal2Invertido = caballosHorizontal1.horizontalMirror()
figura = caballosHorizontal1.up(caballosHorizontal2Invertido)
draw(figura)
