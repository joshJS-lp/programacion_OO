class Persona_encapsular:
    #inicializar atributos
    # el fonle (_init__) es dunder 
# sirve para declarar atributos de clase  o instancia
    def __init__(self, nombre, apellido, edad):
        #atributos de instancia o de objeto
        #para encapsular una varible se pone un guion bajo
        #self._nombre  y si se queire ser mas estricto
        # se coloca doble guion bajo self.__nombre 
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    # get obtener/ recuperar
    @property #sirve para llamar la propiedad sinnecedidad de parentecis
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def edad(self):
        return self._edad
    # set colocar/modificar
    @nombre.setter
    def nombre(self, nombre):
        self._nombre =  nombre 
    @apellido.setter
    def apellido(self, apellido):
        self._apellido =  apellido 
    @edad.setter
    def edad(self, edad):
        self._edad =  edad 


    #methods
    def mostrar_detalle(self):
        print(f'Nombre: {self._nombre}, Apellido: {self._apellido}, edad: {self._edad}')
    # get obtener/ recuperar

    # set colocar/modificar


persona1 = Persona_encapsular('Carol', 'Rosas', 24)
persona1.mostrar_detalle()

print(persona1.nombre)
persona1.nombre = 'yesenia'
persona1.apellido = 'de lopez'
persona1.edad = 25
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
