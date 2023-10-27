
"""
Clase Data:

Esta clase se encarga de gestionar los datos y el registro de operaciones para la calculadora utilizando una arquitectura de
capas. Almacena los números ingresados por el usuario, el resultado de las operaciones, la operación actual y la memoria.
También registra las operaciones en un archivo de bitácora.

Autor: Valesska Blanco y Ramsés Gutiérrez
"""

class Data():

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = ""
        self.operation = ""
        self.memoria = []
        self.MEMORIA_MAX = 10
        self.clear_log()
        

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
        self.set_log()

    def get_operation(self):
        return self.operation

    def set_operation(self, operation):
        self.operation = operation


    # Data Log and Memory

    def set_memory(self):
        try:
            if (self.resultado):
                # Actualiza la memoria en el modelo
                self.memoria.append(self.resultado)

                # Verifica si hay más de 10 valores en la memoria
                if len(self.memoria) > self.MEMORIA_MAX:
                    # Elimina el valor más antiguo de la memoria y del archivo
                    self.memoria = self.memoria[1:]

            # self.resultado = self.memoria

        except Exception as e:
            self.resultado = f"Error: {str(e)}"

    def get_memory(self):
        return self.memoria

    def set_log(self):
        if self.operation and self.operation != "Data":
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
            with open ("./patron_multicapas/Bitacora.txt", "a") as archivo:
                archivo.write(operationsText[self.operation] + "\n")
                archivo.close()
    
    def clear_log(self):
        with open ("./patron_multicapas/Bitacora.txt", "w") as archivo:
            archivo.write("")
            archivo.close()