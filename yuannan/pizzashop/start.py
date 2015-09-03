#!/usr/bin/env python
#
# V0.1.0 Alpha, Functional, but missing some value checking ext.
# "fully functional"
#
# Importing modules and defining essentails
import csv
import operator
from time import gmtime, strftime, sleep
#debug=True

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
        print("9) Help with this app")
        print("0) EXIT")
        menuTemp=input("")
        try:
                menuOption=int(menuTemp)
        except ValueError:
                print("Thats's not even a number!")
                cli(False)
        
        if menuOption in range(0,5) or menuOption == 9:
                menuOption=str(menuOption)
                if menuOption == "0":
                        print("Goodbye!")
                        exit()
                elif menuOption == "1":
                        print_prompt()
                elif menuOption == "2":
                        order()
                elif menuOption == "3":
                        print_Order(False)
                elif menuOption == "4":
                        checkout()
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
        print("7) Print menu")
        print("8) Print current items")
        print("9) Remove an item")
        print("0) Return")
        menuTemp = input("")
        try:
                menuOption=int(menuTemp)
        except ValueError:
                print("That's not even a number!")
                order()
        if menuOption in range(1,6) or menuOption in range(8,10) or menuOption == 0:
                menuOption=str(menuOption)
                if menuOption == "0":
                        cli(False)
                elif menuOption == "9":
                        removeItem()
                elif menuOption == "8":
                        print_Order(False)
                elif menuOption == "7":
                        print_prompt()
                elif menuOption == "1" or menuOption == "4" or menuOption == "5":
                        orderBasics(menuOption)
                elif menuOption == "2":
                        orderPizzas(menuOption)
                elif menuOption == "3":
                        orderDrinks(menuOption)
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
        print("{:<5}{:<50}{}".format("#Num","Item Name","Price"))
        print("="*60)
        for item in range(len(menu[menuOption-1])):
                print("{:<5}{:<50}{}".format(
                str(item+1)+")",menu[menuOption-1][item][0],currency(menu[menuOption-1][item][2])))
        
        currentItemTemp=input("\nItem number: ")
        try:
                currentItem=int(currentItemTemp)-1
        except ValueError:
                orderError="Item not a number"
        if currentItem < 0:
                orderError = "Item number less than 1"
        elif currentItem >= len(menu[menuOption-1]):
                orderError="Item number higher total items"
        
        amount=input("Amount: ")
        try:
                amount=int(amount)
        except ValueError:
                orderError="Amount of item is not a number!"
        if amount <= 0:
                orderError="Amount of item is 0 or lower!"
        
        if orderError != False:
                print("orderError: {}".format(orderError))
                order()
        else:
                comment=str(input("Enter a comment, type in \"C\" to cancel or leave blank to confirm\n"))
                if comment.lower() == "c":
                        print("Cancelling item...")
                else:
                        currentItemList=[amount,menuOption-1,currentItem,"\n"+comment,menu[menuOption-1][currentItem][2]]
                        customerOrder.append(currentItemList)
                if 'debug' in globals():
                        print(customerOrder)

