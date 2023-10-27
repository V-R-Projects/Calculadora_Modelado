import tkinter as tk
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

    import patron_multicapas.gui
    __package__ = 'patron_multicapas.gui'

    from ..business.business import Business

class GUI:
    def __init__(self, business_ : Business):
        self.business = business_
        self.window = tk.Tk()
        self.window.geometry('300x300')
        self.window.title('MVC Calculator')

        #Stablish the grid
        for i in range(7):
            self.window.rowconfigure(i, weight=1)

        for i in range(5):
            self.window.columnconfigure(i, weight=1)

        # Creating all the widgets
        self.txtMain     = tk.Entry(self.window, justify=tk.RIGHT)
        self.numBtns     = [ tk.Button(self.window, text=str(x)) for x in (["C", "0", "."] + list(range(1,10)))]
        self.opBtns      = [ tk.Button(self.window, text=str(x)) for x in ["/", "*", "-", "+"]]
        self.btnAvg      = tk.Button(self.window, text="Avg")
        self.btnPrimo    = tk.Button(self.window, text="Primo")
        self.btnBinario  = tk.Button(self.window, text="Binario")
        self.btnData     = tk.Button(self.window, text="Data")
        self.btnMp       = tk.Button(self.window, text="M+")
        self.btnEqual    = tk.Button(self.window, text="=")

        self.placeWidgets()
        self.window.mainloop()
        

    
    def placeWidgets(self):
        for i in range(len(self.numBtns)):
            self.numBtns[i].grid(row=(6-i//3), column=i%3, sticky=tk.N+tk.E+tk.S+tk.W)
        for i in range(len(self.opBtns)):
            self.opBtns[i].grid(row=3+i, column=3, sticky=tk.N+tk.E+tk.S+tk.W)

        self.txtMain.grid(row=0, column=0, columnspan=5, sticky=tk.N+tk.E+tk.S+tk.W)
        self.btnAvg.grid(row=3, column=4, sticky=tk.N+tk.E+tk.S+tk.W)  
        self.btnMp.grid(row=4, column=4, sticky=tk.N+tk.E+tk.S+tk.W)
        self.btnPrimo.grid(row=1, column=0, columnspan=3, sticky=tk.N+tk.E+tk.S+tk.W)
        self.btnBinario.grid(row=2, column=0, columnspan=3, sticky=tk.N+tk.E+tk.S+tk.W)
        self.btnData.grid(row=1, column=3, columnspan=2, rowspan=2, sticky=tk.N+tk.E+tk.S+tk.W)
        self.btnEqual.grid(row=5, column=4, rowspan=2, sticky=tk.N+tk.E+tk.S+tk.W)

    def bindButtons(self):
        for i in range(len(self.numBtns)):
            self.numBtns[i].bind('<Button-1>', self.btnPress)
        for i in range(len(self.opBtns)):
            self.opBtns[i].bind('<Button-1>', self.opPress)

        # self.btnAvg.bind('<Button-1>', self.avgPress)
        # self.btnPrimo.bind('<Button-1>', self.primoPress)
        # self.btnBinario.bind('<Button-1>', self.binarioPress)
        # self.btnData.bind('<Button-1>', self.dataPress)
        # self.btnMp.bind('<Button-1>', self.mpPress)
        # self.btnEqual.bind('<Button-1>', self.eqPress)
        # self.txtMain.bind('<KeyPress>', self.preventDefault)


    def btnPress(self, ev):
        if (ev.widget.cget("state") != tk.DISABLED):
            btnStr = ev.widget.cget('text')
            if btnStr.isdigit() or btnStr == '.':
                self.view.txtMain.insert(len(self.view.txtMain.get()), btnStr)
            
            if btnStr == "C":
                self.view.txtMain.delete(0,len(self.view.txtMain.get()))
                self.currentOperation = ""
                self.activateButtons()
    
    def activateButtons():
        pass
    def send_request(self, ev):
        result = self.business.send_request(ev, self.txtMain.get())
        self.txtMain.delete(0,len(self.txtMain.get()))
        self.txtMain.insert(0, result)

            

if __name__ == '__main__':
    ins = GUI()