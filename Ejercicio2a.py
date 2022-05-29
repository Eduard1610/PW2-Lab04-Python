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

caballoN = knight.negative()
caballosHorizontal1 = knight.join(caballoN)
caballosHorizontal2 = caballoN.join(knight)
figura = caballosHorizontal1.up(caballosHorizontal2)
draw(figura)

