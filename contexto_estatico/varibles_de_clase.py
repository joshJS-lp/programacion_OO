class MiClase:


    #Variable de clase
    '''
        Estas varibales son las mismas en todos los objetos
    '''
    varible_clase = 'Es una varible de clase'

    def __init__(self,varibale_de_instancia):
        self.varibale_de_instancia = varibale_de_instancia

    #metodo estatico 
    '''Los metodos estaticos no acceden a las
        variables de instancia
        por lo que no esta relacionado directamente
        con la clase...
    '''
    @staticmethod
    def metodo_estatico():
        print(MiClase.varible_clase)

    #Metodo de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.varible_clase)
# Para acceder una variable de clase no e snecesario
# instanciar la clase...
print(MiClase.varible_clase)
#Clase al vuelo..
MiClase.varible_clase2 = 'segunda clase...'
print(MiClase.varible_clase2)
# varibale de instancia 
miClase = MiClase('Soy una variabole de instancia')
print(miClase.varibale_de_instancia)

#instancia y uso del metodo estatico
MiClase.metodo_estatico()
MiClase.metodo_clase()