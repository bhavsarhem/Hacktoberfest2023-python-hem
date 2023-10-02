import tkinter as tk
from tkinter import messagebox
import random

# Initialize the game board
board = [[" " for _ in range(3)] for _ in range(3)]

# Variable to decide the turn of which player
sign = 0

def winner(b, l):
    return (
        (b[0][0] == l and b[0][1] == l and b[0][2] == l) or
        (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
        (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
        (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
        (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
        (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
        (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
        (b[0][2] == l and b[1][1] == l and b[2][0] == l)
    )

def isfree(i, j):
    return board[i][j] == " "

def isfull():
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_text(i, j):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            board[i][j] = "X"
        else:
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
        if winner(board, "X"):
            end_game("Player 1")
        elif winner(board, "O"):
            end_game("Player 2")
        elif isfull():
            end_game("Tie Game")
        elif single_player_mode.get() and sign % 2 != 0:
            make_computer_move()

def end_game(winner):
    messagebox.showinfo("Game Over", f"{winner} won the game!")
    root.destroy()

def make_computer_move():
    possible_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if possible_moves:
        i, j = random.choice(possible_moves)
        get_text(i, j)

def switch_mode():
    global sign
    sign = 0
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            button[i][j].config(text=" ", state=tk.NORMAL)

# Create the main GUI window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the game board
button = []
for i in range(3):
    button.append([])
    for j in range(3):
        button[i].append(tk.Button(root, text=" ", font=('normal', 20), height=2, width=5,
                                   command=lambda i=i, j=j: get_text(i, j)))
        button[i][j].grid(row=i, column=j)

# Create mode switch button
single_player_mode = tk.BooleanVar()
mode_button = tk.Checkbutton(root, text="Single Player", variable=single_player_mode, command=switch_mode)
mode_button.grid(row=3, columnspan=3)

root.mainloop()
