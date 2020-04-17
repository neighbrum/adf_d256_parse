from TransactionParser import ADF
from TransactionParser import TSYS
from io import StringIO

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox

class App(Frame):
    def getFileName(self):
        self.file = askopenfile(mode ='r', filetypes =[('Draft256', '*.TSYS'),('ADF','*.ADF')])
        try:
            ext = self.file.name.split(".")[-1]
            self.file = StringIO(self.file.read().replace("\r","").replace("\n",""))
            for child in self.flat_view.winfo_children()+self.record_view.winfo_children()+self.text_view.winfo_children():
                child.destroy()
            if "TSYS" == ext:
                parser = TSYS.Parser(self.file)
                parser.parse()
                self._loadTSYSFile(parser)
            else:
                parser = ADF.Parser(self.file)
                parser.parse()
                self._loadADFFile(parser)
        except Exception as e:
            messagebox.showerror("File error", "File could not be opened")


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.file = None
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv.heading("#0", text='Flat File Viewer', anchor='w')
        tv.column("#0", anchor="w")
        tv.grid(sticky = (N,W,S))

        self.flat_view = tv
        
        tv = Treeview(self)
        tv.heading("#0", text='Record Viewer', anchor='w')
        tv.column("#0", anchor="w")
        tv.grid(row=0,column=1,sticky = (N,W,S))
        
        self.grid_rowconfigure(0, weight = 1)
        self.record_view = tv
        ta = Text(self)
        ta.grid(row=0,column=2,sticky = (N,E,W,S))
        self.text_view = ta
        self.grid_columnconfigure(2, weight = 1)

    def _loadTSYSFile(self, parsed):
        for sequence, record in parsed.records.items():
            flat_title = f'{sequence} {record.__class__.__name__}'
            print(flat_title)

    
    def _loadADFFile(self, parsed):
        parsed

    def LoadTable(self):
        self.flat_view.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))

def main():
    root = Tk()
    root.title("TransactionView")
    root.geometry(f'{int(root.winfo_screenwidth()/2)}x{int(root.winfo_screenheight()/3)}+0+0')

    app = App(root)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=lambda: app.getFileName())
    filemenu.add_command(label="Save", command=lambda x:None)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    
    
    root.mainloop()

if __name__ == '__main__':
    main()