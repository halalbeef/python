#!/usr/bin/env python
#
# Importing modules
import csv
import time
# Predefines
#debug=True
cliPrompt=True


# Defining all the functions

def start():
        print("Welcome to Big Rod's Pizza!")
        if "debug" in globals():
                dev_menu()
        import_files()
        cli()

def import_files():
        global menu
        menu = [[],[],[],[],[]]
        submenus=["starters", "pizzas", "drinks", "desserts", "extras"]
        for i in range(0,len(submenus)):
                for item in csv.reader(open("etc/"+submenus[i]+".csv")):
                        menu[i].append(item)
def cli():
        global cliPrompt
        if cliPrompt:
                cliPrompt=False
        else:
                #allows the user to read the previouse text easier
                foo=input("\n\n\nPress [ENTER] to return")

        print("\n\n\nWhat would you like to do?\n")
        print("0) Help with this app")
        print("1) Print Menu")
        print("2) Start Ordering/Change your order")
        print("3) Check Order")
        print("4) Print and Checkout")
        print("5) Check on the meal")
        menuTemp=input("")
        try:
                menuOption=int(menuTemp)
        except ValueError:
                print("Thats's not even a number!")
                cli()
        
        if menuOption in range(0,5):
                menuOption=str(menuOption)
                if menuOption == "0":
                        print("\nThis is \"Big Rod's Pizza\" ordering app")
                        print("It's made for python 3.X")
                        print("Type in 1 to see the menu")
                        print("Then 2 to start ordering")
                        print("Then 3 to check your order")
                        print("If it's wrong you can type in 2 to change it")
                        print("Then type in 4 to print your order and check out")
                        print("To track your order type in 5")
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
                else:
                        print("Error, please check the cli menu")
                cli()
        else:
                print("There is no option {}...".format(menu))
                cli()

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
                
                # Redirects back to cli
                cli()
        else:
                print("There is no submenu section {}...".format(printArea))
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
                        print("    >{}".format(menu[menuIndex][item][1])) # Description for the item
                        print("         Price:",currency(menu[menuIndex][item][2]))

        elif menuIndexStr == "1":
                banner(menuIndex)
                if "debug" in globals():
                        print("menuIndex is {} and It should be printing out ONLY pizzas".format(menuIndex))
                for item in range(0,len(menu[menuIndex])):
                        print(menu[menuIndex][item][0])
                        print("    >{}".format(menu[menuIndex][item][1]))
                        print("         Small: "+currency(menu[menuIndex][item][2]))
                        print("        Medium: "+currency(menu[menuIndex][item][3]))
                        print("         Large: "+currency(menu[menuIndex][item][4]))
                        print("       Monster: "+currency(menu[menuIndex][item][5]))

        elif menuIndexStr == "2":
                banner(menuIndex)
                if "debug" in globals():
                        print("menuIndex is {} and It should be printing out ONLY drinks".format(menuIndex))
                for item in range(0,len(menu[menuIndex])):
                        print(menu[menuIndex][item][0])
                        print("    >{}".format(menu[menuIndex][item][1]))
                        print("         Cans: "+currency(menu[menuIndex][item][2]))
                        print("      Bottels: "+currency(menu[menuIndex][item][3]))
                        print("      2Liters: "+currency(menu[menuIndex][item][4]))

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

def dev_menu():
        # Print out the menu in pure python "list" or array form
        for i in range(0,len(menu)):
                print("\n")
                for b in menu[i]:
                        print(b)
                        
import_files()
start()
