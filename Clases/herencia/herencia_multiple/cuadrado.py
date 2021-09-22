from figura_geomrtrica import FiguraGeometrica
from color_figura import ColorFigura

class Cuadrado(FiguraGeometrica, ColorFigura):
    def __init__(self, lado, color):
        # Inicializacion de la clases 
        # Para inicializar los valores de la clase padre
        #no se requiere el mismo nombre de la variable
        FiguraGeometrica.__init__(self, lado, lado)
        ColorFigura.__init__(self, color)

    def __str__(self):
        return f' {FiguraGeometrica.__str__(self)}, {ColorFigura.__str__(self)} '
    def calcular_area(self):
        return self._alto * self._ancho
