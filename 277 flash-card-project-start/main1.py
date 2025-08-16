from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

# ---------------- Load Data ---------------- #
if os.path.exists("./data/words_to_learn.csv"):
    data = pandas.read_csv("./data/words_to_learn.csv")
else:
    data = pandas.read_csv("./data/french_words.csv")

word_list = data.to_dict(orient="records")  # [{'French': 'chaque', 'English': 'each'}, ...]

current_card = {}
flip_timer = None

# ---------------- Functions ---------------- #
def next_word():
    """Show a random French word"""
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)

    if len(word_list) == 0:
        canvas.itemconfig(card_title, text="Done!", fill="black")
        canvas.itemconfig(card_word, text="All words learned 🎉", fill="black")
        return

    current_card = random.choice(word_list)
    canvas.itemconfig(canvas_bg, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip)

def flip():
    """Flip to English translation"""
    canvas.itemconfig(canvas_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def known_word():
    """Remove known word and save to words_to_learn.csv"""
    word_list.remove(current_card)
    new_data = pandas.DataFrame(word_list)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_word()

# ---------------- UI Setup ---------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_bg = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_word)
right_button.grid(row=1, column=1)

# Start
next_word()

window.mainloop()

