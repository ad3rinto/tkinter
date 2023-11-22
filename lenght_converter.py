
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(pady=20, padx=20)


def calculate():
    miles = int(user_input.get())
    kilo = round(miles * 1.6, 2)
    answer_label["text"] = kilo


user_input = Entry(width=7, font=("Arial", 24))
user_input.insert(END, "0")
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=("Arial", 24))
equal_label.grid(row=1, column=0)

answer_label = Label(text="0", font=("Arial", 24))
answer_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 24))
km_label.grid(row=1, column=2)

calculate_button = Button(text="Click Me", command=calculate)
calculate_button.grid(row=2, column=1)
window.mainloop()
