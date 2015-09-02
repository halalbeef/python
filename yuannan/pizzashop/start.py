#!/usr/bin/env python
#
# Importing modules
import csv
import time
# Predefines
debug=True

# Defining all the functions

def start():
        print("Welcome to Big Rod's Pizza!")
        import_files()
        if "debug" in globals():
                dev_menu()
        cli(False)

def dev_menu():
        # Print out the menu in pure python "list" or array form
        for i in range(0,len(menu)):
                print("\n")
                for b in menu[i]:
                        print(b)

def import_files():
        global menu
        global customerOrder
        menu = [[],[],[],[],[]]
        customerOrder = []
        submenus=["starters", "pizzas", "drinks", "desserts", "extras"]
        for i in range(0,len(submenus)):
                for item in csv.reader(open("etc/"+submenus[i]+".csv")):
                        menu[i].append(item)

def cli(prompt):
        if prompt:
                #allows the user to read the previouse text easier
                pause=input("\n\n\nPress [ENTER] to return")
        
        print("\n\n\nWhat would you like to do?\n")
        print("1) Print Menu")
        print("2) Start Ordering/Change your order")
        print("3) Check Order")
        print("4) Checkout and Print")
        print("5) Check on the meal")
        print("9) Help with this app")
        print("0) EXIT")
        menuTemp=input("")
        try:
                menuOption=int(menuTemp)
        except ValueError:
                print("Thats's not even a number!")
                cli(False)
        
        if menuOption in range(0,6):
                menuOption=str(menuOption)
                if menuOption == "0":
                        print("Goodbye!")
                        exit()
                elif menuOption == "1":
                        print_prompt()
                elif menuOption == "2":
                        order()
                elif menuOption == "3":
                        printOrder()
                elif menuOption == "4":
                        checkout()
                elif menuOption == "5":
                        checkMeal()
                elif menuOption == "9":
                        print_help()
                else:
                        print("Error, please check the cli menu")
        else:
                print("There is no option {}...".format(menuOption))
        cli(False)

def print_help():
        print("\nThis is \"Big Rod's Pizza\" ordering app")
        print("It's made for python 3.X")
        print("The pizzas are made fresh in:")
        print("Small   -  9 Inches")
        print("Medium  - 11 Inches")
        print("Large   - 13 Inches")
        print("Monster - 15 Inches")
        print("\nAnd the drinks are avalaiable in:")
        print("Cans    - 330ml")
        print("Bottles - 500ml")
        print("2Liters - 2000ml")
        print("The rest is  only avaliable in one size")

def print_prompt():
        print("\n\n\nWhat do you want print?\n")
        print("0) For all of the menu")
        print("1) Starters")
        print("2) Pizzas")
        print("3) Drinks")
        print("4) Desserts")
        print("5) Extras")
        areaTemp=input("")
        try:
                area=int(areaTemp)
        except ValueError:
                print("Thats's not even a number!")
                print_prompt()
        
        if area in range(0,6):
                print("in area 0-5")
                if area == 0:
                        for submenu in range(0,5):
                                print_menu(submenu)
                else:
                        print_menu(area-1)
                
        else:
                print("There is no submenu section {}...".format(area))
                print_prompt()

