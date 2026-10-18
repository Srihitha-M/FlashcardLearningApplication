import tkinter as tk
import random

# 1. Simple Data List
cards = [
    {"question": "Keyword to define function?", "answer": "def"},
    {"question": "Data type of 5.0?", "answer": "float"},
    {"question": "What does len([1, 2, 3]) return?", "answer": "3"},
    {"question": "What does 10 // 3 give?", "answer": "3"},
    {"question": "What does 10 % 3 give?", "answer": "1"},
    {"question": "Keyword to skip an iteration?", "answer": "continue"},
    {"question": "Method that runs on object creation?", "answer": "__init__"},
    {"question": "What refers to the current object?", "answer": "self"},
    {"question": "What is a blueprint for objects?", "answer": "class"},
    {"question": "What is a mutable sequence type?", "answer": "list"}
]
random.shuffle(cards)

# Simple tracking variables
current_card = 0
user_score = 0
looking_at_question = True  # True means front of card, False means back

# 2. Easy Functions
def click_card():
    global looking_at_question
    
    # If the quiz is finished, stop clicking
    if current_card >= len(cards):
        return
        
    if looking_at_question == True:
        # Flip to the back (Show Answer)
        card_button.config(text=cards[current_card]["answer"], bg="lightgreen", fg="green")
        looking_at_question = False
    else:
        # Flip to the front (Show Question)
        card_button.config(text=cards[current_card]["question"], bg="lightyellow", fg="black")
        looking_at_question = True

def click_next(is_correct):
    global current_card, user_score, looking_at_question
    
    if current_card >= len(cards):
        return
        
    if is_correct == True:
        user_score = user_score + 1
        
    current_card = current_card + 1
    looking_at_question = True  # Reset so the next card starts on the question side
    
    # Check if there are still cards left
    if current_card < len(cards):
        card_button.config(text=cards[current_card]["question"], bg="lightyellow", fg="black")
    else:
        # Finished screen
        card_button.config(text=f"Done!\n\nFinal Score: {user_score} / {len(cards)}", bg="lightblue", fg="green")
        # Hide the bottom buttons row completely so they can't be clicked
        button_frame.pack_forget()
        # Update instructions to show it's over
        top_label.config(text="", fg="green")

# 3. Big Window Setup for Laptops
my_window = tk.Tk()
my_window.title("Python Flashcard Quiz")
my_window.geometry("600x450")  # Much larger size for laptop screens

# --- CHANGED: Added a center frame container ---
main_center_frame = tk.Frame(my_window)
main_center_frame.pack(expand=True)

# Simple instruction text at the top
# --- CHANGED: master is now main_center_frame instead of my_window ---
top_label = tk.Label(main_center_frame, text="Click the card to flip between Question and Answer", font=("Arial", 12), fg="gray")
top_label.pack(pady=15)

# The Giant Flashcard Button
# --- CHANGED: master is now main_center_frame instead of my_window ---
card_button = tk.Button(main_center_frame, text=cards[current_card]["question"], 
                        font=("Arial", 18, "bold"), bg="lightyellow", fg="black", 
                        width=35, height=6, relief="ridge", wraplength=450,
                        command=click_card)
card_button.pack(pady=20)

# Frame to hold the bottom buttons side-by-side
# --- CHANGED: master is now main_center_frame instead of my_window ---
button_frame = tk.Frame(main_center_frame)
button_frame.pack(pady=10)

correct_button = tk.Button(button_frame, text="✔ Correct", font=("Arial", 14), bg="lightgreen", width=12, height=1, command=lambda: click_next(True))
correct_button.pack(side="left", padx=20)

wrong_button = tk.Button(button_frame, text="✖ Wrong", font=("Arial", 14), bg="lightcoral", width=12, height=1, command=lambda: click_next(False))
wrong_button.pack(side="left", padx=20)

my_window.mainloop()