class MiClase:


    #Variable de clase
    '''
        Estas varibales son las mismas en todos los objetos
    '''
    varible_clase = 'Es una varible de clase estatico'
    varible_clase2 = 'Varibale de clase 2'
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
        print(cls.varible_clase2)

#instancia y uso del metodo estatico
MiClase.metodo_estatico()
MiClase.metodo_clase()

miObject = MiClase('Variable de instancia')
'''
La instancia de objetos de la clase dinamico pueden acceder 
a los metos estaticos pero los estaticos no pueden acceder
a los metodos dinamicos...
'''
miObject.metodo_estatico()
