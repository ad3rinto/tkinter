from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=400)

# Creating a label
label_text = "win"
my_label = Label(text=label_text, font=("Arial", 24, "bold"))
my_label.pack()

# Entry component
board_input = Entry(width=10)
board_input.pack()


def button_clicked():
    new_text = board_input.get()
    my_label["text"] = new_text


button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
