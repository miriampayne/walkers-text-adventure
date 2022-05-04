# import random
from random import randint

# import pyfiglet module
import pyfiglet


def start_game():
    """
    This function is called when the player is
    at start of game and includes Intro.
    """
    shotgun = False
    gun = False
    score = 0

    welcome = pyfiglet.figlet_format("Walkers", justify="center")
    print(welcome)
    print("Zombie Apocalypse Text Adventure Game".center(80) + "\n")
    print("Created by Miriam Payne".center(80) + "\n")
    name = input("Please confirm your name:\n")
    age = int(input("Please confirm your age:\n"))

    if age > 0 and age < 12:
        print("You're young ... chances of survival are slim ... ")
    elif age >= 12 and age < 75:
        print("I hope you're a good shot")
    elif age >= 75:
        print("You're as slow as the walkers ... chances are slim")

    input("Press Enter To Continue...\n")
    print("Mission: Survive or die trying")
    print("Chapter 1")
    input("Press Enter To Continue...\n")
    print("You walk into an abandoned Dublin city center tower block car park")
    input("Press Enter To Continue...\n")
    print("Outbreak has turned 95% the population into zombies aka walkers")
    input("Press Enter To Continue...\n")
    print("Your sat nav shows you are 8 miles from a safe haven")
    input("Press Enter To Continue...\n")
    print("")
    print("A zombie horde appears... you grab your hurley from your backpack")
    input("Press Enter To Continue...\n")

    score = stage_one(age)
    score, shotgun = stage_two(score)
    score = stage_three(score, shotgun)


def win(score):
    """
    This function is
    called when the player wins!
    """
    win = pyfiglet.figlet_format("WINNER", font="digital")
    if score >= 5:
        print(win)
    else:
        print("You're a bit rubbish at this game, better luck next time!")


def retry_game():
    """
    This function is called when the player is
    offered a retry of the game.
    """
    print("Would you like to go again? Reply (Y)ES or (N)O")
    answer = input("").lower().strip()
    while answer not in [YES, NO, Y, N]:
        print(
            "Invalid input. Please try again.", 2
            )
        answer = input("").lower().strip()
    if answer in [YES, Y]:
        print("Great! lets go again.", 2)
        retry_game()
    elif answer in [NO, N]:
        print("See you again next time!", 2)


def stage_one(age):
    """
    This function is called
    for user input to stay and fight
    or to run and hide, score depends on age.
    """
    action = input("(F)ight or (R)un?\n").upper()
    while action not in ["FIGHT", "RUN", "F", "R"]:
        input("Press Enter To Continue...\n")
        print("That is not a valid action")
        action = input("Fight or Run?\n").upper()

    if action == "FIGHT" or action == 'F':
        if age >= 12:
            print("Your youthfulness helps you avoid being chomped")
            input("Press Enter To Continue...\n")
            print("You made it this time")
            score = 2
        else:
            print("You attack")
            input("Press Enter To Continue...\n")
            print("Combo of old age and slowness cause you to be bitten")
            print("You're too old to be fighting zombies")
            score = 1
    elif action == "RUN" or action == 'R':
        if age <= 12:
            print("You run from the zombie, but are too slow")
            input("Press Enter To Continue...\n")
            print("This walker has some agility and catches up quick")
            score = 1
        else:
            print("You run from the zombie")
            input("Press Enter To Continue...\n")
            print("Your athletic legs carry you to safety")
            score = 2

    return score


def stage_two(score):
    """
    This function is only called
    if you have survived with a score of 2 now.
    """
    if score == 2:
        input("Press Enter To Continue...\n")
        print("Chapter 2: ... ")
        input("Press Enter To Continue...\n")

        print("You come across an old abandoned house, barn and store")

        input("Press Enter To Continue...\n")
        choice = input("Enter (H)ouse, (B)arn or (S)tore?\n").upper()

        while choice not in["HOUSE", "BARN", "STORE", "H", "B", "S"]:
            input("Press Enter To Continue...\n")
            print("Sorry. I don't understand")
            choice = input("Enter house or barn or store?\n").upper()

        if choice == ["HOUSE", "H"]:
            input("Press Enter To Continue...\n")
            print("You enter the house, rummaging around ... ")
            input("Press Enter To Continue...\n")
            print("You find a shot gun and three shot gun shells")
            input("Press Enter To Continue...\n")
            shotgun = True
            score = 3
        elif choice == ["STORE", "S"]:
            input("Press Enter To Continue...\n")
            print("You enter the store, rummaging around ... ")
            input("Press Enter To Continue...\n")
            print("You stock up on supplies and find a gun with 4 bullets")
            input("Press Enter To Continue...\n")
            gun = True
            score = 3
        elif choice == ["BARN", "B"]:
            input("Press Enter To Continue...\n")
            print("You enter the barn where you could hear odd noises ... ")
            input("Press Enter To Continue...\n")
            print("You encounter a mob of zombies")
            input("Press Enter To Continue...\n")
            print("You didn't survive")
        else:
            input("Press Enter To Continue...\n")
            print("You enter the store and slip going down the escalater ")
            input("Press Enter To Continue...\n")
            print("You fall to your death")
            input("Press Enter To Continue...\n")
            print("You didn't survive")

    return (score, shotgun)


def stage_three(score, shotgun):
    """
    This function is only called
    if you have survived with a score of 3 now.
    """
    if score == 3:
        input("Press Enter To Continue...\n")
        print("Chapter 3: ... ")
        input("Press Enter To Continue...\n")

        print("You make it to the perimeter of the safe haven")
        input("Press Enter To Continue...\n")
        print("Only one problem ... ")
        input("Press Enter To Continue...\n")
        print("Two Zombies")
        print("")
        input("Press Enter To Continue...\n")

        if shotgun:
            print("You have three shots to hit two targets")
            shots = 3
        else:
            print("You have four shots to hit two targets")
            shots = 4

        input("Press Enter To Continue...\n")
        zombies = 2
        while shots > 0 and zombies > 0:
            hit = randint(1, 3)

            if hit in [1, 2]:
                input("Press Enter To Continue...\n")
                print("A lucky shot, you killed a zombie")
                shots = shots - 1
                zombies = zombies - 1
            else:
                input("Press Enter To Continue...\n")
                print("You fire a shot, but miss")
                shots = shots - 1

        if zombies == 0:
            print("You made it!")
            score = 5
        else:
            print("You fired all shots and the zombies are enclosing")
            score = 4
    return score


# Step 0: Call main menu procedure
if __name__ == '__main__':
    while True:
        start_game()
        if not retry_game():
            exit(1)
