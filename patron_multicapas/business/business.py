import sys
from pathlib import Path

if __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    import patron_multicapas.business
    __package__ = 'patron_multicapas.business'

    from ..data.data import Data

"""
Clase Business:

Esta clase implementa la lógica de negocio para una calculadora utilizando una arquitectura de capas. Se encarga de
gestionar las operaciones matemáticas, realizar cálculos y manejar las solicitudes del usuario. Esta clase
sigue un enfoque multicapa en el diseño de la aplicación.

Autor: Valesska Blanco y Ramsés Gutiérrez
"""

class Business:
    def __init__(self, dataHandler_):
        self.dataHandler = dataHandler_
        self.operationsDict = {
            "+": self.realizar_suma,
            "-": self.realizar_resta,
            "*": self.realizar_multiplicacion,
            "/": self.realizar_division,
            "Avg": self.calcular_promedio,
            "Primo": self.es_primo,
            "M+": self.guardar_memoria,
            "Binario": self.mostrar_binario,
            "C": self.clear,
            "Data": self.mostrar_memoria
        }

    def guardar_memoria(self):
        self.dataHandler.set_memory()
        self.save_result(self.dataHandler.get_resultado())

    def save_result(self, result):
        self.dataHandler.set_resultado(result)

    def save_operation(self, result):
        self.dataHandler.set_operation(result)

    def save_num1(self, num1):
        self.dataHandler.set_num1(num1)

    def save_num2(self, num2):
        self.dataHandler.set_num2(num2)

    def realizar_suma(self):
        result = self.dataHandler.get_num1() + self.dataHandler.get_num2()
        self.save_result(result)

    def realizar_resta(self):
        result = self.dataHandler.get_num1() - self.dataHandler.get_num2()
        self.save_result(result)

    def realizar_multiplicacion(self):
        result = self.dataHandler.get_num1() * self.dataHandler.get_num2()
        self.save_result(result)

    def realizar_division(self):
        if self.dataHandler.get_num2() != 0:
            result = self.dataHandler.get_num1() / self.dataHandler.get_num2()
            self.save_result(result)
        else:
            self.save_result("Error: Division por cero")

    def calcular_promedio(self):
        memory = self.dataHandler.get_memory()
        if len(memory) > 0:
            result = sum(memory) / len(memory)
            self.save_result(result)
        else:
            self.save_result(0)

    def mostrar_binario(self):
        num1 = self.dataHandler.get_num1()
        if (num1 % 1 == 0):
            result = bin(int(num1))[2:]
            self.save_result(result)
        else:
            self.save_result("Error: Entrada invalida")

    def es_primo(self):
        num1 = self.dataHandler.get_num1()
        if (num1 % 1 == 0):
            if num1 <= 1:
                result = "No es primo"
            else:
                es_primo = "Si es primo"
                for i in range(2, int(num1 ** 0.5) + 1):
                    if num1 % i == 0:
                        es_primo = "No es primo"
                        break
                result = es_primo
        else:
            result = "Error: Entrada invalida"

        self.save_result(result)

    def equal(self):
        op = self.dataHandler.get_operation()
        if (op):
            self.operationsDict[op]()
            self.save_operation("")

    def mostrar_memoria(self):
        self.save_result(str(self.dataHandler.get_memory()))
    

    def opPress(self, operation):
        if self.dataHandler.get_operation():
            self.equal()
            self.save_num1(self.dataHandler.get_resultado())
            
        if self.dataHandler.get_resultado():
            self.save_result("")
        self.save_operation(operation)

    def clear(self):
        self.save_operation("")
        self.save_result("")

    def send_request(self, event, txt):
        btn = event.widget.cget("text")
        special = False
        if txt and not self.dataHandler.get_operation():
            self.save_num1(float(txt))
        elif txt:
            self.save_num2(float(txt))

        if btn in "+-*/":
            self.opPress(btn)
        elif btn == "=":
            self.equal()
        else:
            special = True
            self.save_operation(btn)
            self.operationsDict[btn]()
        
        return self.dataHandler.get_resultado(), special
