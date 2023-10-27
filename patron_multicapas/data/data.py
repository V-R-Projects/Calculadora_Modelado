

class Data():

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        self.memoria = []
        self.MEMORIA_MAX = 10
        self.operationsText = {
            "+": str(self.num1) + " + " + str(self.num2) + " = " + str(self.resultado),
            "-": str(self.num1) + " - " + str(self.num2) + " = " + str(self.resultado),
            "*": str(self.num1) + " * " + str(self.num2) + " = " + str(self.resultado),
            "/": str(self.num1) + " / " + str(self.num2) + " = " + str(self.resultado),
            "Avg": "Avg " + str(self.memoria) + " = " + str(self.resultado),
            "Primo": "Primo " + str(self.num1) + " = " + str(self.resultado),
            "M+": "M+ " + str(self.resultado) + " > " + str(self.memoria),
            "Binario": "Binario " + str(self.num1) + " = " + str(self.resultado)
        }

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

    def get_operation_text(self, operation):
        return self.operationsText[operation]