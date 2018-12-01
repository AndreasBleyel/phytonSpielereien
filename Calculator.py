import tkinter as tk
import tkinter.messagebox as mb

w = tk.Tk()
w.title("Calculator")
w.geometry("365x125")
w.resizable(False,False)

tk.Label(w, text ="Input Number 1:").place(width= 125, height=20, x=5, y=5)
e1 = tk.Entry(w)
e1.place(width=235, height=20 , x=125, y=5 )

tk.Label(w, text ="Input Number 2:").place(width= 125, height=20, x=5, y=25)
e2 = tk.Entry(w)
e2.place(width=235, height=20 , x=125, y=25 )

tk.Label(w, text ="Result:").place(width= 70, height=20, x= 5, y= 85)
res = tk.Entry(w)
res.place(width= 235, height=20, x=125, y =85, )

def plus():
    try:
        numb1 = float(e1.get())
        numb2 = float(e2.get())
        res.delete(0, "end")
        res.insert(0,numb1+numb2)
    except ValueError:
        mb.showerror("Error", "Nur Zahlen eingeben. Punkt für Komma")

def minus():
    try:
        numb1 = float(e1.get())
        numb2 = float(e2.get())
        res.delete(0, "end")
        res.insert(0,numb1-numb2)
    except ValueError:
        mb.showerror("Error", "Nur Zahlen eingeben. Punkt für Komma")

def mal():
    try:
        numb1 = float(e1.get())
        numb2 = float(e2.get())
        res.delete(0, "end")
        res.insert(0,numb1*numb2)
    except ValueError:
        mb.showerror("Error", "Nur Zahlen eingeben. Punkt für Komma")

def div():
    try:
        numb1 = float(e1.get())
        numb2 = float(e2.get())
        res.delete(0, "end")
        res.insert(0, numb1 / numb2)
    except (ValueError, ZeroDivisionError) as e:
        if isinstance(e, ValueError):
            mb.showerror("Error", "Nur Zahlen eingeben. Punkt für Komma")
        else:
            mb.showerror("Error", "Division durch 0")


b_plus = tk.Button(w, text="+", command=plus).place(width= 90, height=30 , x=5, y=50)
b_minus = tk.Button(w, text="-", command=minus).place(width= 90, height=30, x=95, y=50)
b_mal = tk.Button(w, text="*", command=mal).place(width= 90, height=30, x=185, y=50)
b_div = tk.Button(w, text="/", command=div).place(width= 90, height=30, x=275, y=50)


w.mainloop()
