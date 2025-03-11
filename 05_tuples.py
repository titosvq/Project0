### Tuplas ###

tupla = tuple()
mi_tupla = ("pera", "naranja", "manzana", "fresa", "pera")
print(mi_tupla)

print(mi_tupla.count("pera"))
print(mi_tupla.index("fresa"))
print(mi_tupla[3])

otra_tupla = ("tomate", "pimiento", "cebolla", "calabaza")
sumatupla = mi_tupla + otra_tupla
print(sumatupla)

print(sumatupla[2:6])

mi_tupla = list(mi_tupla) # Convierto en lista
print(type(mi_tupla))

mi_tupla.insert(3, "sandia") #Convertido en lista si podemos anadir valores
print(mi_tupla)
print(len(mi_tupla))

del mi_tupla # print(mi_tupla)    -----> NameError: name 'mi_tupla' is not defined