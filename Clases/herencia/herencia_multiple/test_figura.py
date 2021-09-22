from cuadrado import Cuadrado
from triangulo import Triangulo

print('Objeto cuadrado'.center(50, '-'))
cuadrado00 = Cuadrado(4,'negro')
print(cuadrado00.alto)
print(cuadrado00.ancho)
print(cuadrado00.color)
print(cuadrado00.calcular_area())
print(cuadrado00)
#indica el orden de los metodos
# MRO Method Resolution Order
#print(Cuadrado.mro())

print('Objeto Triangulo'.center(50, '-'))
tria00 = Triangulo(15, 5, 'gris')
print(f'Area: {tria00.calcular_area()}')
print(tria00)