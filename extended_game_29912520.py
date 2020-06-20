#      ASSIGNMENT- 1
#      FIT9133
#      PROGRAMMING FOUNDATION IN PYTHON
#      StudentID: 29912520
#      Name: Shubham Jaideep Sankpal
#      Assignment start date: 04/08/2018
#      Last Modified date: 22/08/218
#      Submission Date: 23/08/2018
#      Due Date: 24/08/2018
#      EXTENDED GAME

# Importing needed libraries
from time import sleep

# Printing Menus for the Commanders
print("=====================================")
print("The Extended Game")
print("=====================================")
print("Select Troops.")
print("1.A= Archer and Cost= 1$")
print("2.K= Knight and Cost= 1$")
print("3.S= Soldier and Cost= 1$")
print("4.W= Wizard and Cost= 3$")
print("5.C= Seige Equipment and cost= 2$")
print("6.E= Exit")


# Initializing commander1 list and the army_choice list to store the troops selected by commander1.
# army_choice will take the input of the commander1 and accordingly add the troops to the commander1 list.
''' The base amount given to commander1 is 10$ which will get deducted by 1$, 2$ or 3$
according to selection of the troops.'''

x = 0
commander1 = []
army_choice = []
print("Commander 1 select your army with your 10$:")
while x < 10:
    army_choice = input("Enter troop of your choice (A/K/S/W/C/E):")
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
    elif army_choice == "W":
        commander1.append(army_choice)
        print("You have selected Wizard")
        print("Amount Remaining", 10 - (x + 3))
        x += 3
    elif army_choice == "C":
        commander1.append(army_choice)
        print("You have selected Seige Equiment")
        print("Amount Remaining", 10 - (x + 2))
        x += 2
    elif army_choice == "E":
        print("Commander 1 army selection completed")
        medics1 = 10 - x
        print("Medics Available:", medics1)
        break
    else:
        print("troop does not exist")
print(commander1)



# Initializing commander2 list and the army_choice list to store the troops selected by commander2.
# army_choice will take the input of the commander2 and accordingly add the troops to the commander2 list.
''' The base amount given to commander2 is 10$ which will get deducted by 1$, 2$ or 3$
according to selection of the troops.'''
# After the army selection is completed the reamining amount of the is converted into medics each of 1$ cost.

x = 0
commander2 = []
army_choice = []
print("Commander 2 select your army with your 10$: ")
while x < 10:
    army_choice = input("Enter troop of your choice (A/K/S/W/C/E):")
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
    elif army_choice == "W":
        commander2.append(army_choice)
        print("You have selected Wizard")
        print("Amount Remaining", 10 - (x + 3))
        x += 3
    elif army_choice == "C":
        commander2.append(army_choice)
        print("You have selected Seige Equiment")
        print("Amount Remaining", 10 - (x + 2))
        x += 2
    elif army_choice =="E":
        print("Commander 2 army selection completed")
        medics2 = 10 - x
        print("Medics Available:", medics2)
        break
    else:
        print("troop does not exist")
print(commander2)

# Checking lengths of both the lists of commander1 and commander2.
# Comparing the elements of both the lists as per the order of troops selected by the commanders.
# Initializing temp, temp1 temp2 for storing the eliminated troops.
# Initializing medics1 and medics2 for applying medics to the eliminated troops and then add them at the last of list of that commanders untill the medics count is zero.
# Checking all the test cases that are possible with their outcomes.

temp=""
temp1=""
temp2=""
medics1
medics2
while len(commander2) > 0 and len(commander1) > 0:
    if commander1[0] == 'A' and  commander2[0] == 'A':
        print("Battle is going on... ")
        print("It's a Tie between the troops...")
        temp1 = commander1.pop(0)
        temp2 = commander2.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
        if medics2 !=0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'A' and  commander2[0] == 'K':
        print("Battle is going on... ")
        print("Knight is the winner in this battle...")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'A' and  commander2[0] == 'S':
        print("Battle is going on... ")
        print("Archer is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 !=0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'A' and  commander2[0] == 'W':
        print("Battle is going on... ")
        print("Archer is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 !=0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'A' and  commander2[0] == 'C':
        print("Battle is going on... ")
        print("Seige Equipment is the winner in this battle...")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'K' and  commander2[0] == 'K':
        print("Battle is going on... ")
        print("It's a Tie between the troops...")
        temp1 = commander1.pop(0)
        temp2 = commander2.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
        if medics2 !=0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'K' and  commander2[0] == 'S':
        print("Battle is going on... ")
        print("Soldier is the winner in this battle... ")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'K' and  commander2[0] == 'A':
        print("Battle is going on... ")
        print("Knight is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 !=0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'K' and  commander2[0] == 'W':
        print("Battle is going on... ")
        print("Wizard is the winner in this battle... ")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'K' and  commander2[0] == 'C':
        print("Battle is going on... ")
        print("Knight is the winner in this battle... ")
        temp2 = commander2.pop(0)
        if medics2 !=0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'S' and  commander2[0] == 'S':
        print("Battle is going on... ")
        print("It's a Tie between the troops...")
        commander1.pop(0)
        temp2 = commander2.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
        if medics2 != 0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'S' and  commander2[0] == 'K':
        print("Battle is going on... ")
        print("Soldier is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 !=0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'S' and  commander2[0] == 'A':
        print("Battle is going on... ")
        print("Archer is the winner in this battle...")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'S' and  commander2[0] == 'W':
        print("Battle is going on... ")
        print("Wizard is the winner in this battle...")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'S' and  commander2[0] == 'C':
        print("Battle is going on... ")
        print("Seige Equipment is the winner in this battle...")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'W' and  commander2[0] == 'W':
        print("Battle is going on... ")
        print("It's a Tie between the troops...")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
        temp2 = commander2.pop(0)
        if medics2 != 0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'W' and  commander2[0] == 'A':
        print("Battle is going on... ")
        print("Archer is the winner in this battle...")
        temp1 = commander1.pop(0)
        if medics1 !=0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'W' and  commander2[0] == 'K':
        print("Battle is going on... ")
        print("Wizard is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 !=0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'W' and  commander2[0] == 'S':
        print("Battle is going on... ")
        print("Wizard is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 != 0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'W' and  commander2[0] == 'C':
        print("Battle is going on... ")
        print("Wizard is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 != 0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'C' and  commander2[0] == 'C':
        print("Battle is going on... ")
        print("It's a Tie between the troops...")
        temp1 = commander1.pop(0)
        if medics1 != 0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
        temp2 = commander2.pop(0)
        if medics2 != 0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'C' and  commander2[0] == 'A':
        print("Battle is going on... ")
        print("Seige Equipment is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 != 0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'C' and  commander2[0] == 'K':
        print("Battle is going on... ")
        print("Knight is the winner in this battle...")
        temp1 = commander1.pop(0)
        if medics1 != 0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
            sleep(3)

    elif commander1[0] == 'C' and  commander2[0] == 'S':
        print("Battle is going on... ")
        print("Seige Equipment is the winner in this battle...")
        temp2 = commander2.pop(0)
        if medics2 != 0 and temp != None:
            commander2.append(temp2)
            medics2 -= 1
            sleep(3)

    elif commander1[0] == 'C' and  commander2[0] == 'W':
        print("Battle is going on... ")
        print("Wizard is the winner in this battle...")
        temp1 = commander1.pop(0)
        if medics1 != 0 and temp != None:
            commander1.append(temp1)
            medics1 -= 1
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