from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=400)
window.config(padx=60, pady=60)
# Creating a label
label_text = "win"
my_label = Label(text=label_text, font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

# Entry component
board_input = Entry(width=10)
board_input.insert(END, "Email: ")
board_input.grid(row=2, column=3)


def button_clicked():
    new_text = board_input.get()
    my_label["text"] = new_text


new_button = Button(text="New button", command=button_clicked)
new_button.grid(row=0, column=2)

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

window.mainloop()
