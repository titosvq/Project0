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

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# print(my_dict.fromkeys()) # A este caso no le encuentro utilidad, puede hacerse un diccionario nuevo directamente

my_list = ["Nombre", "Apellido", "Población"]
my_new_dict = dict.fromkeys(my_list) # Posible utilidad, de pasar una lista a diccionario
print(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict) # Otra utilidad, combinar las keys de otro diccionario existente al crear el nuevo
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Marian", "De la Vega")) # Mete los valores a todas las claves
print(my_new_dict)