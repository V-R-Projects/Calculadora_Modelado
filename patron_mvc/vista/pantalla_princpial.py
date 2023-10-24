import tkinter as tk

window = tk.Tk()
window.geometry('300x300')
window.title('MVC Calculator')

#Stablish the grid
for i in range(7):
    window.rowconfigure(i, weight=1)

for i in range(5):
    window.columnconfigure(i, weight=1)

# Button functions
def btnPress(ev):
    print(ev.widget.cget('text'))


# Creating all the widgets
txtMain     = tk.Entry(window, justify=tk.RIGHT)
numBtns     = [ tk.Button(window, text=str(x)) for x in (["0", "C", "."] + list(range(1,10)))]
opBtns      = [ tk.Button(window, text=str(x)) for x in ["/", "*", "-", "+"]]
btnAvg      = tk.Button(window, text="Avg")
btnPrimo    = tk.Button(window, text="Primo")
btnBinario  = tk.Button(window, text="Binario")
btnData     = tk.Button(window, text="Data")
btnMp       = tk.Button(window, text="M+")
btnEqual    = tk.Button(window, text="=")

# Placing and binding the widgets
txtMain.grid(row=0, column=0, columnspan=5, sticky=tk.N+tk.E+tk.S+tk.W)

for i in range(len(numBtns)):
    numBtns[i].grid(row=(6-i//3), column=i%3, sticky=tk.N+tk.E+tk.S+tk.W)
    numBtns[i].bind('<Button-1>', btnPress)

for i in range(len(opBtns)):
    opBtns[i].grid(row=3+i, column=3, sticky=tk.N+tk.E+tk.S+tk.W)
    opBtns[i].bind('<Button-1>', btnPress)

btnAvg.bind('<Button-1>', btnPress)
btnPrimo.bind('<Button-1>', btnPress)
btnBinario.bind('<Button-1>', btnPress)
btnData.bind('<Button-1>', btnPress)
btnMp.bind('<Button-1>', btnPress)
btnEqual.bind('<Button-1>', btnPress)

btnAvg.grid(row=3, column=4, sticky=tk.N+tk.E+tk.S+tk.W)  
btnMp.grid(row=4, column=4, sticky=tk.N+tk.E+tk.S+tk.W)
btnPrimo.grid(row=1, column=0, columnspan=3, sticky=tk.N+tk.E+tk.S+tk.W)
btnBinario.grid(row=2, column=0, columnspan=3, sticky=tk.N+tk.E+tk.S+tk.W)
btnData.grid(row=1, column=3, columnspan=2, rowspan=2, sticky=tk.N+tk.E+tk.S+tk.W)
btnEqual.grid(row=5, column=4, rowspan=2, sticky=tk.N+tk.E+tk.S+tk.W)

window.mainloop()