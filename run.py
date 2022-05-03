# import pyfiglet module
import pyfiglet
import time
from random import randint

#Start Game
def startGame():

    shotgun = False
    gun = False
    score = 0
    
    welcome = pyfiglet.figlet_format("Walkers")
    print(welcome)
    print("A Zombie Apocalypse Text Adventure by Miriam Payne")
    name = input("Please confirm your name:\n")
    age = int(input("Please confirm your age:\n"))

    if age > 0 and age < 12:
        print("You're young ... chances of survival are slim ... use size and speed to your advantage")
    elif age >= 12 and age <75:
        print("You're going to need a good aim ... fair survival if you're a good shot")
    elif age >= 75:
        print("You're as slow as the walkers ... I hate to break it to you but your chances are slim")

    # time.sleep(1)
    input("Press Enter To Continue...")

    print("Mission: Survive or die trying")
    print("Chapter 1")

    print("You walk into an abandoned Dublin city center tower block car park")
    input("Press Enter To Continue...")

    print("A dodgy vaccine for the pandemic has turned 95% the population into a flesh eating zombies outbreak.")
    input("Press Enter To Continue...")

    print("Your sat nav shows you are 8 miles from a safe haven")
    input("Press Enter To Continue...")

    print("")
    print("A zombie horde appears... you grab your hurley from your backpack")

    input("Press Enter To Continue...")

    score = stage_one()
    score, shotgun = stage_two(score)
    score = stage_three(score, shotgun)

    if score > 1:
        print("Well done you win")
    else:
        print("You suck at this game")

    # win or lose function

    
# Define Function - Retry
def retry_game():
    # Ask user whether they want to retry

    # return True/False


# Step 1: Get first action
def stage_one():
    action = input("(F)ight or (R)un?\n").upper()
    while action not in ["FIGHT", "RUN", "F", "R"]:
        input("Press Enter To Continue...")
        print("That is not a valid action")
        action = input("Fight or Run?\n").upper()

    if action == "FIGHT":
        if age >= 12:
            print("Your youthfulness helps you avoid being chomped")
            input("Press Enter To Continue...")
            print("You made it this time")
            score = 2
        else:
            print("You attack")
            input("Press Enter To Continue...")
            print("A combination of old age and slow reactions cause you to be bitten")
            print("You're too old to be fighting zombies")
            score = 1
    elif action == "RUN":
        if age <=12:
            print("You run from the zombie, but are too slow")
            input("Press Enter To Continue...")
            print("This walker clearly has some agility left in them and catches up quick")
            score = 1
        else:
            print("You run from the zombie")
            input("Press Enter To Continue...")
            print("Your athletic legs carry you to safety")
            score = 2

    return score

# Step 2 only happens if you have survived with a score of 2 now
def stage_two(score):
    if score == 2:
        input("Press Enter To Continue...")
        print("Chapter 2: ... ") 
        input("Press Enter To Continue...")

        print("You come across an abandoned house, an old barn and a boarded-up store")

        input("Press Enter To Continue...")
        choice = input("Do you enter the house, barn or the store?\n").upper()

        while choice not in["HOUSE", "BARN", "STORE"]:
            input("Press Enter To Continue...")
            print("Sorry. I don't understand")
            choice = input("Do you enter the house or the barn or the store?\n").upper()

        if choice == "HOUSE":
            input("Press Enter To Continue...")
            print("You enter the house, rummaging around ... ")
            input("Press Enter To Continue...")
            print("You find a shot gun and three shot gun shells")
            input("Press Enter To Continue...")
            shotgun = True
            score = 3
        elif choice == "STORE":
            input("Press Enter To Continue...")
            print("You enter the store, rummaging around ... ")
            input("Press Enter To Continue...")
            print("You stock up on canned food, drink, first aid and find a gun with 4 bullets")
            input("Press Enter To Continue...")
            gun = True
            score = 3
        elif choice == "BARN":
            input("Press Enter To Continue...")
            print("You enter the barn where you could hear sounds of groaning ... ")
            input("Press Enter To Continue...")
            print("You encounter a mob of zombies")
            input("Press Enter To Continue...")
            print("You didn't survive")
        else:
            input("Press Enter To Continue...")
            print("You enter the store, climbing down the escalater you slip on some blood ... ")
            input("Press Enter To Continue...")
            print("You fall to your death")
            input("Press Enter To Continue...")
            print("You didn't survive")

    return (score, shotgun)

#Part 3 only happens if you have a score of 3 now
def stage_three(score, shotgun):
    if score == 3:
        input("Press Enter To Continue...")
        print("Chapter 3: ... ") 
        input("Press Enter To Continue...")

        print("You make it to the perimeter of the safe haven")
        input("Press Enter To Continue...")
        print("Only one problem ... ")
        input("Press Enter To Continue...")
        print("Two Zombies")
        input("Press Enter To Continue...")
        print("")
        input("Press Enter To Continue...")
        
        if shotgun:
            print("You have three shots to hit two targets")
            shots = 3
        else:
            print("You have four shots to hit two targets")
            shots = 4

        input("Press Enter To Continue...")
        zombies = 2
        while shots > 0 and zombies > 0:
            hit = randint(1, 3)

            if hit in [1, 2]:
                input("Press Enter To Continue...")
                print("A lucky shot, you killed a zombie")
                shots = shots - 1
                zombies = zombies - 1
            else:
                input("Press Enter To Continue...")
                print("You fire a shot, but miss")
                shots = shots - 1

        if zombies == 0:
            print("You made it!")
            score = 5
        else:
            print("You fired all your shots and now the zombies are moving closer")
            score = 4
    return score


# Step 0: Call main menu procedure
if __name__ == '__main__':
    
    while True:
        startGame()
        if not retry_game():
            exit(1)