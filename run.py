# import pyfiglet module
import pyfiglet
import time

def startGame():
    
    welcome = pyfiglet.figlet_format("Walkers")
    print (welcome)
    print ("A Zombie Text Adventure by Miriam Payne")
    print ("Survive the Zombie Apocalypse!!")

    time.sleep(2)

    name = input("What is your name?")
    age = int(input("Enter your age?"))