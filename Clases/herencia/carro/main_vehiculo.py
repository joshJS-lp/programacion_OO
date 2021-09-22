class Vehiculo():
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f'{self._color}, {self._ruedas}'

    @property
    def color(self):
        return self._color

    @property
    def ruedas(self):
        return self._ruedas

    @color.setter
    def color(self, color):
        self._color = color

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        # Herencia de la clase padre
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    def __str__(self):
        return f'{super().__str__()}, {self._velocidad}'
    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo
    def __str__(self):
        return f'{super().__str__()}, {self._tipo}'    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

vehiculo = Vehiculo('red',4)
print(vehiculo)

coche = Coche('blue', 4, 120)
print(coche)

bici = Bicicleta('purple', 2, 'urbana')
print(bici)