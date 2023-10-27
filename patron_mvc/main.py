from model.model import OperationsModel
from view.view import View
from controller.controller import Controller

class Main:

    def __init__(self):
        self._model = OperationsModel()
        self._view = View()
        self._controller = Controller(self._model, self._view)

if __name__ == "__main__":
    Main()