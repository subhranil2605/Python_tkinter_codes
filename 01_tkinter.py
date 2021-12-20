import tkinter as tk

window = tk.Tk()

x = tk.Label(text="ROUNAK")
x.pack()

y = tk.Label(
    text="Subhranil Sarkar",
    fg="#C97AF1",
    bg="#23DECD"
)
y.pack()

z = tk.Label(
    text="Rick",
    width=50,
    height=20,
    # bg= "red"
)

z.pack()

b = tk.Button(
    text="Click Me!",
    width=10,
    height=5,
    bg="red",
)
b.pack()

window.mainloop()