def orderPizzas(menuOption):
        # Ordering for Pizzas only, due to it's funky multi-sized formatting
        menuOption=int(menuOption)
        orderError=False
        print("\n")
        print(("{:<5}{:<50}"+"{:>10}"*4).format("#Num","Pizza Flavours","Small","Medium","Large","Monster"))
        print("="*95)
        for item in range(len(menu[menuOption-1])):
                print("{:<5}{:<50}{:>10}{:>10}{:>10}{:>10}".format(
                str(item+1)+")",
                menu[menuOption-1][item][0],
                currency(menu[menuOption-1][item][2]),
                currency(menu[menuOption-1][item][3]),
                currency(menu[menuOption-1][item][4]),
                currency(menu[menuOption-1][item][5])))
        
        currentItemTemp=input("\nItem number: ")
        try:
                currentItem=int(currentItemTemp)-1
        except ValueError:
                orderError="Item not a number"
        if currentItem < 0:
                orderError = "Item number less than 1"
        elif currentItem >= len(menu[menuOption-1]):
                orderError="Item number higher total items"
        
        # Size selection and verification system
        print("What size would you like?")
        print("1) Small")
        print("2) Medium")
        print("3) Large")
        print("4) Monster")
        size=input("Size: ")
        try:
                size=int(size)
        except ValueError:
                orderError="The size was not a number!"
        if size in range(1,5):
                if size == 1:
                        sizeComment="Small"
                elif size == 2:
                        sizeComment="Medium"
                elif size == 3:
                        sizeComment="Large"
                elif size == 4:
                        sizeComment="Monster"
                else:
                        orderError="Critical error in size checking, line ~318"
        else:
                if size <= 0:
                        orderError="Size was 0 or smaller"
                elif size >4:
                        orderError="Size was larger than 4(Maximum size)"
                else:
                        orderError="Critical error in size checking, line ~315"
        
        # Amount selection system
        amount=input("Amount: ")
        try:
                amount=int(amount)
        except ValueError:
                orderError="Amount of item is not a number!"
        if amount <= 0:
                orderError="Amount of item is 0 or lower!"
        
        if orderError != False:
                print("orderError: {}".format(orderError))
                order()
        else:
                comment=str(input("Enter a comment, type in \"C\" to cancel or leave blank to confirm\n"))
                if comment.lower() == "c":
                        print("Cancelling item...")
                else:
                        if comment == "":
                                currentItemList =[amount,menuOption-1,currentItem,sizeComment,menu[menuOption-1][currentItem][size+1]]
                        else:
                                currentItemList =[amount,menuOption-1,currentItem,sizeComment+"\n"+comment,menu[menuOption-1][currentItem][size+1]]
                        customerOrder.append(currentItemList)
                if 'debug' in globals():
                        print(customerOrder)

def orderDrinks(menuOption):
        # Ordering for Drinks only, due to it's funky size formatting
        menuOption=int(menuOption)
        orderError=False
        print("\n")
        print(("{:<5}{:<50}"+("{:>10}")*3).format("#Num","Item Name","Can","Bottle","2Liters"))
        print("="*85)
        for item in range(len(menu[menuOption-1])):
                print("{:<5}{:<50}{:>10}{:>10}{:>10}".format(
                str(item+1)+")",
                menu[menuOption-1][item][0],
                currency(menu[menuOption-1][item][2]),
                currency(menu[menuOption-1][item][3]),
                currency(menu[menuOption-1][item][3])))

        currentItemTemp=input("\nItem number: ")
        try:
                currentItem=int(currentItemTemp)-1
        except ValueError:
                orderError="Item not a number"
        if currentItem < 0:
                orderError = "Item number less than 1"
        elif currentItem >= len(menu[menuOption-1]):
                orderError="Item number higher total items"
                
        # Size selection and verification system
        print("What size would you like?")
        print("1) Can")
        print("2) Bottle")
        print("3) 2Liters")
        size=input("Size: ")
        try:
                size=int(size)
        except ValueError:
                orderError="The size was not a number!"
        if size in range(1,4):
                if size == 1:
                        sizeComment="Can"
                elif size == 2:
                        sizeComment="Bottle"
                elif size == 3:
                        sizeComment="2Liters"
                else:
                        orderError="Critical error in size checking, line ~381"
        else:
                if size <= 0:
                        orderError="Size was 0 or smaller"
                elif size >3:
                        orderError="Size was larger than 3(Maximum size)"
                else:
                        orderError="Critical error in size checking, line ~388"
                
        amount=input("Amount: ")
        try:
                amount=int(amount)
        except ValueError:
                orderError="Amount of item is not a number!"
        if amount <= 0:
                orderError="Amount of item is 0 or lower!"

        if orderError != False:
                print("orderError: {}".format(orderError))
                order()
        else:
                comment=str(input("Enter a comment, type in \"C\" to cancel or leave blank to confirm\n"))
                if comment.lower() == "c":
                        print("Cancelling item...")
                else:
                        if comment == "":
                                currentItemList =[amount,menuOption-1,currentItem,sizeComment,menu[menuOption-1][currentItem][size+1]]
                        else:
                                currentItemList =[amount,menuOption-1,currentItem,sizeComment+"\n"+comment,menu[menuOption-1][currentItem][size+1]]
                        customerOrder.append(currentItemList)
                if 'debug' in globals():
                        print(customerOrder)

