"""
Clase OperationsModel:

Este es el modelo en el patrón de arquitectura MVC para una calculadora en Python.
Contiene métodos para realizar operaciones matemáticas básicas, gestionar memoria,
verificar si un número es primo, y mantener un registro de operaciones en un archivo
de bitácora.

Autores: Valesska Blanco y Ramsés Gutiérrez
"""

class OperationsModel:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        self.memoria = []
        self.MEMORIA_MAX = 10

    # Get - Set
    def get_num1 (self):
        return self.num1
    
    def set_num1 (self, num1):
        self.num1 = num1

    def get_num2 (self):
        return self.num2
    
    def set_num2 (self, num2):
        self.num2 = num2

    def get_resultado(self):
        return self.resultado

    def set_resultado(self, resultado):
        self.resultado = resultado
    
    # Operations

    def realizar_suma(self):
        self.resultado = self.num1 + self.num2

    def realizar_resta(self):
        self.resultado = self.num1 - self.num2

    def realizar_multiplicacion(self):
        self.resultado = self.num1 * self.num2

    def realizar_division(self):
        if self.num2 != 0:
            self.resultado = self.num1 / self.num2
        else:
            self.resultado = "Error: Division por cero"

    def calcular_promedio(self):
        if len(self.memoria) > 0:
            self.resultado = sum(self.memoria) / len(self.memoria)
        else:
            self.resultado = 0

    def mostrar_binario(self):
        if (self.num1 % 1 == 0):
            self.resultado = bin(int(self.num1))[2:]
        else:
            self.resultado = "Error: Entrada invalida"

    def es_primo(self):
        if (self.num1 % 1 == 0):
            numero_entero = self.num1
            if numero_entero <= 1:
                self.resultado = "No es primo"
            else:
                es_primo = "Si es primo"
                for i in range(2, int(numero_entero ** 0.5) + 1):
                    if numero_entero % i == 0:
                        es_primo = "No es primo"
                        break
                self.resultado = es_primo
        else:
            self.resultado = "Error: Entrada invalida"

    def guardar_memoria(self):
        try:
            # Actualiza la memoria en el modelo
            self.memoria.append(self.resultado)

            # Verifica si hay más de 10 valores en la memoria
            if len(self.memoria) > self.MEMORIA_MAX:
                # Elimina el valor más antiguo de la memoria y del archivo
                self.memoria = self.memoria[1:]

            # self.resultado = self.memoria

        except Exception as e:
            self.resultado = f"Error: {str(e)}"

    def mostrar_memoria(self):
        self.resultado = str(self.memoria)

    def guardar_bitacora(self, operation):

        operationsText = {
            "+": str(self.num1) + " + " + str(self.num2) + " = " + str(self.resultado),
            "-": str(self.num1) + " - " + str(self.num2) + " = " + str(self.resultado),
            "*": str(self.num1) + " * " + str(self.num2) + " = " + str(self.resultado),
            "/": str(self.num1) + " / " + str(self.num2) + " = " + str(self.resultado),
            "Avg": "Avg " + str(self.memoria) + " = " + str(self.resultado),
            "Primo": "Primo " + str(self.num1) + " = " + str(self.resultado),
            "M+": "M+ " + str(self.resultado) + " > " + str(self.memoria),
            "Binario": "Binario " + str(self.num1) + " = " + str(self.resultado)
        }

        with open ("Bitacora.txt", "a") as archivo:
            archivo.write(operationsText[operation] + "\n")
            archivo.close()
    
    def limpiar_bitacora(self):
        with open ("Bitacora.txt", "w") as archivo:
            archivo.write("")
            archivo.close()

