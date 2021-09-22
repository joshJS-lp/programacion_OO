from class_persona import Persona #pra importar todas las clases se usa *

print('Instancia de Objetos'.center(50,'-'))
persona00 = Persona('Carolina', 'Perez', 24)
persona00.mostrar_detalle()

# Metodo destructor para librerar espacio en memoria
del persona00