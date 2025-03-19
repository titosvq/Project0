### Bucles ###

# Nos sirven para pasar por un mismo código varias veces

## While ##

my_condition = 0

while my_condition < 12:
    print(my_condition) # Si la condición no cambia, el bucle es infinito
    my_condition += 2 # Añadimos un operador para que vaya cambiando la condición y acabe el bucle
if my_condition == 10:
    print("Mi condición es igual a 10")

else: # Tiene que haber un if delante, pero si el while fuera un bucle infinito se puede meter sin necesidad del if. Un elif no lo acepta sin if delante
    print("Mi condición es mayor que 10")

print("La ejecución del código continúa")

while my_condition < 30:
    my_condition += 1
    if my_condition == 21:
        print("Mi condición es 21")
        break # Marca que se detenga la ejecución del código para una condición dada
    print(my_condition)

print("Continúa la ejecución 2")

## For ##

# Recordemos que "element" no es palabra reservada, es una forma de llamarlo, podríamos ponerle "fsdfsdfds"

my_list = [23, 34, 56, 32, 11, 23, 45, 78]
for element in my_list: # Va recorriendo los elementos de la lista, el while estaba atado a cumplir una condición. 
    # Para el caso del for, está más destinada a un conjunto finito de elementos
    print(element)

my_tuple = ("Pera", "Manzana", "Plátano", "Melón")
for element in my_tuple: 
    print(element)

my_set = {"Adolfo", "López", 36}
for element in my_set:
    print(element)

my_dict = {"Nombre":"Adolfo", "Apellido":"López", "Edad":36, 1:"Python"} # En el caso de diccionarios, imprime las keys
for element in my_dict: 
    print(element)

for element in list(my_dict.values()): # En este caso podríamos imprimir los valores del diccionario
    print(element)

for element in list(my_dict.values()): # En este caso podríamos imprimir los valores del diccionario
    print(element)


for element in my_dict: 
    print(element)
    if element == "Edad":
        break # Acaba con el bucle for y sale del bloque
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continúa 3")

for element in my_dict: 
    print(element)
    if element == "Edad":
        continue # Se salta el último se ejecuta pero vuelve al principio del for
    else:
        print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")