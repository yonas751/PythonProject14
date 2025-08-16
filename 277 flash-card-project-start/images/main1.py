from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Sample data
dict1 = [("partie", "part"), ("chien", "dog"), ("maison", "house")]

# --- Canvas setup ---
canvas = Canvas(width=900, height=626, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="card_front.png")
canvas_bg = canvas.create_image(450, 313, image=card_front_img)

card_title = canvas.create_text(450, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(450, 313, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# --- Functions ---
def random_word():
    french, english = random.choice(dict1)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french)

# --- Buttons ---
wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")

wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, command=random_word, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=1)

# Start
random_word()
window.mainloop()
