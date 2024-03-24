print("Welcome to Rock-Paper-Scissor Game!")
print("Players please input your choice: rock, paper, or scissor.")
p1 = input("player 1: ")
p2 = input("player 2: ")

if p1 == p2:
        print("it's a tie!")
    
elif(p1=="rock" and p2=="scissor") or (p1=="scissor" and p2=="paper") or (p1=="paper" and p2=="rock"):
        print("Player1 Wins!")

elif(p2=="rock" and p1=="scissor") or (p2=="scissor" and p1=="paper") or (p2=="paper" and p1=="rock"):
        print("Player2 Wins!")