from tkinter import Tk, StringVar
from tkinter.ttk import Frame, Entry, Button

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        self.entry_text = StringVar()
        self.entry = Entry(self, textvariable=self.entry_text)
        self.entry.grid(row=0, columnspan=4, sticky='we')

        cls = Button(self, text="cls", command=self.clear_entry)
        cls.grid(row=1, column=0)
        bck = Button(self, text="back", command=self.delete_last_char)
        bck.grid(row=1, column=1)
        lbl = Button(self, text="")
        lbl.grid(row=1, column=2)
        clo = Button(self, text="close", command=self.quit)
        clo.grid(row=1, column=3)
        
        sev = Button(self, text="7", command=lambda: self.append_to_entry("7"))
        sev.grid(row=2, column=0)
        eig = Button(self, text="8", command=lambda: self.append_to_entry("8"))
        eig.grid(row=2, column=1)
        nin = Button(self, text="9", command=lambda: self.append_to_entry("9"))
        nin.grid(row=2, column=2)
        div = Button(self, text="/", command=lambda: self.append_to_entry("/"))
        div.grid(row=2, column=3)
        
        fou = Button(self, text="4", command=lambda: self.append_to_entry("4"))
        fou.grid(row=3, column=0)
        fiv = Button(self, text="5", command=lambda: self.append_to_entry("5"))
        fiv.grid(row=3, column=1)
        six = Button(self, text="6", command=lambda: self.append_to_entry("6"))
        six.grid(row=3, column=2)
        mul = Button(self, text="*", command=lambda: self.append_to_entry("*"))
        mul.grid(row=3, column=3)
        
        one = Button(self, text="1", command=lambda: self.append_to_entry("1"))
        one.grid(row=4, column=0)
        two = Button(self, text="2", command=lambda: self.append_to_entry("2"))
        two.grid(row=4, column=1)
        thr = Button(self, text="3", command=lambda: self.append_to_entry("3"))
        thr.grid(row=4, column=2)
        mns = Button(self, text="-", command=lambda: self.append_to_entry("-"))
        mns.grid(row=4, column=3)
        
        zer = Button(self, text="0", command=lambda: self.append_to_entry("0"))
        zer.grid(row=5, column=0)
        dot = Button(self, text=".", command=lambda: self.append_to_entry("."))
        dot.grid(row=5, column=1)
        equ = Button(self, text="=", command=self.calculate)
        equ.grid(row=5, column=2)
        pls = Button(self, text="+", command=lambda: self.append_to_entry("+"))
        pls.grid(row=5, column=3)

        self.pack()

    def append_to_entry(self, value):
        self.entry_text.set(self.entry_text.get() + value)

    def clear_entry(self):
        self.entry_text.set("")

    def delete_last_char(self):
        self.entry_text.set(self.entry_text.get()[:-1])

    def calculate(self):
        try:
            result = eval(self.entry_text.get())
            self.entry_text.set(str(result))
        except:
            self.entry_text.set("Error")

root = Tk()
app = Calculator(root)
root.mainloop()