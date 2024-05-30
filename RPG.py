#RPG Keinzeit may/2024

import os
import time
import math

#Function to clear console
def clear(t = 2):
    print("Loading..."); 
    time.sleep(t);
    if os.name == "nt":
        os.system("cls");
    else:
        os.system("clear");

def startStats():
    #TODO make an object
    HP = 5;
    df = 2;
    atk = 1;
    exp = 0;

#Fills the HP bar with '=' acording to the current HP, it has 10 parts

def drawBar(name, totalHP, currentHP):
    bar = "";
    targetDraw = math.ceil(currentHP * 10 / totalHP);

    for i in range(10):
        if i < targetDraw:
            bar += "="
        else:
            bar += " "

    print(name + " HP\t[" + bar + "]");

#TODO attack function
#TODO enemy list

#main loop

finishGame = False;
playerName = input("Welcome to kzn's RPG\nWrite your name: ");
startStats();

while not finishGame:
    drawBar(playerName, 10, 10);
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
