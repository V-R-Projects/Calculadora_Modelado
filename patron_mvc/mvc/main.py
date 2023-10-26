from modelo import OperationsModel
from vista import View
from controlador import Controller

class Main:

    def __init__(self):
        self._model = OperationsModel()
        self._view = View()
        self._controller = Controller(self._model, self._view)