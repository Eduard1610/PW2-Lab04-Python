from interpreter import draw
from chessPictures import *

#draw(rock)
#draw(rock.verticalMirror())
#draw(knight)
#draw(knight.horizontalMirror())
#draw(knight.negative())
#draw(knight.join(queen))
#draw(knight.up(rock))
#draw(knight.under(king))
#draw(knight.horizontalRepeat(3))
#draw(knight.verticalRepeat(3))

caballoN = knight.negative() # Caballo cambia a su color inverso (Negativo)
caballosHorizontal1 = knight.join(caballoN) # Al caballo normal le agregamos uno negativo al lado
caballosHorizontal2 = caballoN.join(knight) # Al caballo negativo le agregamos un caballo normal al lado
figura = caballosHorizontal1.up(caballosHorizontal2) # Juntamos lo anterior
draw(figura)
