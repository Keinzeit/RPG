#RPG Keinzeit may/2024

import os
import time

#Function to clear console
def clear(t = 2):
    print("Loading..."); 
    time.sleep(t);
    if os.name == "nt":
        os.system("cls");
    else:
        os.system("clear");

def startStats():
    HP = 5;
    df = 2;
    atk = 1;
    exp = 0;

#main loop

finishGame = False;

playerName = input("Welcome to kzn's RPG\nWrite your name: ");
startStats();

while not finishGame:
    playerAction = input("Choose your action:\tAttack\t Finish\n");
    playerAction = playerAction.strip().lower();
    
    if playerAction == "finish":
        finishGame = True;
        print("You chose to", playerAction);
    elif playerAction == "attack":
        print("You chose to", playerAction);
    else:
        print("Invalid action\nChoose other option");
        clear();
    
print("Thank you for playing");

clear(3);
