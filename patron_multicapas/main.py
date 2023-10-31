from gui.GUI import GUI
from data.data import Data
from business.business import Business

"""
Inicio de la Aplicación:

Este script es el punto de entrada de la aplicación. Importa las clases necesarias para la funcionalidad de la calculadora
y crea una instancia de la clase GUI, pasando un objeto Business que utiliza un objeto Data para manejar los datos y las
operaciones.

Autor: Valesska Blanco y Ramsés Gutiérrez
"""

if __name__ == '__main__':
    gui = GUI(Business(Data()))