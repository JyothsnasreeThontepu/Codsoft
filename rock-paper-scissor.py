import random
r1 = random.choice(["Rock", "Paper", "Scissors"])
player_choice = input("Choose Rock, Paper, or Scissors: ")
computer_choice = r1
print("You chose: ", player_choice)
print("Computer chose: ", computer_choice)
if((player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scissors" and computer_choice == "Paper")):
    print("You win!")
elif(player_choice == computer_choice):
    print("Its a tie")
else:
     print("Computer wins!")