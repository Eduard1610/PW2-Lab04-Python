from interpreter import draw
from chessPictures import *
cuadradoNegativo = square.negative()
parCuadrados = cuadradoNegativo.join(square)
draw(parCuadrados.horizontalRepeat(4))
