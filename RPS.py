import random

def get_choices():
    player_choice=input("Enter a choice(rock,paper,scissors): ")
    options = ["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices
def check_win(computer,player):
    if computer==player :
        return "draw"
    elif computer=="rock":
        if player=="paper":
            return "player won"
        else:
            return "computer won"
    elif computer=="paper":
        if player=="scissors":
            return "player won"
        else:
            return "computer won"
    elif computer=="scissors":
        if player=="rock":
            return "player won"
        else:
            return "computer won"
choices=get_choices()
p_choice=choices["player"]
c_choice=choices["computer"]
print("\nYou played "+p_choice+", computer played "+c_choice+"\n")
print(check_win(c_choice,p_choice))
