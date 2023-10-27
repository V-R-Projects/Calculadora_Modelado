from gui.GUI import GUI
from data.data import Data
from business.business import Business

if __name__ == '__main__':
    gui = GUI(Business(Data()))