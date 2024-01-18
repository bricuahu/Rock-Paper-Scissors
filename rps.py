#Rock Paper Scissors game 

import random 


player = input("Do you want to play Rock, Paper, Scissors, Lizard, or Spock?")

player = str(input("Rock, Paper, Scissors, Lizard, or Spock? "))
computer = random.randint(1,5)

if computer == 1:
    computer = "Rock"
elif computer == 2:
    computer = "Paper"
elif computer == 3:
    computer = "Scissors"
elif computer == 4:
    computer = "Lizard"
elif computer == 5:
    computer = "Spock"

print("I choose:", computer)

if player == computer: 
    print("Tie")
elif (player == "Rock" and computer == "Scissors") or (player == "Scissors" and computer == "Paper") or (player == "Paper" and computer == "Rock") or (player == "Lizard" and computer == "Spock") or (player == "Lizard" and computer == "Paper") or (player == "Spock" and computer == "Rock") or (player == "Spock" and computer == "Scissors"):
    print("You Win :( ")
else: 
    print("You Lose :) ")