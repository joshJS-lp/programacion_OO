class Persona:
    #inicializar atributos
    # el fonle (_init__) es dunder 
# sirve para declarar atributos de clase  o instancia
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        #atributos de instancia o de objeto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    #methods
    def mostrar_detalle(self):
        print(f'Nombre: {self.nombre}, Apellido: {self.apellido}, edad: {self.edad}, tupla: {self.args}, dic: {self.kwargs}')


persona1 = Persona('Carol', 'Rosas', 24, 2,2,3,5,6, m='molesto', e='enojado')
persona1.mostrar_detalle()
#print(persona1.nombre)

person2 = Persona('josh', 'lopez', 25)

#modificar valors de un objeto
#person2.nombre = 'benito'

#print(person2.nombre)
person2.mostrar_detalle()
# Agregar un atributi
#person2.telefono = 12548793
#print(person2.telefono)
# Se puede acceder al metodo desde la intacia 
# de la clase 
# Persona.mostrar_detalle(persona1)