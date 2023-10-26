import tkinter as tk


class View:
    def __init__(self):
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

            

if __name__ == '__main__':
    ins = View()