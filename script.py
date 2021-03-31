# Dentro de las funciones, los argumentos son asignados a variables llamadas parámetros, 
#función definida por el usuario que recibe un argumento, con el parámetro bruce:

def muestra_dos_veces(bruce):
print bruce
print bruce


# Esta función funciona con cualquier valor que pueda ser mostrado en pantalla:

>>> muestra_dos_veces('Spam')
Spam
Spam

>>> muestra_dos_veces(17)
17
17

>>> muestra_dos_veces(math.pi)
3.14159265359
3.14159265359


# Las mismas reglas de composición que se aplican a las funciones internas, también 
# se aplican a las funciones definidas por el usuario, de modo que podemos usar cualquier
# tipo de expresión como argumento para muestra_dos_veces:

>>> muestra_dos_veces('Spam '*4)
Spam Spam Spam Spam
Spam Spam Spam Spam

>>> muestra_dos_veces(math.cos(math.pi))
-1.0
-1.0
