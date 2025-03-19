### Funciones ###

# Útil para operaciones complejas y repetitivas durante la ejecución del código

def my_function ():
    print("Esto es una función")

my_function()
my_function()

def product_two_values(value1, value2):
    print(value1 * value2)

product_two_values(5, 2)
product_two_values(53232, 254734)
product_two_values("Hola", 2)
product_two_values(3.452, 2.872) # El tipado débil de Python, mientras pasemos tipos de datos que puedan concatenarse no habrá problema, por lo que 
# no hace falta y no se puede forzar de alguna manera el tipo de dato que tiene que recibir la función. Si la función fuera de división, petaría al llegar
# a las cadenas de texto

my_result = product_two_values(53232, 254734)
print(my_result) # Imprime el valor por consola porque estaba definido el print en la propia función, pero este print está devolviendo "None", ya que la
# función no tiene return

def product_two_values_with_return(value1, value2):
    my_result = value1 * value2
    return my_result # Lo que hacíamos con el print, lo devuelve directamente con el return. El resultado hay que asignarlo a una variable y no hay que
# meter el print en la propia función, lo podemos poner por fuera y si tendremos el resultado esperado.

my_result = product_two_values_with_return(10, 5)
print(my_result)


def print_name (name, surname):
    print(f'Tú te llamas {name} {surname}')

print_name("Adolfo", "López")
print_name(surname = "López", name = "Adolfo")

def print_name_with_default (name, surname, alias = "sin alias"): # Le meto un valor por defecto por si no se indica alias, a través de la string "Sin alias"
    print(f'Tú eres {name} {surname} y te llaman el {alias}')

print_name_with_default("Adolfo", "López")
print_name_with_default("Adolfo", "López", "tito")


def print_texts(*text): # Si le pongo el asterisco significa que le puedo pasar el número de parámetros que yo quiera
    print(text)

print_texts("Holaaaaaa")
print_texts("Holaaaaaa", "chavaleeeeeh")

def print_upper_texts(*texts): 
    for text in texts:
        print(text.upper())

print_upper_texts("Holaaaaaa", "chavaleeeeeh", "todo en mayúsculas")