import tkinter as tk


class Vista:
    def __init__(self):
        window = tk.Tk()
        window.geometry('300x300')
        window.title('MVC Calculator')

        #Stablish the grid
        for i in range(7):
            window.rowconfigure(i, weight=1)

        for i in range(5):
            window.columnconfigure(i, weight=1)

        # Creating all the widgets
        self.txtMain     = tk.Entry(window, justify=tk.RIGHT)
        self.numBtns     = [ tk.Button(window, text=str(x)) for x in (["C", "0", "."] + list(range(1,10)))]
        self.opBtns      = [ tk.Button(window, text=str(x)) for x in ["/", "*", "-", "+"]]
        self.btnAvg      = tk.Button(window, text="Avg")
        self.btnPrimo    = tk.Button(window, text="Primo")
        self.btnBinario  = tk.Button(window, text="Binario")
        self.btnData     = tk.Button(window, text="Data")
        self.btnMp       = tk.Button(window, text="M+")
        self.btnEqual    = tk.Button(window, text="=")

        self.placeWidgets()
        self.bindWidgets()

        window.mainloop()

    
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


    def bindWidgets(self):
        for i in range(len(self.numBtns)):
            self.numBtns[i].bind('<Button-1>', self.btnPress)
        for i in range(len(self.opBtns)):
            self.opBtns[i].bind('<Button-1>', self.btnPress)

        self.btnAvg.bind('<Button-1>', self.btnPress)
        self.btnPrimo.bind('<Button-1>', self.btnPress)
        self.btnBinario.bind('<Button-1>', self.btnPress)
        self.btnData.bind('<Button-1>', self.btnPress)
        self.btnMp.bind('<Button-1>', self.btnPress)
        self.btnEqual.bind('<Button-1>', self.btnPress)


    def btnPress(self, ev):
        btnStr = ev.widget.cget('text')
        if btnStr.isdigit() or btnStr == '.':
            self.txtMain.insert(len(self.txtMain.get()), btnStr)
        elif btnStr in "/*-+":
            self.btnEqual.invoke()
            self.num1 = float(self.txtMain.get())
            self.op = btnStr
            self.txtMain.delete(0,len(self.txtMain.get()))
        elif btnStr == '=':
            self.num2 = float(self.txtMain.get())
            # do operation
            

if __name__ == '__main__':
    ins = Vista()