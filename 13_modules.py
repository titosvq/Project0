### Módulos ###

import module  # Forma 1, llamando al módulo general.

# No podría acceder a mis ficheros que empiezan por número para usarlos como módulos porque python no acepta números como inicio de nombre de archivo

from module import sum, printValue # Forma 2, llamando funciones concretas

module.sum(3, 4, 2) # Forma 1, hay que llamar las funciones que queramos del módulo
module.printValue("Holaaaaa")

sum(3, 4, 2) # Forma 2, puedo invocar las funciones directamente
printValue("Holaaaaa")

# Importar otro tipos de módulo, del propio Python o externos #

import math # Biblioteca de matemáticas, pertenece a Python

print(math.pi)
print(math.e)
print(math.pow(2, 4)) # Potencia
print(math.cos(23))

from math import pi as PI_VALUE # Creo alias para elementos que quiera invocar del módulo

print(PI_VALUE)



