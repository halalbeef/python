#/usr/bin/env python
#
#A quick and simple script that output a "run and replace" timer
#Can be change to anything, but currently support it in minutes max
#Easily modded to create a a hours option

import time
from time import sleep

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        sleep (1)
        t -= 1
    print('Times Up!!!')


