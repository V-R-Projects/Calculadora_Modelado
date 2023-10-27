from model import OperationsModel

modelo_calculadora = OperationsModel()

modelo_calculadora.set_num1(36)
modelo_calculadora.set_num2(2)
modelo_calculadora.realizar_multiplicacion()
modelo_calculadora.guardar_bitacora("*")

print("Resultado: ", modelo_calculadora.resultado)
