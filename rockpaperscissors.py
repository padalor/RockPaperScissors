'''
Created on Feb 1, 2020

@author: ITAUser
'''

import random 


keepPlaying = True

print("Welcome!")
print("First to 2 wins. Press q to quit.")
    

comp_wins = 0
player_wins = 0
    
def Choose_option():
    user_choice= input ("Choose Rock, Paper or Scissors")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again")
        Choose_option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint (1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice 

    print("Welcome!")
while True:
    print("")
    user_choice = Choose_option()
    comp_choice = Computer_Option()

    print("")
    
    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")
            
    elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1
            
    elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_wins += 1
        
        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")
            
            
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1
        
        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            player_wins += 1
            
        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")
        
    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")
    
    if (user_choice == 2):
        print("You Win!")
    
    if (comp_choice == 2):
        print("You Lose!")
        
    user_choice = input("Do you want to play again? (y/n/q)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    if user_choice in ["N", "n", "no", "No"]:
        break
    elif user_choice in ["q", "Q", "quit", "Quit"]:
        break
    
    