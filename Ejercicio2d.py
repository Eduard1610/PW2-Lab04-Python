from interpreter import draw
from chessPictures import *

casillaN = square.negative()
#uniendo casilla pareja(N) al (B)
casillaBN = square.join(casillaN)
#repeticion de n veces horizontalmente
draw(casillaBN.horizontalRepeat(4))
