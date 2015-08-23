import csv

var1=input("var one plox\n")
var2=input("var 2 will be gud\n")
var3=input("slap me up with var\n")

filevar=open("memes.csv","w")
filevarWrite=csv.writer(filevar)
filevarWrite.writerow([var1,var2,var3])
filevar.close