def print_menu(menuIndex):
        menuIndexStr=str(menuIndex)
        simpleMenu=["0","3","4"]
        if menuIndexStr in simpleMenu:
                if "debug" in globals():
                        print("menuIndex is {} and it should print out: Starters, Desserts and Extras".format(menuIndex))
                banner(menuIndex)
                for item in range(0,len(menu[menuIndex])):
                        print(menu[menuIndex][item][0])
                        print("{:>5}>{}".format("",menu[menuIndex][item][1])) # Description for the item
                        print("         Price:",currency(menu[menuIndex][item][2]))

        elif menuIndexStr == "1":
                banner(menuIndex)
                if "debug" in globals():
                        print("menuIndex is {} and It should be printing out ONLY pizzas".format(menuIndex))
                for item in range(0,len(menu[menuIndex])):
                        print(menu[menuIndex][item][0])
                        print("{:>5}>{}".format("",menu[menuIndex][item][1]))
                        print("{:>20}: {:>6}".format("Small",currency(menu[menuIndex][item][2])))
                        print("{:>20}: {:>6}".format("Medium",currency(menu[menuIndex][item][3])))
                        print("{:>20}: {:>6}".format("Large",currency(menu[menuIndex][item][4])))
                        print("{:>20}: {:>6}".format("Monster",currency(menu[menuIndex][item][5])))

        elif menuIndexStr == "2":
                banner(menuIndex)
                if "debug" in globals():
                        print("menuIndex is {} and It should be printing out ONLY drinks".format(menuIndex))
                for item in range(0,len(menu[menuIndex])):
                        print(menu[menuIndex][item][0])
                        print("{:>5}>{}".format("",menu[menuIndex][item][1]))
                        print("{:>20}: {:>6}".format("Cans",currency(menu[menuIndex][item][2])))
                        print("{:>20}: {:>6}".format("Bottles",currency(menu[menuIndex][item][3])))
                        print("{:>20}: {:>6}".format("2Liters",currency(menu[menuIndex][item][4])))

        else:
                print("This should have never happened!\nCheck function \"print_menu()\"")

def banner(subMenu):
        print("\n==============================")
        if subMenu == 0:
                print("========   STARTERS   ========")
        elif subMenu == 1:
                print("========    PIZZAS    ========")
        elif subMenu == 2:
                print("========    DRINKS    ========")
        elif subMenu == 3:
                print("========   DESSERTS   ========")
        elif subMenu == 4:
                print("========    EXTRAS    ========")
        else:
                print("ERROR!!! Check the function \"print_menu()\" line 3+")
        print("==============================\n")

def currency(money):
        money=str(money) # Converts to a string for later handeling
        whole=money[:-2]
        units=money[-2:]
        if len(whole) < 1:
                whole="0"
        while len(units) < 2:
                units="0"+units
        return("£"+whole+"."+units)

def order():
        print("\n\n\nWhat would you like to order?")
        print("1) Starters")
        print("2) Pizzas")
        print("3) Drinks")
        print("4) Desserts")
        print("5) Extras")
        print("8) Print menu")
        print("9) Remove an item")
        print("0) Return")
        menuTemp = input("")
        try:
                menuOption=int(menuTemp)
        except ValueError:
                print("That's not even a number!")
                order()
        if menuOption in range(1,5) or menuOption in range(8,10) or menuOption == 0:
                menuOption=str(menuOption)
                if menuOption == "0":
                        cli(False)
                elif menuOption == "9":
                        removeItem()
                elif menuOption == "8":
                        print_prompt()
                elif menuOption == "1" or menuOption == "4" or menuOption == "5":
                        orderBasics(menuOption)
                elif menuOption == "2":
                        orderPizza()
                elif menuOption == "3":
                        orderDrinks()
                else:
                        print("Error, this should not have happened, Error in function \"order()\"")
        else:
                print("There is no option {}...".format(menuOption))
        order()

def orderBasics(menuOption):
        # Ordering for item that have a set value e.g. Starters, 
        menuOption=int(menuOption)
        orderError=False
        print("\n")
        for item in range(len(menu[menuOption-1])):
                formatSpaces=50-len(menu[menuOption-1][item][0])
                print("{0}){1}{2:50}{3}".format(item+1," "*(3-len(str(item+1))),menu[menuOption-1][item][0],currency(menu[menuOption-1][item][2])))
        currentItemTemp=input("\nItem number: ")
        try:
                currentItem=int(currentItemTemp)-1
        except ValueError:
                orderError="Item not a number"
        if currentItem < 0:
                orderError = "Item number less than 1"
        elif currentItem >= len(menu[menuOption]):
                orderError="Item number higher total items"
        if orderError != False:
                print("orderError: {}".format(orderError))
                order()
        else:
                comment=str(input("Enter a comment, type in \"C\" to cancel or leave blank to confirm\n"))
                if comment.lower() == "c":
                        print("Cancelling item...")
                else:
                        currentItemList =[[menuOption-1],[currentItem],[menu[menuOption-1][currentItem][2]],[comment]]
                        customerOrder.append(currentItemList)
                if 'debug' in globals():
                        print(customerOrder)
        


#Starts the "start" function and actully  boots the program
start()
