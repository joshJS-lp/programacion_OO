class Aritmetica:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b
    
    def restar(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b

    def divcion(self):
        return self.a / self.b
#instacia
opercaion1 = Aritmetica(5,8)
# uso de metodos
print(opercaion1.suma())
print(opercaion1.restar())
print(opercaion1.mul())
print(opercaion1.divcion())