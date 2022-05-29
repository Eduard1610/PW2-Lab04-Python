from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    imgInv = [] # Será la figura devuleta 
    contador = len(self.img) - 1
    while contador >= 0:
      imgInv.append(self.img[contador])
      contador -= 1
    return Picture(imgInv)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    imgInv = []
    listaActual_Pieza = self.img
    contador = 0
    while contador < len(listaActual_Pieza):
      lineaInvertida = ''
      indice = len(listaActual_Pieza[contador]) - 1
      while indice >= 0:
        lineaInvertida += listaActual_Pieza[contador][indice] # Caracter
        indice -= 1
      imgInv.append(lineaInvertida)
      contador += 1
    return Picture(imgInv)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    imgNeg = []
    listaPieza = self.img # La pieza se muestra como un conjunto de strings
    indice = 0
    while indice < len(listaPieza): # El índice representa cada línea de nuestra lista 
      lineaNegativa = ''
      # Se usa un for para rellenar lineaNegativa caracter por caracter
      for caracter in range(0,len(listaPieza[indice])): # Len(arregloPieza[indice]) representa la longitud de una linea
        caracterNegativo = self._invColor(listaPieza[indice][caracter]) # Se llama a la función invColor para cada caracter de una determinada linea
        lineaNegativa += caracterNegativo # Esta es la linea negativa de un índice determinado 
      imgNeg.append(lineaNegativa) # Agregamos línea a línea para nuestra lista de negativos
      indice += 1
    return Picture(imgNeg)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    piezaActual = self.img
    piezaSubyacente = p.img
    indice = 0
    piezasUnidas = []
    while indice < len(piezaActual):
      linea = piezaActual[indice]+piezaSubyacente[indice] # Creamos una línea de un determinado índice que sea la fusión de piezas
      piezasUnidas.append(linea)
      indice += 1 
    return Picture(piezasUnidas)

  def up(self, p):
    """Devuelve una nueva figura poniendo la figura p debajo de la figura actual """
    piezaActual = self.img
    piezaAbajo = p.img
    indice1 = 0
    indice2 = 0
    """Indice 1 para la pieza actual y Indice 2 para la pieza a agregar"""
    conjuntoDePiezas = []
    while indice1 < len(piezaActual):
      linea = piezaActual[indice1]
      conjuntoDePiezas.append(linea)
      indice1 += 1 
    while indice2 < len(piezaAbajo):
      linea2 = piezaAbajo[indice2]
      conjuntoDePiezas.append(linea2)
      indice2 += 1 
    return Picture(conjuntoDePiezas)
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    piezaActual = self.img
    piezaArriba = p.img
    indice1 = 0
    indice2 = 0
    """Indice 1 para la pieza actual y Indice 2 para la pieza a agregar"""
    conjuntoDePiezas = []
    """Para esto debemos empezar creando la lista con la 2da pieza"""
    while indice2 < len(piezaArriba):
      linea2 = piezaArriba[indice2]
      conjuntoDePiezas.append(linea2)
      indice2 += 1 
    while indice1 < len(piezaActual):
      linea = piezaActual[indice1]
      conjuntoDePiezas.append(linea)
      indice1 += 1 

    return Picture(conjuntoDePiezas)
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    piezaActual = self.img
    indice1 = 0
    """ Indice para la pieza actual"""
    conjuntoDePiezas = []
    for indice1 in range(0,len(piezaActual)):
      linea = ''
      count = 0
      while count < n:
        linea += piezaActual[indice1]
        count += 1
      conjuntoDePiezas.append(linea)
    return Picture(conjuntoDePiezas)    

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual por encima la
        cantidad de veces que el valor de n indique"""
    piezaActual = self.img
    indice1 = 0
    contador = 0
    """ Indice para la figura actual"""
    conjuntoDePiezas = []

    return Picture(conjuntoDePiezas)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

