from tkinter import *

#Button
def button_clicked():
    input_entry = input.get()
    converted_input = round(float(input_entry) * 1.60934)
    result["text"] = converted_input

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=350, height=180)
window.config(padx=20, pady=20)

#Label
miles_label = Label(text="Miles")
miles_label.config(padx=15, pady=15)
miles_label.grid(column=3, row=0)
result = Label(text="0")
result.grid(column=1, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.config(padx=15, pady=15)
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.config(padx=15, pady=15)
km_label.grid(column=3, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()