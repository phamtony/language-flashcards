from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- Flashcard SETUP ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

data_dic = data.to_dict(orient="records")
current_card = {}

def select_flash_cards():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dic)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=frontcard_img)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- Change Flashcard SETUP ------------------------------- #
def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=backcard_img)
    canvas.itemconfig(word, text=current_card['English'], fill="white")

# ---------------------------- Known Flashcards ------------------------------- #
def known():
    data_dic.remove(current_card)
    more_data = pandas.DataFrame(data_dic)
    more_data.to_csv("data/words_to_learn.csv", index=False)
    select_flash_cards()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Language Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
frontcard_img = PhotoImage(file="images/card_front.png")
backcard_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=frontcard_img)
canvas.grid(row=0, column=0, columnspan=2)

title = canvas.create_text(400, 150, fill="black", text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, fill="black", text="Word", font=("Ariel", 60, "italic"))

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, bd=0, command=known)
right_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bd=0, command=select_flash_cards)
wrong_button.grid(row=1, column=0)

select_flash_cards()

window.mainloop()