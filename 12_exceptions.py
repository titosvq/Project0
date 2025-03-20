### Excepciones ###

# Manejo de errores - Exception Handling

numberOne = 1
numberTwo = 5
numberTwo = "1"

# try - except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# try - except - else

numberTwo = 1

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    print("La ejecución de código continúa") # Se ejecuta si no se produce la expcepción
finally: # Opcional
    print("La ejecución continúa 2") # Se ejecuta siempre


# Excepciones por tipo

numberTwo = "caca"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except ValueError: # Ejecuta si hay errores de tipo valor
    print("Se ha producido un value error")
except TypeError: # Sólo se ejecuta por errores de tipo de dato
    print("Se ha producido un type error")
else: # Opcional
    print("La ejecución de código continúa") # Se ejecuta si no se produce la expcepción
finally: # Opcional
    print("La ejecución continúa 3") # Se ejecuta siempre

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: # Se lo salta porque el error no es de valor, sino de tipo de dato, está intentando sumar int con string
    print(error)
except Exception as exception:
    print(exception)


