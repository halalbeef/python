import time

def countdown(t):
    while time:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time -= 1
    print('Times Up!!!')
