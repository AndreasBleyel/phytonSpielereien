import tkinter as tk
import tkinter.messagebox as mb

w = tk.Tk()
w.title("Calculator")
w.geometry("400x125")
w.resizable(False,False)

tk.Label(w, text ="Input Number 1:").place(row=0, column=0,  padx=(5,5), pady=(5,5))
e1 = tk.Entry(w)
e1.grid(row=0, column=1, columnspan = 4)

tk.Label(w, text ="Input Number 2:").grid(row=1, column=0, padx=(5,5), pady=(5,5) )
e2 = tk.Entry(w)
e2.grid(row=1, column=1, columnspan = 4)

tk.Label(w, text ="Result:").grid(row=3, column=0, padx=(5,5), pady=(5,5))
res = tk.Entry(w)
res.grid(row=3, column=1, columnspan = 4)

def plus():
    try:
        numb1 = float(e1.get())
        numb2 = float(e2.get())
        res.delete(0, "end")
        res.insert(0,numb1+numb2)
    except ValueError:
        mb.showerror("Error", "Nur Zahlen eingeben. Punkt für Komma")
    return
def minus():
    try:
        numb1 = float(e1.get())
        numb2 = float(e2.get())
        res.delete(0, "end")
        res.insert(0,numb1-numb2)
    except ValueError:
        mb.showerror("Error", "Nur Zahlen eingeben. Punkt für Komma")
    return
def mal():
    try:
        numb1 = float(e1.get())
        numb2 = float(e2.get())
        res.delete(0, "end")
        res.insert(0,numb1*numb2)
    except ValueError:
        mb.showerror("Error", "Nur Zahlen eingeben. Punkt für Komma")
    return
def div():
    try:
        numb1 = float(e1.get())
        numb2 = float(e2.get())
        res.delete(0, "end")
        res.insert(0,numb1/numb2)
    except ValueError:
        mb.showerror("Error", "Nur Zahlen eingeben. Punkt für Komma")
    return

b_plus = tk.Button(w, text="+", command=plus, width=5).grid(row=2,column=1)
b_minus = tk.Button(w, text="-", command=minus, width=5).grid(row=2,column=2)
b_mal = tk.Button(w, text="*", command=mal, width=5).grid(row=2,column=3)
b_div = tk.Button(w, text="/", command=div, width=5).grid(row=2,column=4)


w.mainloop()
