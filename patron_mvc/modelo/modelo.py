'''
**********************************************************

Modelo de Operaciones para Calculadora
Autores: Valesska Blanco Montoya y Ramsés Gutiérrez Rodríguez

**********************************************************
'''

class OperationsModel:

    def __init__(self):
        self.resultado = 0
        self.memoria = []
        self.MEMORIA_MAX = 10

    def realizar_suma(self, num1, num2):
        self.resultado = num1 + num2

    def realizar_resta(self, num1, num2):
        self.resultado = num1 - num2

    def realizar_multiplicacion(self, num1, num2):
        self.resultado = num1 * num2

    def realizar_division(self, num1, num2):
        if num2 != 0:
            self.resultado = num1 / num2
        else:
            self.resultado = "Error: División por cero"

    def calcular_promedio(self, numeros):
        if len(numeros) > 0:
            self.resultado = sum(numeros) / len(numeros)
        else:
            self.resultado = "Error: No hay suficientes elementos para calcular promedio"

    def mostrar_binario(self, numero):
        try:
            numero_float = float(numero)
            self.resultado = bin(int(numero_float))[2:]
        except ValueError:
            self.resultado = "Error: Entrada inválida"

    def es_primo(self, numero):
        try:
            numero_entero = int(numero)
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

    def guardar_memoria(self, numero):
        try:

            # Actualiza la memoria en el modelo
            self.memoria.append(numero)

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

    def obtener_resultado(self):
        return self.resultado
    
