from model.model import OperationsModel
from view.view import View
from controller.controller import Controller

"""
Clase Main:

Este es el punto de entrada principal para la aplicación de la calculadora MVC. En esta clase, se crea una instancia del
modelo (OperationsModel), una instancia de la vista (View) y una instancia del controlador (Controller). La clase Main
inicia la aplicación creando una instancia de sí misma.

Autor: Valesska Blanco y Ramsés Gutiérrez
"""

class Main:

    def __init__(self):
        self._model = OperationsModel()
        self._view = View()
        self._controller = Controller(self._model, self._view)

if __name__ == "__main__":
    Main()