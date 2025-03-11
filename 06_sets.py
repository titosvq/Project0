### Sets ###

# No es una estructura ordenada, ordena por hash
# Un set no admite repetidos
# Acceso a elementos y busqueda no funciona

mi_set = set()
print(type(mi_set))

mi_set = {"Adolfo", 36, "Utrera"}
print(type(mi_set))
print(len(mi_set))

mi_set.add("Lopez")
print(mi_set)

print("Utrera" in mi_set)
print("Sevilla" in mi_set)

mi_set.remove("Utrera")
print(mi_set)

mi_set.clear()
print(len(mi_set))

# Recomendación para estudiar, poner la variable (de tipo set) y añadir el punto "." para ver que operaciones podemos ejectuar, ir probando y tirando de documentación para conocerlas.

mi_set = {"Adolfo", 36, "Lopez"}
convertido_a_lista = list(mi_set)
print(convertido_a_lista[0]) # Cuidado con la ordenación que trae al convertirse a lista, porque el set no era una estructura ordenada

mi_otro_set = {"Andalucía", "España", "Europa"}

mi_nuevo_set = mi_set.union(mi_otro_set) # Almacenamos el union en la variable, podría hacerlo dentro de un print sólamente.
print(mi_nuevo_set)
print(mi_nuevo_set.difference(mi_set))

del mi_set
# print(mi_set) Daría error, porque mi_set ya no estaría definido al utilizar del para borrarlo.