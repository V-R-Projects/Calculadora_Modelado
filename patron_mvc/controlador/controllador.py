

class Controller:

    def __init__(self, model_, view_):
        self.model = model_
        self.view = view_

    def bindButtons(self):
        for i in range(len(self.view.numBtns)):
            self.view.numBtns[i].bind('<Button-1>', self.btnPress)
        for i in range(len(self.view.opBtns)):
            self.view.opBtns[i].bind('<Button-1>', )

        self.view.btnAvg.bind('<Button-1>', )
        self.view.btnPrimo.bind('<Button-1>', )
        self.view.btnBinario.bind('<Button-1>', )
        self.view.btnData.bind('<Button-1>', )
        self.view.btnMp.bind('<Button-1>', )
        self.view.btnEqual.bind('<Button-1>', )

    def btnPress(self, ev):
        btnStr = ev.widget.cget('text')
        if btnStr.isdigit() or btnStr == '.':
            self.view.txtMain.insert(len(self.view.txtMain.get()), btnStr)
        