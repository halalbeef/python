#!/usr/bin/env python

import csv


submenus=["starters", "pizzas", "drinks", "desserts", "extras"]
open("etc/"+submenus[0]+".csv")
print(csv.reader(open("etc/"+submenus[0]+".csv")))
