### Clases ###

class MyEmptyPerson: # Ahora definimos los nombres de las clases con CamelCase en vez snake_case (que usábamos para las variables), 
    # por buenas prácticas, sin espacios, sin guiones bajos
    pass # Para poder dejar la clase vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__ (self, name, surname): # No es una función, es un constructor de clase. Siempre hay que poner el init y el self para definir el constructor
        self.name = name # Se van creando las propiedades con self y se les va dando valor
        self.surname = surname

my_person = Person("Adolfo", "López")
print(my_person.name)

class Person:
    def __init__ (self, name, surname): # No es una función, es un constructor de clase. Siempre hay que poner el init y el self para definir el constructor
        self.fullname = f"{name} {surname}"

my_person = Person("Adolfo", "López")
print(my_person.fullname)

class Person:
    def __init__ (self, name, surname, alias = "sin alias"): # Igual que en las funciones, se pueden meter valores por defecto por si no se introduce algún
        # parámetro
        self.fullname = f"{name} {surname} {alias}" # Es una propiedad pública, podemos desde fuera acceder y modificar.
        self.__name = name # Hemos definido variable/propiedad privada con __. Desde fuera no podría modificarla 
        self.__surname = surname

    def walk (self):
        print(f"{self.fullname} está caminando") # Una función dentro de una clase: podemos llamar al self para acceder a lo que haya guardado
        # dentro de self, no volvemos a llamar a la clase.

my_other_person = Person("Marian", "De la Vega")
print(my_other_person.fullname)
my_other_person.walk()

my_other_person.fullname = "Jaime López el guapo" # Puedo cambiar directamente alguna propiedad de mi clase, sin necesidad de tirar del constructor
print(my_other_person.fullname)

my_other_person.fullname = 3242
print(my_other_person.fullname)