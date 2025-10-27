import tkinter as tk
from tkinter import messagebox
import random


t = ("ROCK", "PAPER", "SCISSORS")
up = 0  
cp = 0  

def show_instructions():
    messagebox.showinfo(
        "📋 Game Instructions",
        "❌ To Remember:\n\n"
        "🪨 Rock beats ✂️ Scissors\n"
        "✂️ Scissors beat 📄 Paper\n"
        "📄 Paper beats 🪨 Rock\n\n"
        "🎮 Make your move wisely!"
    )


def start_game():
    for widget in root.winfo_children():
        widget.destroy()

    
    global score_label
    score_label = tk.Label(root, text=f"User: {up}  |  Computer: {cp}", anchor="e", justify="right")
    score_label.pack(anchor="ne", padx=10, pady=5)

   
    tk.Label(root, text="Make Your Move", font=("Helvetica", 14)).pack(pady=5)

    
    b_frame = tk.Frame(root)
    b_frame.pack(pady=10)
    tk.Button(b_frame, text="ROCK", width=12, command=lambda: play("ROCK")).grid(row=0, column=0, padx=5)
    tk.Button(b_frame, text="PAPER", width=12, command=lambda: play("PAPER")).grid(row=0, column=1, padx=5)
    tk.Button(b_frame, text="SCISSORS", width=12, command=lambda: play("SCISSORS")).grid(row=0, column=2, padx=5)

    
    global user_label, comp_label, result_label
    user_label = tk.Label(root, text="", fg="blue")
    user_label.pack(pady=2)
    comp_label = tk.Label(root, text="", fg="purple")
    comp_label.pack(pady=2)
    result_label = tk.Label(root, text="", fg="green")
    result_label.pack(pady=5)

    
    tk.Button(root, text="End Game", width=25, command=end_game).pack(side="bottom", pady=15)


def play(user_move):
    global up, cp
    comp_move = random.choice(t)

    
    user_label.config(text="You chose: " + user_move)
    comp_label.config(text="Computer chose: " + comp_move)

    
    if user_move == comp_move:
        result = "It's a tie!"
    elif (user_move == "ROCK" and comp_move == "SCISSORS") or \
         (user_move == "PAPER" and comp_move == "ROCK") or \
         (user_move == "SCISSORS" and comp_move == "PAPER"):
        up += 1
        result = "You won! 🥳"
    else:
        cp += 1
        result = "You lost! 😢"

    
    score_label.config(text=f"User: {up}  |  Computer: {cp}")
    result_label.config(text=result)


def end_game():
    for widget in root.winfo_children():
        widget.destroy()

    if up > cp:
        msg = "You Win! 🎉"
    elif cp > up:
        msg = "Computer Wins! 🤖"
    else:
        msg = "It's a Tie!"

    summary = f"Game Over!\n\nFinal Score:\nYou: {up}\nComputer: {cp}\n\n{msg}"
    tk.Label(root, text=summary, justify="center").pack(pady=40)
    tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x330")
root.option_add("*Font", "Helvetica 14")

label = tk.Label(root, text="Rock Paper Scissors", font=60)
label.pack(pady=20)

sb = tk.Button(root, text="Start Game", width=25, command=start_game)
sb.pack(side="top", pady=10, padx=20)

ib = tk.Button(root, text="Instructions", width=25, command=show_instructions)
ib.pack(side="top", pady=10, padx=20)

eb = tk.Button(root, text="Exit", width=25, command=root.destroy)
eb.pack(side="top", pady=10, padx=20)

root.mainloop()
