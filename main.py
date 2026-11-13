from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Simple GUI")
root.geometry("400x300")

my_label = Label(root, text="Right click to see the menu", font=("Helvetica", 16))
my_label.pack(pady=50)


def hello():
    messagebox.showinfo("Hello", "Hello World")
def goodbye():
    messagebox.showinfo("Goodbye", "Goodbye")
def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)
my_menu = Menu(root, tearoff=0)
my_menu.add_command(label="Exit", command=root.quit)
my_menu.add_separator()
my_menu.add_command(label="Say Hello", command=hello)
my_menu.add_command(label="Say Good-bye", command=goodbye)
root.bind("<Button-3>", my_popup)










root.mainloop()