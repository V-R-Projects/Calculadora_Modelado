'''
**********************************************************

Modelo de Operaciones para Calculadora
Autores: Valesska Blanco Montoya y Ramsés Gutiérrez Rodríguez

**********************************************************
'''

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
            self.resultado = "Error: División por cero"

    def calcular_promedio(self):
        if len(self.memoria) > 0:
            self.resultado = sum(self.memoria) / len(self.memoria)
        else:
            self.resultado = "Error: No hay suficientes elementos para calcular promedio"

    def mostrar_binario(self):
        try:
            numero_float = float(self.num1)
            self.resultado = bin(int(numero_float))[2:]
        except ValueError:
            self.resultado = "Error: Entrada inválida"

    def es_primo(self):
        try:
            numero_entero = int(self.num1)
            if numero_entero <= 1:
                self.resultado = False
            else:
                es_primo = True
                for i in range(2, int(numero_entero ** 0.5) + 1):
                    if numero_entero % i == 0:
                        es_primo = False
                        break
                self.resultado = es_primo
        except ValueError:
            self.resultado = "Error: Entrada inválida"

    def guardar_memoria(self):
        try:
            # Actualiza la memoria en el modelo
            self.memoria.append(self.resultado)

            # Verifica si hay más de 10 valores en la memoria
            if len(self.memoria) > self.MEMORIA_MAX:
                # Elimina el valor más antiguo de la memoria y del archivo
                self.memoria = self.memoria[1:]

            with open("memoria.txt", "w") as archivo:
                for valor in self.memoria:
                    archivo.write(str(valor) + '\n')

            self.resultado = "Valor guardado en memoria."

        except Exception as e:
            self.resultado = f"Error: {str(e)}"

    
