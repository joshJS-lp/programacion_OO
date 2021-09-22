
class Area():
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

base = int(input('Inserta la base: '))
altura = int(input('Ingresa la altura: '))
rectangulo_area = Area(base,altura)
print(rectangulo_area.calcular_area())