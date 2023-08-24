import random
list=["rock","paper","scissors"]
user_choice=int(input("what is your choice?,type 0 for rock,type 1 for paper,type 2 for scissors"))
computer_choice=random.randint(0,2)
print(f"Computer choosses {computer_choice}")
if computer_choice>user_choice:
    print("computer won the game")
elif computer_choice==user_choice:
    print("play one more time")
else:
    print("You won the game")
