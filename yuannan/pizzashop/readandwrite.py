#!/usr/bin/env python
#testing read and write for my stuff
import csv
starter = open("etc/starters.csv")

csv_starter = csv.reader(starter)

for blah in csv_starter:
	print(blah)
print(csv_starter)
starter.close
