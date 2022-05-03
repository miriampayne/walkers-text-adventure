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

#Step 0: Call main menu procedure
startGame()