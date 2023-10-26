import tkinter as tk

class Controller:

    def __init__(self, model_, view_):
        self.model = model_
        self.view = view_
        self.actualOperation = ""
        self.operationsDict = {
            "+": self.model.realizar_suma,
            "-": self.model.realizar_resta,
            "*": self.model.realizar_multiplicacion,
            "/": self.model.realizar_division
        }

        self.bindButtons()
        self.view.window.mainloop()

    def bindButtons(self):
        for i in range(len(self.view.numBtns)):
            self.view.numBtns[i].bind('<Button-1>', self.btnPress)
        for i in range(len(self.view.opBtns)):
            self.view.opBtns[i].bind('<Button-1>', self.opPress)

        # self.view.btnAvg.bind('<Button-1>', )
        # self.view.btnPrimo.bind('<Button-1>', )
        # self.view.btnBinario.bind('<Button-1>', )
        # self.view.btnData.bind('<Button-1>', )
        self.view.btnMp.bind('<Button-1>', self.mpPress)
        self.view.btnEqual.bind('<Button-1>', self.eqPress)

    def deactivateButtons(self):
        for i in range(1,len(self.view.numBtns)):
            self.view.numBtns[i].config(state = tk.DISABLED)
        for i in range(len(self.view.opBtns)):
            self.view.opBtns[i].config(state = tk.DISABLED)

        self.view.btnAvg.config(state = tk.DISABLED)
        self.view.btnPrimo.config(state = tk.DISABLED)
        self.view.btnBinario.config(state = tk.DISABLED)
        self.view.btnData.config(state = tk.DISABLED)
        self.view.btnMp.config(state = tk.DISABLED)
        self.view.btnEqual.config(state = tk.DISABLED)

    def activateButtons(self):
        for i in range(1,len(self.view.numBtns)):
            self.view.numBtns[i].config(state = tk.NORMAL)
        for i in range(len(self.view.opBtns)):
            self.view.opBtns[i].config(state = tk.NORMAL)

        self.view.btnAvg.config(state = tk.NORMAL)
        self.view.btnPrimo.config(state = tk.NORMAL)
        self.view.btnBinario.config(state = tk.NORMAL)
        self.view.btnData.config(state = tk.NORMAL)
        self.view.btnMp.config(state = tk.NORMAL)
        self.view.btnEqual.config(state = tk.NORMAL)

    def printResultado(self):
        self.view.txtMain.delete(0,len(self.view.txtMain.get()))
        self.view.txtMain.insert(0,self.model.get_resultado())

    def btnPress(self, ev):
        if (ev.widget.cget("state") != tk.DISABLED):
            btnStr = ev.widget.cget('text')
            if btnStr.isdigit() or btnStr == '.':
                self.view.txtMain.insert(len(self.view.txtMain.get()), btnStr)
            
            if btnStr == "C":
                self.view.txtMain.delete(0,len(self.view.txtMain.get()))
                self.activateButtons()
    
    def opPress(self, ev):
        if (ev.widget.cget("state") != tk.DISABLED):
            opStr = ev.widget.cget('text')
            self.actualOperation = opStr

            num = self.view.txtMain.get()
            self.model.set_num1(float(num))
            self.view.txtMain.delete(0,len(self.view.txtMain.get()))

    
    def eqPress(self, ev):
        if (ev.widget.cget("state") != tk.DISABLED):
            num = self.view.txtMain.get()
            self.model.set_num2(float(num))
            self.operationsDict[self.actualOperation]()
            self.printResultado()
    
    def mpPress(self, ev):
        if (ev.widget.cget("state") != tk.DISABLED):
            self.deactivateButtons()
            self.model.guardar_memoria()
            self.printResultado()

        
        