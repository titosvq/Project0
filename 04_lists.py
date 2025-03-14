### Listas ###

my_list = list()
my_list = [36, 1.73, "Adolfo", "López"]

print(my_list)
print(len(my_list))
print(type(my_list))

edad, altura, nombre, apellido = my_list

print(apellido)

my_2list = [6, 1.18, "Jaime", "López"]

print(my_list + my_2list)
print(my_2list + my_list)
print(my_list * 2)

my_2list.append("Salesianos") # Añade un elemento al final de la lista
print(my_2list)

my_2list.insert(2, "pokémon") # Añade un elemento en la posición indicada
print(my_2list)

my_2list[2] = "kirby" # Modifica el elemento en la posición indicada
my_2list.remove("Salesianos") # Elimina el primer elemento que coincida con el parámetro
print(my_2list)

list_int = [8, 7, 4, 4, 5, 6, 7]
print(list_int)

print(list_int.pop()) # Elimina el último elemento de la lista
print(list_int)

print(list_int.pop(4)) # Elimina el elemento de la posición indicada
print(list_int)

variablepop = list_int.pop(4)
print(variablepop)

del list_int[0] # Elimina el elemento de la posición indicada
print(list_int)

list_int = [8, 7, 4, 4, 5, 6, 7]
print(list_int)

my_new_list = list_int.copy() # Copia la lista
list_int.clear() # Elimina todos los elementos de la lista
print(my_new_list)

my_new_list.reverse() # Invierte el orden de los elementos de la lista
print(my_new_list)

my_new_list.sort() # Ordena los elementos de forma ascendente
print(my_new_list)

print(3 in list_int) #Buscar un elemento dentro de la lista, una forma de respuesta true or false