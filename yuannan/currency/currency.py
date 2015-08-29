#/usr/bin/env python
#Converts 123 into £1.23

def currency(money):
        money=str(money) # Converts to a string for later handeling
        whole=money[:-2]
        units=money[-2:]
        if len(whole) < 1:
                whole="0"
        while len(units) < 2:
                units="0"+units
        return("£"+whole+"."+units) #Change "£" accordingly
