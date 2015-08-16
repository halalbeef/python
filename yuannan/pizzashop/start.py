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
                firstTime=False
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
                menu=int(menuTemp)
        except ValueError:
                print("Thats's not even a number!")
                cli()
        
        if menu in range(0,5):
                menu=str(menu)
                if menu == "0":
                        print("\nThis is Big Rod's pizza ordering app")
                        print("It's made for python 3.X")
                        print("Type in 1 to see the menu")
                        print("Then 2 to start ordering")
                        print("Then 3 to check your order")
                        print("If it's wrong you can type in 2 to change it")
                        print("Then type in 4 to print your order and check out")
                        print("To track your order type in \"5\"\n\n\n")

                if menu == "1":
                        print_menu()
                if menu == "2":
                        order()
                        
                if menu == "3":
                        printOrder()
                        
                if menu == "4":
                        checkout()
                        
                if menu == "5":
                        checkMeal()
                        
                cli()
        else:
                print("There is no option {}...".format(menu))
                cli()

def print_menu():
        def starters():
                for item in range(0,len(menu[0])):
                        print("\n")
                        print(menu[0][item][0])
                        print("    -{}".format(menu[0][item][1]))
                        print(p2p(menu[0][item][2]))

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
                print_menu()
        
        if area in range(0,5):
                area=str(area)
                print("in area 0-5")
                if area == "0":
                        starters()
                        pizzas()
                        drinks()
                        desserts()
                        extras()
                        print_menu()
                if area == "1":
                        starters()
                if area == "2":
                        pizzas()
                if area == "3":
                        drinks()
                if area == "4":
                        desserts()
                if area == "5":
                        extras()
                
                #redirects back to cli
                cli()
        else:
                print("There is no submenu section {}...".format(printArea))
                print_menu()

def p2p(pennies):
        return("£"+pennies[:-2]+"."+pennies[-2:])

def dev_menu():
        for i in range(0,len(menu)):
                print("\n")
                for b in menu[i]:
                        print(b)
                        
import_files()
start()