def print_Order(numbers):
        totalCost=0
        if "debug" in globals():
                print(customerOrder)
                for i in range(len(customerOrder)):
                        print(customerOrder[i])
        
        for orderedItem in range(len(customerOrder)):
                if numbers:
                        print("{0}) {1}   {2}".format(
                                orderedItem+1, #Item number for identification
                                menu[customerOrder[orderedItem][1]][customerOrder[orderedItem][2]][0], # name
                                customerOrder[orderedItem][3])) # size (built into  the comment)
                else:
                        print("{0}   {1}".format(
                                menu[customerOrder[orderedItem][1]][customerOrder[orderedItem][2]][0],
                                customerOrder[orderedItem][3]))
                
                print("{0:<3}X {1:>5}{2:>50}".format(
                customerOrder[orderedItem][0], # amount of items
                currency(customerOrder[orderedItem][4]), # Single item cost
                currency((int(customerOrder[orderedItem][0])*int(customerOrder[orderedItem][4])))))
                totalCost+=int(customerOrder[orderedItem][0])*int(customerOrder[orderedItem][4])
        if numbers:
                print("Pick an item to remove")
        else:
                print("\nTotal:  {}".format(currency(totalCost)))

def removeItem():
        print_Order(True)
        itemToRemove=input("Item to remove: ")
        try:
                itemToRemove=int(itemToRemove)
        except ValueError:
                print("It's not a number!")
                removeItem()
        if itemToRemove in range(1,(len(customerOrder)+1)):
                del customerOrder[itemToRemove-1]
                print("Item deleted.\nHere is your current order")
                print_Order(False)
        else:
                if itemToRemove <= 0:
                        print("There is no item 0 or below...")
                        removeItem()
                else:
                        print("There is not item {}, it only goes up to {}!".format(str(itemToRemove),str(len(customerOrder+1))))
                        removeItem()

def checkout():
        global checkoutTime
        checkoutTime=strftime("%H%M%S", gmtime())
        print("Are you sure you want to place this order? After you do so you cannot change it!")
        confirm=input("\"Y\" for yes and \"N\" for no\n")
        if confirm.lower() == "y":
                sortByIndex(customerOrder,1)
                print_Order(False)
                orderToTxt()
                print("Your order will arive in:")
                countdown(20*60)
        elif confirm.lower() == "n":
                print("Okay.")
                cli(False)
        else:
                print("Sorry \"Y\" or \"N\" only")
                checkout()

def countdown(t):
        while t > 0:
                mins, secs = divmod(t, 60)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                print(timeformat, end='\r')
                sleep (1)
                t -= 1
        print('Times Up!!!\nYour Delivery should be here now!\nIf not call \"Big Rod\'s Pizza Directly at 999\"')

def orderToTxt():
        # A modded version of "print order"
        outputFile=open("orderOutput.txt","w")
        totalCost=0
        for orderedItem in range(len(customerOrder)):
                outputFile.write("\n") # gives a cushion so the outlook is easier it read
                outputFile.write("{0}   {1}\n".format(
                menu[customerOrder[orderedItem][1]][customerOrder[orderedItem][2]][0],
                customerOrder[orderedItem][3]))
                outputFile.write("{0:<3}X {1:>5}{2:>30}\n".format(
                customerOrder[orderedItem][0], # amount of items
                currency(customerOrder[orderedItem][4]), # Single item cost
                currency((int(customerOrder[orderedItem][0])*int(customerOrder[orderedItem][4])))))
                totalCost=totalCost+(int(customerOrder[orderedItem][0])*int(customerOrder[orderedItem][4]))
        outputFile.write("\nTotal:  {}".format(currency(totalCost)))
        outputFile.close()

def sortByIndex(inputList, index):
        inputList.sort(key=operator.itemgetter(index))

#Starts the "start" function and actully  boots the program
start()
