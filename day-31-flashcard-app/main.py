from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
words_data_frame = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_data_frame = original_data.to_dict(orient="records")
else:
    words_data_frame = data.to_dict(orient="records")

# ---------------------------- Create new flash card ------------------------------- #
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_data_frame)
    canvas.itemconfig(canvas_image, image=canvas_image_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)
# ---------------------------- Flip the flash card ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=canvas_image_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
# ---------------------------- Remove the known words from the list ------------------------------- #
def is_known():
    words_data_frame.remove(current_card)
    data = pandas.DataFrame(words_data_frame)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image_front = PhotoImage(file="./images/card_front.png")
canvas_image_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=canvas_image_front)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()


window.mainloop()
