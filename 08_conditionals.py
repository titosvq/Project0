### Condicionales ###

# Si se cumple una condición se ejecuta el código

mi_condición = True # Tiene que ser verdadero para ejecutar 

if mi_condición: # Es lo mismo que if mi_condición == True, ponerlo sería redundante
    print("Se ejecuta la condición del if")

print("La ejecución continúa 1")

mi_condición = False # Si es falso no se ejecuta

if mi_condición:
    print("Se ejecuta la condición del if")

print("La ejecución continúa 2")


my_condition = 5 * 2

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition >= 10:
    print("Se ejecuta la condición del tercer if")

if my_condition > 10:
    print("Se ejecuta la condición del cuarto if")

print("La ejecución continúa 3")


if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

print("La ejecución continúa 4")

# Añadimos operadores lógicos

my_condition = 5 * 3 # Meter distintos valores para ver el comportamiento de las salidas por terminal

if my_condition > 10 and my_condition < 20:

    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20") # Importante la indentación para que lo ejecute o no, según toque

print("La ejecución continúa 5")


my_condition = 5 * 2

if my_condition == 10:
    print("Se ejecuta la condición")

elif my_condition > 10 and my_condition < 20: # El orden que lleva establece jerarquía
    print("Es mayor que 10 y menor que 20")

elif my_condition == 25:
    print("Es igual a 25")

else:
    print("Es menor o igual que 10 o mayor o igual que 20") # Importante la indentación para que lo ejecute o no, según toque

print("La ejecución continúa 5")

my_string = "" # Un string vacío es False
my_string = "Mi cadena de texto"

if my_string: # Comprueba true or false según tenga contenido la variable y responde en consecuencia, 
    print("Mi cadena de texto no es vacía")

if my_string == "Mi cadena de texto":
    print("Mi cadena de texto no es vacía 1")

my_string = ""
if not my_string == "Mi cadena de texto": # Ejemplo de if not
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textooooo":
    print("Mi cadena de texto no es vacía")