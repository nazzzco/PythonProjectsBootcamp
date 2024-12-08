from tkinter import *

#Button
def button_clicked():
    input_entry = input.get()
    my_label["text"] = input_entry

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
#my_label.place(x=100, y=200)
my_label.config(padx=15, pady=15)
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
button_new = Button(text="New button", command=button_clicked)
button_new.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)



window.mainloop()
