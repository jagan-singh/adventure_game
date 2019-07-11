import time
import random

enemies = ["Dragon", "Troll", "Pirate", "Vampire", "Gorgon"]
enemy = random.choice(enemies)

def house(str):
    print("You approach the door of the house.")
    time.sleep(1)
    print("You are about to knock when the door opens and out steps a " + str + ".")
    time.sleep(1)
    print("Eep! This is the " + str +"\'s house!")
    time.sleep(1)
    print("The " + str + " attacks you!")
    time.sleep(1)
    print("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    time.sleep(1)
    print("Would you like to (1) fight or (2) run away?")



def cave():
    print("")


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

while int(num) == 1 and int(num) == 2:
    if int(num) == 1:
        house(enemy)
    elif int(num) == 2:
     cave(enemy)
    else:
        num = input("Please enter 1 or 2")




