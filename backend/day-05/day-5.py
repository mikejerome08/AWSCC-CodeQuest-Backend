print("Welcome to Rock-Paper-Scissor Game!")
print("You are Player 1, please input your choice: rock, paper, or scissor.")
p1 = input("player 1: ").lower()

import random
list = ["rock", "paper", "scissor"]
computer_choice = random.choice(list)
print(f"player 2: {computer_choice}")

if p1 == computer_choice:
        print("it's a tie!")
    
elif(p1=="rock" and computer_choice=="scissor") or (p1=="scissor" and computer_choice=="paper") or (p1=="paper" and computer_choice=="rock"):
        print("Player1 Wins!")

elif(computer_choice=="rock" and p1=="scissor") or (computer_choice=="scissor" and p1=="paper") or (computer_choice=="paper" and p1=="rock"):
        print("Player2 Wins!")
