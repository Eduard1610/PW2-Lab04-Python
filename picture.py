from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    piezaNueva = [];
    casilla = self.img
    piezaPintar = other.img
    indice = 0
    while indice < len(casilla):#Itero cada elemetno de la casilla
      longitud = len(piezaPintar[indice])#Longitud del elemento i del array de figura
      iterador = 0
      temporal = '';
      #Compara cada elemento del string y lo va pintando
      while iterador < longitud: 
        if( piezaPintar[indice][iterador]!= '_' and  piezaPintar[indice][iterador] != " "):
          temporal += piezaPintar[indice][iterador]
          #print(piezaPintar[indice][iterador])
        else:
          temporal += casilla[indice][iterador];
        iterador += 1
      piezaNueva.append(temporal)#Se agrega el string combinado con los caracteres de las dos figuras
      indice += 1
    return Picture(piezaNueva)

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    #Arreglo donde almacenare la figura invertida
    imgInv = [];
    #Longitud del tamaño del arreglo de la figura
    longitud = len(self.img)-1; 
    #Invierto el arreglo
    while longitud >= 0:
      imgInv.append(self.img[longitud])
      #print(self.img[longitud])
      longitud -= 1;

    #Se retorna el arreglo ya convertido
    return Picture(imgInv); 


  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    imgInv = [];
    
    imagenActual = self.img;
    for x in imagenActual:
      longitud = len(x)-1; #Longitud del elemento actual
      temporal = [];
      while longitud >= 0:
        temporal.append(x[longitud])
        longitud -= 1
      temporal = "".join(temporal);#Convierte el array a string
      imgInv.append(temporal);#Se agrega al nuevo arreglo que se retornará
    return Picture(imgInv);


  def negative(self):
    """ Devuelve un negativo de la imagen """
    imgN = [];
    imagenActual = self.img;
    for x in imagenActual: #Itera cada elemtno del array
      temporal = "";
      for y in x:
        temporal += self._invColor(y);
      imgN.append(temporal)
    return Picture(imgN);

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    figurasUnidas = [];
    imagenActual = self.img;
    longitud = len(self.img)-1;
    temporal = "";
    i = 0; #Iterador
    
    while i <= longitud:#Cada figura tiene 58 elementos 
      temporal = imagenActual[i] +p.img[i] #Se unen los dos arays
      figurasUnidas.append(temporal);
      i += 1;
    return Picture(figurasUnidas);

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
    resultado = Picture(self.img);
    i = 1; #Empieza desde 1 porque ya se le asigna una imagen en la linea de arriba
    while i < n:
      resultado = resultado.join(self)# Picture
      i+= 1;
    return resultado

  def verticalRepeat(self, n):
    resultado = Picture(self.img);
    i = 1; #Empieza desde 1 porque ya se le asigna una imagen en la linea de arriba
    while i < n:
      resultado = resultado.up(self)# Picture
      i+= 1;
    return resultado


  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)