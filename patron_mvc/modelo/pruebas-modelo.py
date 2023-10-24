from modelo import *

modelo_calculadora = OperationsModel()

modelo_calculadora.realizar_suma(5,5)
print("Resultado: ", modelo_calculadora.resultado)

modelo_calculadora.es_primo(7)
print("¿Es primo?: ", modelo_calculadora.resultado)

modelo_calculadora.mostrar_binario(10.5)
print("Representación binaria: ", modelo_calculadora.resultado)

modelo_calculadora.realizar_resta(5,5)
print("Resultado: ", modelo_calculadora.resultado)

modelo_calculadora.realizar_division(10,5)
print("Resultado: ", modelo_calculadora.resultado)

# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(1144)
# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(4)
print(modelo_calculadora.memoria)
# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(5)
print(modelo_calculadora.memoria)
# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(6)
print(modelo_calculadora.memoria)
# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(2)
print(modelo_calculadora.memoria)
# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(1144)

# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(4)
print(modelo_calculadora.memoria)
# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(5)
print(modelo_calculadora.memoria)
# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(6)
print(modelo_calculadora.memoria)
# Guarda un valor en memoria
modelo_calculadora.guardar_memoria(2)
print(modelo_calculadora.memoria)

modelo_calculadora.guardar_memoria(1000)
print(modelo_calculadora.memoria)