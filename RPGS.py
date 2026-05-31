import customtkinter as ctk
import random
from playsound import playsound
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
rounds_to_win = 2  # default is best of 3


def play_sound(file):
    threading.Thread(target=lambda: playsound(file), daemon=True).start()


def get_computer_choice():
    return random.choice(choices)


def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"


def start_round(user_choice):
    global user_score, computer_score

    result_label.configure(text="🤖 Computer is choosing...", text_color="yellow")

    root.after(1200, lambda: finish_round(user_choice))


def finish_round(user_choice):
    global user_score, computer_score

    computer_choice = get_computer_choice()

    user_label.configure(text=f"You: {user_choice.upper()}")
    comp_label.configure(text=f"Computer: {computer_choice.upper()}")

    result = decide_winner(user_choice, computer_choice)

    if result == "tie":
        result_label.configure(text="🤝 It's a Tie!", text_color="white")
        play_sound("C:\\Users\\MY\\Downloads\\click.mp3.wav")

    elif result == "user":
        user_score += 1
        result_label.configure(text="🎉 You Win!", text_color="green")
        play_sound("C:\\Users\\MY\\Downloads\\win.mp3.mp3")

    else:
        computer_score += 1
        result_label.configure(text="💻 Computer Wins!", text_color="red")
        play_sound("C:\\Users\\MY\\Downloads\\lose.mp3.mp3")

    score_label.configure(text=f"Score → You: {user_score} | Computer: {computer_score}")

    check_game_over()


def check_game_over():
    global user_score, computer_score

    if user_score == rounds_to_win:
        result_label.configure(text="🏆 You Won the Match!", text_color="green")
        disable_buttons()

    elif computer_score == rounds_to_win:
        result_label.configure(text="💀 Computer Won the Match!", text_color="red")
        disable_buttons()


def disable_buttons():
    rock_btn.configure(state="disabled")
    paper_btn.configure(state="disabled")
    scissors_btn.configure(state="disabled")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_label.configure(text="You: -")
    comp_label.configure(text="Computer: -")
    result_label.configure(text="Choose your move!", text_color="white")
    score_label.configure(text="Score → You: 0 | Computer: 0")

    rock_btn.configure(state="normal")
    paper_btn.configure(state="normal")
    scissors_btn.configure(state="normal")


def set_mode(mode):
    global rounds_to_win
    if mode == 3:
        rounds_to_win = 2
        mode_label.configure(text="Mode: Best of 3")
    else:
        rounds_to_win = 3
        mode_label.configure(text="Mode: Best of 5")
    reset_game()


# GUI Setup
root = ctk.CTk()
root.title("Rock Paper Scissors Pro")
root.geometry("500x450")

title = ctk.CTkLabel(root, text="🎮 Rock Paper Scissors", font=("Arial", 20, "bold"))
title.pack(pady=10)

mode_label = ctk.CTkLabel(root, text="Mode: Best of 3", font=("Arial", 12))
mode_label.pack()

mode_frame = ctk.CTkFrame(root)
mode_frame.pack(pady=5)

ctk.CTkButton(mode_frame, text="Best of 3", command=lambda: set_mode(3)).grid(row=0, column=0, padx=5)
ctk.CTkButton(mode_frame, text="Best of 5", command=lambda: set_mode(5)).grid(row=0, column=1, padx=5)

user_label = ctk.CTkLabel(root, text="You: -", font=("Arial", 14))
user_label.pack()

comp_label = ctk.CTkLabel(root, text="Computer: -", font=("Arial", 14))
comp_label.pack()

result_label = ctk.CTkLabel(root, text="Choose your move!", font=("Arial", 16))
result_label.pack(pady=10)

score_label = ctk.CTkLabel(root, text="Score → You: 0 | Computer: 0", font=("Arial", 14))
score_label.pack(pady=5)

btn_frame = ctk.CTkFrame(root)
btn_frame.pack(pady=20)

rock_btn = ctk.CTkButton(btn_frame, text="🪨 Rock", width=100, command=lambda: start_round("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = ctk.CTkButton(btn_frame, text="📄 Paper", width=100, command=lambda: start_round("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = ctk.CTkButton(btn_frame, text="✂️ Scissors", width=100, command=lambda: start_round("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

reset_btn = ctk.CTkButton(root, text="Reset Game", command=reset_game, fg_color="gray")
reset_btn.pack(pady=10)

root.mainloop()