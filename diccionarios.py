from sqlite3 import TimestampFromTicks


diccionario={
    'nombre':'Mateo',
    'edad':'19',
    'estatura':'1.66',
    'peso':'50',
    'estudios':'Tecnica',
    'Asignatura':'Nuevas Tecnologias',
    'fecha_nacimiento':'26/09/2002',
    'hobbies':'Jugar Pokemon Unite',
}


"""Accediendo de forma individual a los atributos
y valores de un diccionario """
print(diccionario)
print(diccionario['nombre'])
print(diccionario.get('edad'))

""" Acceder a TODOS los atributos y valores
de un diccionario al mismo tiempo
RECORRER UN DICCIONARIO """

for clave,valor in diccionario.items():
    print(clave,valor)

##Agregar desde el codigo una propiedad mas
diccionario['apellido'] = 'Franco'

print(diccionario)