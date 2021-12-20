import tkinter as tk

window = tk.Tk()
name = tk.Label(text="Enter your number")
name.pack()

e = tk.Entry()
e.pack()


def d():
    d=e.get()
    print(d)

b = tk.Button(text="Show" , command=d)
b.pack()



window.mainloop()