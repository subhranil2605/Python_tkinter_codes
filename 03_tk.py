from tkinter import *

window = Tk()

x_label = Label(text="x")
x_label.pack()

x_entry = Entry()
x_entry.pack()


y_label = Label(text="y")
y_label.pack()

y_entry = Entry()
y_entry.pack()


def mult():
    x = int(x_entry.get())
    y = int(y_entry.get())
    result = x * y
    result_label.config(text=result)


add_button = Button(text="*", command=mult)
add_button.pack()

result_label = Label(text="")
result_label.pack()

window.mainloop()

