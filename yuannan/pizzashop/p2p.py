def currency(money):
        money=str(money)
        whole=money[:-2]
        units=money[-2:]
        if len(whole) < 1:
                whole="0"
        while len(units) < 2:
                units="0"+units
        return("£"+whole+"."+units)

for i in range(0,101):
    print(currency(i))
