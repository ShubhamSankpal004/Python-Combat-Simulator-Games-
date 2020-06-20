#      ASSIGNMENT- 1
#      FIT9133
#      PROGRAMMING FOUNDATION IN PYTHON
#      StudentID: 29912520
#      Name: Shubham Jaideep Sankpal
#      Assignment start date: 04/08/2018
#      Last Modified date: 22/08/2018
#      Submission Date: 23/08/2018
#      Due Date: 24/08/2018
#      BASIC GAME


# Importing needed libraries
from time import sleep


# Printing Menus for the Commanders
print("=====================================")
print("The Basic Game")
print("=====================================")
print("Select Troops.")
print("1.A= Archer and Cost= 1$")
print("2.K= Knight and Cost= 1$")
print("3.S= Soldier and Cost= 1$")
print("4.E= Exit")


# Initializing commander1 list and the army_choice list to store the troops selected by commander1.
# army_choice will take the input of the commander1 and accordingly add the troops to the commander1 list.
# The base amount given to commander1 is 10$ which will get deducted by 1$ after selecting each troop.

x = 0
commander1 = []
army_choice = []
print("Commander 1 select your army with your 10$:")
while x < 10:
    army_choice = input("Enter troop of your choice (A/K/S/E):")
    if army_choice == "A":
        commander1.append(army_choice)
        print("You have selected Archer")
        print("Amount Remaining", 10 - (x + 1))
        x += 1
    elif army_choice == "K":
        commander1.append(army_choice)
        print("You have selected Knight")
        print("Amount Remaining", 10 - (x + 1))
        x += 1
    elif army_choice == "S":
        commander1.append(army_choice)
        print("You have selected Soldier")
        print("Amount Remaining", 10 - (x + 1))
        x += 1
    elif army_choice == "E":
        print("Commander 1 army selection completed")
        break
    else:
        print("troop does not exist")
print(commander1)


# Initializing commander2 list and the army_choice list to store the troops selected by commander2
# army_choice will take the input of the commander2 and accordingly add the troops to the commander2 list
# The base amount given to commander2 is 10$ which will get deducted by 1$ after selecting each troop.

x = 0
commander2 = []
army_choice = []
print("Commander 2 select your army with your 10$: ")

while x < 10:
    army_choice = input("Enter troop of your choice (A/K/S/E):")
    if army_choice == "A":
        commander2.append(army_choice)
        print("You have selected Archer")
        print("Amount Remaining", 10 - (x + 1))
        x += 1
    elif army_choice == "K":
        commander2.append(army_choice)
        print("You have selected Knight")
        print("Amount Remaining", 10 - (x + 1))
        x += 1
    elif army_choice == "S":
        commander2.append(army_choice)
        print("You have selected Soldier")
        print("Amount Remaining", 10 - (x + 1))
        x += 1
    elif army_choice == "E":
        print("Commander 2 army selection completed")
        break
else:
    print("troop does not exist")
print(commander2)

# Checking lengths of both the lists of commander1 and commander2
# Comparing the elements of both the lists as per the order of troops selected by the commanders
# Checking all the test cases that are possible with their outcomes

while len(commander2) > 0 and len(commander1) > 0:
    if commander1[0] == 'A' and commander2[0] == 'A':
        print("Battle is going on... ")
        print("It's a Tie between the troops...")
        commander1.pop(0)
        commander2.pop(0)
        sleep(3)

    elif commander1[0] == 'A' and commander2[0] == 'K':
        print("Battle is going on... ")
        print("Knight is the winner in this battle...")
        commander1.pop(0)
        sleep(3)

    elif commander1[0] == 'A' and commander2[0] == 'S':
        print("Battle is going on... ")
        print("Archer is the winner in this battle...")
        commander2.pop(0)
        sleep(3)

    elif commander1[0] == 'K' and commander2[0] == 'K':
        print("Battle is going on... ")
        print("It's a Tie between the troops...")
        commander1.pop(0)
        commander2.pop(0)
        sleep(3)

    elif commander1[0] == 'K' and commander2[0] == 'S':
        print("Battle is going on... ")
        print("Soldier is the winner in this battle... ")
        commander1.pop(0)
        sleep(3)

    elif commander1[0] == 'K' and commander2[0] == 'A':
        print("Battle is going on... ")
        print("Knight is the winner in this battle...")
        commander2.pop(0)
        sleep(3)

    elif commander1[0] == 'S' and commander2[0] == 'S':
        print("Battle is going on... ")
        print("It's a Tie between the troops...")
        commander1.pop(0)
        commander2.pop(0)
        sleep(3)

    elif commander1[0] == 'S' and commander2[0] == 'K':
        print("Battle is going on... ")
        print("Soldier is the winner in this battle...")
        commander2.pop(0)
        sleep(3)

    elif commander1[0] == 'S' and commander2[0] == 'A':
        print("Battle is going on... ")
        print("Archer is the winner in this battle...")
        commander1.pop(0)
        sleep(3)

# At the end declare the battle winner by comparing lengths of commander1 and commander2 lists
# Also printing the remaining troops in battle winner's list

print("Battle Stops...")
print("Result of the Battle:")
if len(commander1) == len(commander2):
    print("Its a tie between the Commanders...")
elif len(commander1) > len(commander2):
    print("Commander 1 is the winner of the Battle...")
    print("Remaining troops of the winner:", commander1)
elif len(commander1) < len(commander2):
    print("Commander 2 is the winner of the Battle...")
    print("Remaining troops of the winner:", commander2)


	