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

class Business:
    def __init__(self, dataHandler_ : Data):
        self.dataHandler = dataHandler_
        self.operationsDict = {
            "+": self.realizar_suma,
            "-": self.realizar_resta,
            "*": self.realizar_multiplicacion,
            "/": self.realizar_division,
            "Avg": self.calcular_promedio,
            "Primo": self.es_primo,
            "M+": self.guardar_memoria,
            "Binario": self.mostrar_binario
        }

    def guardar_memoria(self):
        self.dataHandler.set_memory()

    def save_result(self, result):
        self.dataHandler.set_resultado(result)

    def save_num1(self, num1):
        self.dataHandler.set_num1(num1)

    def save_num2(self, num2):
        self.dataHandler.set_num2(num2)

    def realizar_suma(self):
        result = self.dataHandler.getnum1() + self.dataHandler.getnum2()
        self.save_result(result)

    def realizar_resta(self):
        result = self.dataHandler.getnum1() - self.dataHandler.getnum2()
        self.save_result(result)

    def realizar_multiplicacion(self):
        result = self.dataHandler.getnum1() * self.dataHandler.getnum2()
        self.save_result(result)

    def realizar_division(self):
        if self.dataHandler.get_num2() != 0:
            result = self.dataHandler.getnum1() / self.dataHandler.getnum2()
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

    def send_request(self, event, txt):
        
        return self.dataHandler.get_resultado()