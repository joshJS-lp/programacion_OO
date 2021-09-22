class Persona:
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

    #destructuring
    def __del__(self):
        print(f'Eliminacion de {self._nombre}')

if __name__ == '__main__':
    print('modulo principal')
# Porpiedades de una clase 
#print(__name__)