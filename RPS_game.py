"""
Rock, Paper, Scissors Game

This program implements a simple Rock, Paper, Scissors game using Tkinter GUI library.
Players can choose between rock, paper, or scissors and compete against the computer.

Author: Khaled AHMED

"""

from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Create the main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# Load images for user and computer choices
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# Insert picture labels for user and computer choices
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Create score labels for player and computer
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# Create indicators for user and computer
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Create message label
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# Function to update message
def updateMessage(x):
    msg['text'] = x

# Function to update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# Function to update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# Function to check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass

# List of choices
choices = ["rock", "paper", "scissor"]

# Function to update choices
def updateChoice(x):
    # Generate random choice for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # Update user choice label
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    # Check winner
    checkWin(x, compChoice)

# Create buttons for player choices
rock = Button(root, width=20, height=2, text="ROCK", fg="white", command=lambda: updateChoice("rock"))
rock.configure(bg="#3498db")  # Set background color
rock.grid(row=2, column=1)

paper = Button(root, width=20, height=2, text="PAPER", fg="white", command=lambda: updateChoice("paper"))
paper.configure(bg="#2ecc71")  # Set background color
paper.grid(row=2, column=2)

scissor = Button(root, width=20, height=2, text="SCISSOR", fg="white", command=lambda: updateChoice("scissor"))
scissor.configure(bg="#e74c3c")  # Set background color
scissor.grid(row=2, column=3)

# Run the main loop
root.mainloop()
