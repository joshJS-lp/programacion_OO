class Cubo():
    def __init__(self, l, a, aa):
        self.l = l
        self.a = a
        self.aa = aa
    def calcular_cubo(self):
        return self.l * self.a * self.aa

l = int(input('Inserta la lado: '))
a = int(input('Ingresa la altura: '))
aa = int(input('Ingresa la ancho: '))

fig1 = Cubo(l, a, aa)
print('El volumen del cubo es de: ', fig1.calcular_cubo())