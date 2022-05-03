# import pyfiglet module
import pyfiglet
import time

def startGame():
    
    welcome = pyfiglet.figlet_format("Walkers")
    print (welcome)
    print ("A Zombie Text Adventure by Miriam Payne")
    print ("Mission: Survive the Zombie Apocalypse or Die Trying!")

    time.sleep(2)

    name = input("Please confirm your name: ")
    age = int(input("Please confirm your age: "))

    time.sleep(1)
    if age >0 and age < 12:
        print("You're young ... chances of survival are slim ... use size and speed to your advantage")
    elif age >= 12 and age <75:
        print ("You're going to need a good aim ... fair survival if you're a good shot")
    elif age >=75:
        print ("You're as slow as the walkers ... I hate to break it to you but your chances are slim")

    time.sleep(1)
    print ("Try and survive")

    time.sleep(1)
    print ("Chapter 1")

    time.sleep(1)
    print ("...")

    time.sleep(1)

    print ("You walk into an abandoned Dublin city center tower block car park")
    time.sleep(1)

    print ("A dodgy vaccine for the pandemic has turned 95% the population into a flesh eating zombies outbreak.")
    time.sleep(1)

    print ("Your sat nav shows you are 8 miles from a safe haven")
    time.sleep(1)

    time.sleep(1)

    print("")
    print ("A zombie horde appears... you grab your hurley from your backpack")

    time.sleep(2)

#Step 0: Call main menu procedure
startGame()

#Step 1: Get first action
action = input("Fight or Flight Response?").upper()
while action not in ["FIGHT", "RUN"]:
    time.sleep(1)
    print ("That is not a valid action")
    action = input("Fight or Run?").upper()

if action == "FIGHT":
    if age >= 12:
        print("Your youthfulness helps you avoid being chomped")
        time.sleep(1)
        print ("You made it this time")
        score = 2
    else:
        print ("You attack")
        time.sleep(1)
        print ("A combination of old age and slow reactions cause you to be bitten")
        print ("You're too old to be fighting zombies")
        score = 1
elif action == "RUN":
    if age <=12:
        print("You run from the zombie, but are too slow")
        time.sleep(1)
        print ("This walker clearly has some agility left in them and catches up quick")
        score = 1
    else:
        print ("You run from the zombie")
        time.sleep(1)
        print ("Your experienced legs carry you to safety")
        score = 2