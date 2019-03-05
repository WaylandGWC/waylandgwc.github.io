x = 1
import random

def walking():
    print("1. North")
    print("2. South")
    print("3. East")
    print("4. West")
    dir = int(input("Select the number of the direction you want to walk: "))
    print("")
    numberofblocks = random.randint(1,10)
    if numberofblocks < 5:
        danger = 0
    else:
        danger = 1
    return danger

def useSupply(supply, bag, health):
    if supply == 1:
        health = health + 2
        supp = "food"
    elif supply == 2:
        health = health + 2
        supp = "water"
    elif supply == 3:
        health = health + 5
        supp = "medicine"
    else:
        supp = "socks"
    
    
    if health > 10:
        health = 10
    
    newbag = bag[0:len(bag)-1]
    length = 0
    for i in range(0,len(bag)):
        if bag[i] != supp:
            newbag[length] = bag[i]
            length = length + 1
    bag = newbag
    return (bag,health)
    
def addSupply(bag):
    r = random.randint(1,4)
    if r == 1:
        print("You have found a pair of socks!")
        print("")
        bag.append("socks")
    elif r == 2:
        print("You have found food!")
        print("")
        bag.append("food")
    elif r == 3:
        print("You have found water!")
        print("")
        bag.append("water")
    else:
        print("You have found medicine!")
        print("")
        bag.append("medicine")
    return bag
        
def displayOptions():
    print("1. Show supplies")
    print("2. Use supplies")
    print("3. Show Health")
    print("4. Keep walking")
    option = int(input("Select an option: "))
    print("")
    return option

def infectedAttack(bag,health):
    death = 0
    r = random.randint(1,3)
    if r <=2:
        print("A hoard of zombies has noticed you!")
        run = int(input("1.Run of 2. Attack?"))
        print("")
    else:
        print("There are zombies ahead but they have not noticed you yet.")
        run = int(input("1.Run of 2. Attack?"))
        print("")
    f = random.randint(1,3)
    if run == 1 and r<=2:
        if f == 1:
            print("The hoard has overtaken you. GAME OVER")
            print("")
            x = 0
            death == 1
        elif f == 2:
            health = health -4
            if health < 0:
                death = 1
                print("You have been injured, but were not healthy enough to survive. GAME OVER")
                print("")
                x = 0
            else:
                print("You have been injured, but manage to escape.")
                print("")
        else:
            print("You have successfully evaded the zombies.")
            print("")
    if run == 2 and r<=2:
        hasSocks = 0
        for i in range(0,len(bag)-1):
            if bag[i] == "socks":
                hasSocks = 1
        if hasSocks>0:
            useSupply('socks',bag,health)
            if f == 1:
                print("The hoard has overtaken you. GAME OVER")
                print("")
                x = 0
                death = 1
            elif f == 2:
                health = health - 3
                if health < 0:
                    death = 1;
                    print("You have been injured, but were not healthy enough to survive. GAME OVER")
                    print("")
                    x = 0
                else:
                    print("You have been injured, but manage to escape.")
                    print("")
            else:
                print("You successfully attacked the zombies and managed to escape.")
                print("")
                
        else:
            print("You have no socks! GAME OVER")
            print("")
            death = 1
            x = 0
            
    if run == 1 and r > 2:
        if f == 1:
            print("The zombies have noticed you and killed you. GAME OVER")
            print("")
            x = 0
            death = 1
        elif f > 1:
            print("You've managed to avoid them.")
            print("")
    if run == 2 and r >2:
        for i in range(0,len(bag)-1):
            if bag[i] == "socks":
                hasSocks = 1
        if hasSocks>0:
            useSupply('socks',bag,health)
            if f == 1:
                print("The hoard has overtaken you. GAME OVER")
                print("")
                x = 0
                death = 1
            elif f == 2:
                health = health - 3
                if health < 0:
                    death = 1;
                    print("You have been injured, but were not healthy enough to survive. GAME OVER")
                    print("")
                    x = 0
                else:
                    print("You have been injured, but manage to escape.")
                    print("")
            else:
                print("You successfully attacked the zombies and managed to escape.")
                print("")
        else:
            print("You have no socks! GAME OVER")
            print("")
            x = 0
            death = 1
    return (death, health, bag)
while x==1:
    print("Main Menu")
    print("1. Start")
    print("2. Instructions")
    print("3. Exit")
    s = int(input("Select option number (1,2, or 3): "))
    print("")
    if s == 2:
        print("Instructions")
        print("Your mission is to stay alive. You can use supplies to increase your health. Food and water increase your health by 2")
        print("and medicine increases your health by 5. If your health goes below 0, you are dead. You also have socks which can be used")
        print("to attack the zombies. When you run into zombies, you have the choice of running or attacking. If you decide to attack, but")
        print("have no socks, you will die. Good luck....")
        print("")
    elif s == 3:
        x = 0
    elif s == 1:
        r = random.randint(1,4)
        if r == 1:
            bag = ["socks","water"]
        elif r == 2:
            bag = ["socks","food"]
        elif r == 3:
            bag = ["water", "medicine"]
        else:
            bag = ["water","food","medicine"]
        health = random.randint(1,9)
        alive = 0;
        danger = 0;
        print("Three weeks ago, the CDC issued a statement that a new virus was identified.") 
        print("If infected, people start to become more aggressive, eventually going so far ")
        print("as to kill other humans. Now, everyone you know has become infected. However, there are ")
        print("still some people out there. Your goal is to stay alive. The infected are everywhere and ")
        print("the only way to kill them is with socks.")
        a = int(input("Are you ready? (Yes = 1/No = 2)"))
        print("")
        if a == 1:
            print("Right now, you have the following supplies and health level (out of 10): ")
            print(bag)
            print(health)
            print("")
            while alive == 0:
                while danger == 0:
                    option = displayOptions()
                   
                    if option == 1:
                        print(bag)
                        print("")
                    elif option == 2:
                        supply = int(input("Which supply would you like to use? 1. Food, 2. Water, or 3. Medicine?"))
                        print("")
                        [bag, health] = useSupply(supply, bag, health)
                    elif option == 3:
                        print(health)
                        print("")
                    else:
                        danger = walking()
                        d = random.randint(1,4)
                        if d <=3 and danger == 0:
                            bag = addSupply(bag)
                        
                while danger == 1:
                    [alive, health, bag] = infectedAttack(bag, health)
                    danger = 0
                    if alive == 0:
                        option = displayOptions()
                        if option == 1:
                            print(bag)
                        elif option == 2:
                            supply = int(input("Which supply would you like to use? 1. Food, 2. Water, or 3. Medicine?"))
                            print("")
                            [bag, health] = useSupply(supply, bag, health)
                        elif option == 3:
                            print(health)
                        else:
                            danger = walking()
                            d = random.randint(1,4)
                            if d <=3 and danger == 0:
                                bag = addSupply(bag)
           
    else:
        x = 0            
        


                    
            
            
    