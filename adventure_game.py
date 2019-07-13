import time
import random

# List of all the enemies in the game to randomize.
enemies = ["Dragon", "Troll", "Pirate", "Vampire", "Gorgon"]
enemy = random.choice(enemies)

# boolean to check if the game is being played for the first time
firstTime = True

# Boolean to check if the game is being restarted
restart = False

# to check if the player have the sword or not
sword = False

# Boolean for the victory TODO
victory = False

# Boolean for the defeat TODO
defeat = False


def house(name, weapon):
    print("You approach the door of the house.")
    time.sleep(1.5)
    print("You are about to knock when the door opens and out steps a " + name + ".")
    time.sleep(1.5)
    print("Eep! This is the " + name +"\'s house!")
    time.sleep(1.5)
    print("The " + name + " attacks you!")
    time.sleep(1.5)
    print("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    time.sleep(1.5)
    print("Would you like to (1) fight or (2) run away?")
    res = input("Please enter 1 or 2")
    while True:
        if res == "1":
            if weapon == True:
                print("As the " + name + "moves to attack, you unsheath your new sword.")
                time.sleep(1.5)
                print("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
                time.sleep(1.5)
                print("But the " + name + "takes one look at your shiny new toy and runs away!")
                time.sleep(1.5)
                print("You have rid the town of the " + name + ". You are victorious!")



def cave(weapon):
    print("You peer cautiously into the cave.")
    time.sleep(1.5)
    if weapon == False:
        print("It turns out to be only a very small cave.")
        time.sleep(1.5)
        print("Your eye catches a glint of metal behind a rock.")
        time.sleep(1.5)
        print("You have found the magical Sword of Ogoroth!")
        time.sleep(1.5)
        print("You discard your silly old dagger and take the sword with you.")
        sword = True
        time.sleep(1.5)
        print("You walk back out to the field.")
        time.sleep(1.5)
        print("\nEnter 1 to knock on the door of the house.")
        time.sleep(1.5)
        print("Enter 2 to peer into the cave.")
        time.sleep(1.5)
        print("What would you like to do?")
    else:
        print("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        time.sleep(1.5)
        print("You walk back out to the field.")
        time.sleep(1.5)
        print("\nEnter 1 to knock on the door of the house.")
        time.sleep(1.5)
        print("Enter 2 to peer into the cave.")
        time.sleep(1.5)
        print("What would you like to do?")




def field():
    print("field")


while firstTime or restart:
    sword = False
    firstTime = False
    restart = False
    print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    time.sleep(1.5)
    print("Rumor has it that a "+ enemy +"  is somewhere around here, and has been terrifying the nearby village.")
    time.sleep(1.5)
    print("In front of you is a house.")
    time.sleep(1.5)
    print("To your right is a dark cave.")
    time.sleep(1.5)
    print("In your hand you hold your trusty (but not very effective) dagger.")
    time.sleep(1.5)
    print("")
    time.sleep(1.5)
    print("Enter 1 to knock on the door of the house.")
    time.sleep(1.5)
    print("Enter 2 to peer into the cave.")
    time.sleep(1.5)
    print("What would you like to do?")
    num =  input("Please enter 1 or 2")


    while True:
        if num == "1":
            house(enemy)
            break
        elif num == "2":
            cave(sword)
            break
        else:
            num = input("Please enter 1 or 2")

# response is used to ask user to restart or end the game.
    response = input("Would you like to play again? (y/n)")
    while True:
        if response == "y":
            restart = True
            print("Excellent! Restarting the game")
            break
        elif response == "n":
            print("Thanks for playing! See you next time.")
            break
        else:
            response = input("Would you like to play again? (y/n)")