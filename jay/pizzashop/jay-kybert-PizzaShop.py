#/usr/bin/env python

from time import sleep#Imports sleep function for the 'for' loop.


def firstPizza ():#1st Option.
    global ordinaryCost
    print ("You chose the Ordinary Pizza. The details are listed below.\nPrice: £10.00\nSizes Available: small/medium/large\n")
    choice = int(input("How many do you want to purcahse?\n"))
    ordinaryCost = 10*(choice)
    print ("Total cost so far for this pizza: £",ordinaryCost,"\n")
    correct = input ("Is this information correct? (Y/N)\n")
    if correct == 'y' or correct == 'Y':
        print ("Thank you. Continuing...")
    else:
        firstPizza ()

def secondPizza ():#2nd Option.
    global pepperoniCost
    print ("You chose the Pepperoni Pizza. The details are listed below.\nPrice: £13.00\nSizes Available: medium/large\n")
    choice = int(input("How many do you want to purcahse?\n"))
    pepperoniCost = 13*(choice)
    print ("Total cost so far for this pizza: £",pepperoniCost,"\n")
    correct = input ("Is this information correct? (Y/N)\n")
    if correct == 'y' or correct == 'Y':
        print ("Thank you. Continuing...")
    else:
        secondPizza ()

def thirdPizza ():#3rd Option.
    global meatCost
    print ("You chose the Meat-Feast Pizza. The details are listed below.\nPrice: £11.00\nSizes Available: small/medium\n")
    choice = int(input("How many do you want to purcahse?\n"))
    meatCost = 11*(choice)
    print ("Total cost so far for this pizza: £",meatCost,"\n")
    correct = input ("Is this information correct? (Y/N)\n")
    if correct == 'y' or correct == 'Y':
        print ("Thank you. Continuing...")
    else:
        thirdPizza ()

def fourthPizza ():#4th Option.
    global vegeCost
    print ("You chose the Vegetarian Pizza. The details are listed below.\nPrice: £9.00\nSizes Available: small/medium/large\n")
    choice = int(input("How many do you want to purcahse?\n"))
    vegeCost = 9*(choice)
    print ("Total cost so far for this pizza: £",vegeCost,"\n")
    correct = input ("Is this information correct? (Y/N)\n")
    if correct == 'y' or correct == 'Y':
        print ("Thank you. Continuing...")
    else:
        fourthPizza ()

def fifthPizza ():#5th Option.
    global exoticCost
    print ("You chose the Exotic Pizza. The details are listed below.\nPrice: £15.00\nSizes Available: small/medium/large\n")
    choice = int(input("How many do you want to purcahse?\n"))
    exoticCost = 15*(choice)
    print ("Total cost so far for this pizza: £",exoticCost,"\n")
    correct = input ("Is this information correct? (Y/N)\n")
    if correct == 'y' or correct == 'Y':
        print ("Thank you. Continuing...")
    else:
        fifthPizza ()

def payment ():#Final Option.
    #Global Varaibles to allow the use of them in other subprograms.
    global choice
    global ordinaryCost
    global pepperoniCost
    global meatCost
    global vegeCost
    global exoticCost
    global loop

    print ("This is the price you payed for your Pizzas:\n1: Ordinary Pizza: £",ordinaryCost,"\n2: Pepperoni Pizza: £",pepperoniCost,"\n3 : Meat-Feast Pizza: £",meatCost,"\n4: Vegetarian Pizza: £",vegeCost,"\n5: Exotic Pizza: £",exoticCost,"\n")
    totalCost = ordinaryCost+pepperoniCost+meatCost+vegeCost+exoticCost#Variable for the Total Amount. Used in txt file later on.
    print ("The total price is",ordinaryCost+pepperoniCost+meatCost+vegeCost+exoticCost,"\n")
    finalChoice = input ("Is your final order correct? (Y/N)\n")
    if finalChoice == 'y' or finalChoice == 'Y':
        print ("We hope you enjoy your pizza. Thank you for using this app. A delivery vehicle will arrive shortly to the location.\n")
        print ("A text file has been created displaying your current order.")

        #txt Code below.   
        txtCreate = open ("Order_Receipt.txt","w")#Tells the program to create a file named 'Order_Receipt' if one isn't already created. Also the "w" allows us to write on the txt file.
        #Prints the cost of pizza variables on differnt lines along with some other text. 
        txtCreate.write ("Ordinary Pizza Cost: £")
        txtCreate.write ("%d" % ordinaryCost)
        txtCreate.write ("\n\n")
        txtCreate.write ("Pepperoni Pizza Cost: £")
        txtCreate.write ("%d" % pepperoniCost)
        txtCreate.write ("\n\n")
        txtCreate.write ("Meat-Feast Pizza Cost: £")
        txtCreate.write ("%d" % meatCost)
        txtCreate.write ("\n\n")
        txtCreate.write ("Vegetarian Pizza Cost: £")
        
        txtCreate.write ("%d" % vegeCost)
        txtCreate.write ("\n\n")
        txtCreate.write ("Exotic Pizza Cost: £")
        txtCreate.write ("%d" % exoticCost)
        txtCreate.write ("\n\n")
        txtCreate.write ("Total Amount: £")
        txtCreate.write ("%d" % totalCost)
        txtCreate.write ("\nWe hope you enjoy your meal.\nIt should arrive within 20 minutes. Thank you.\n")
        txtCreate.close ()#Signifies the end of the txt file.
        txtRead = txtCreate.read
        print (txtRead)#Prints the txt file made above.


        print ("A countdown has initiated showing you how many seconds until your order will arrive. (approx. 20 mintues)\n")
        for t in range (0,1200):#Simple for loop. 20 minutes in seconds
            print (1200-t)
            sleep (1)
            
        print ("Your order should arrive any second now. We hope you enjoy.")
        loop = False
    else:
        print ("Ok. Redirecting you now.")
        loop = True


print ("Welcome to the Pizza Delivery App.\n")#Welcome messege. Code starts here.
loop = True#Simple loop to allowed the code to stop/start at given points throughout the code.
while loop == True:
    choice = input("Our current selection offers all of these:\n1: Ordinary Pizza\n2: Pepperoni Pizza\n3: Meat-Feast Pizza\n4: Vegetarian Pizza\n5: Exotic Pizza\n6: Payment (Please enter a purcahse for all products please before clicking this)\nPlease enter the corrosponding number to view our product in more depth.\n")
    #Redirects users to the subprograms above.
    if choice =='1':
        firstPizza ()
    elif choice =='2':
         secondPizza ()
    elif choice =='3':
        thirdPizza ()
    elif choice =='4':
        fourthPizza ()
    elif choice =='5':
        fifthPizza ()
    elif choice =='6':
        payment ()
    else:
        print ("Thank you for your time.")
        loop = False
