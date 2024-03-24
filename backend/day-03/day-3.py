ans1 = input("A man is asking for shelter. Do you let him in (yes or no)?: ")

if ans1 == "yes":
    print("Police arrived & asked wether thief is inside")
    ans2 = input("Do you tell them the truth (yes or no)?: ")

    if ans2 == "yes":
        print("You win!")
              
    if ans2 == "no":
        print("Game Over")

if ans1 == "no":
    print("He attacked on you.")
    ans3 = input("Will you knock him down (yes or no)?: ")

    if ans3 == "yes":
        print("You win!")

    if ans3 == "no":
        print("Game Over")