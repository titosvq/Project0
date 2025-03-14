### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Adolfo", "Apellido":"López", "Edad":36, 1:"Python", } # Para almacenar datos en tipo clave-valor, key-value, dentro de los valores se puede jugar con los tipos de datos
my_dict = {
    "Nombre":"Adolfo", 
    "Apellido":"López", 
    "Edad":36, 
    "Lenguajes":{"Python", "HTML", "JavaScript"},   
    1:1.73
    }

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"]) # Print de alguna clave concreta, devuelve el valor
my_dict["Nombre"] = "Jaime" # Sustituir valores
print(my_dict["Nombre"])
my_dict["Población"] = "Utrera" # Añadir valores al diccionario
print(my_dict["Población"])
print(my_dict)

del my_dict["Población"]
print(my_dict)

print("Adolfo" in my_dict) # Me dice false, porque aquí está buscando por clave, no por valor
print("Nombre" in my_dict)

print(my_dict.items()) # Listado de los ítems
print(my_dict.keys()) # Listado de todas las claves
print(my_dict.values()) # Listado de todos los valores

# print(my_dict.fromkeys()) # A este caso no le encuentro utilidad, puede hacerse un diccionario nuevo directamente

my_list = ["Nombre", "Apellido", "Población"]
my_new_dict = dict.fromkeys(my_list) # Posible utilidad, de pasar una lista a diccionario
print(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict) # Otra utilidad, combinar las keys de otro diccionario existente al crear el nuevo
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Marian", "De la Vega")) # Mete el/los valores a todas las claves
print(my_new_dict)

my_values = my_new_dict.values() # Creamos variable con los valores de my_new_dict
print(type(my_values)) # Nuevo tipo de dato: dict.values

print(list(my_new_dict)) # Convierto a lista
print(list(my_new_dict.values())) # Accedo a los valores y creo una lista, me da una lista de valores
print(dict.fromkeys(list(my_new_dict.values()))) # Dándole vueltas: imprimo diccionario con las keys de una lista creada con los valores del dict my_new_dict
print(list(dict.fromkeys(list(my_new_dict.values())).keys())) # Muy rebuscado
print(set(my_new_dict)) # Convierto a set