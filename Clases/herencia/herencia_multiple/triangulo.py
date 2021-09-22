from figura_geomrtrica import FiguraGeometrica
from color_figura import ColorFigura

class Triangulo(FiguraGeometrica, ColorFigura):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        ColorFigura.__init__(self, color)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {ColorFigura.__str__(self)}'

    def calcular_area(self):
        return self.ancho * self.alto / 2