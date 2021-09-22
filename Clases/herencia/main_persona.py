class Persona:
    #inicializar atributos
    # el fonle (_init__) es dunder 
# sirve para declarar atributos de clase  o instancia
    def __init__(self, nombre,  edad):
        #atributos de instancia o de objeto
        #para encapsular una varible se pone un guion bajo
        #self._nombre  y si se queire ser mas estricto
        # se coloca doble guion bajo self.__nombre 
        self._nombre = nombre
        self._edad = edad

    # Sobrescribir el metodo str
    def __str__(self):
        return f'{self._nombre}, {self._edad}'

    # get obtener/ recuperar
    @property #sirve para llamar la propiedad sinnecedidad de parentecis
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    # set colocar/modificar
    @nombre.setter
    def nombre(self, nombre):
        self._nombre =  nombre 
    @edad.setter
    def edad(self, edad):
        self._edad =  edad 


    #methods
'''    def mostrar_detalle(self):
        print(f'Nombre: {self._nombre}, Apellido: {self._apellido}, edad: {self._edad}')
'''

# Clase hija 
class Empleado(Persona):
    # inicializar atributos 
    def __init__(self, nombre, edad, sueldo):
        #instancia de la calse padre
        super().__init__(nombre, edad)
        self._sueldo = sueldo
    #sobre el metodo __str__
    def __str__(self):
    # El metodo super ayuda a acceder a los datos del padre
        return f'{super().__str__()}, {self._sueldo}'
    
    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo


if __name__ == '__main__':

    empleado1 = Empleado('joshua', 25, 50000)
    print(empleado1.nombre)
    print(empleado1.edad)
    print(empleado1.sueldo)