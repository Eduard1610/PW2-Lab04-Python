from interpreter import draw
from chessPictures import *

casillaN = square.negative()
# Uniendo casilla negativa a una casilla blanca(normal)
casillaBN = square.join(casillaN)
#repeticion de n veces horizontalmente
draw(casillaBN.horizontalRepeat(4))

