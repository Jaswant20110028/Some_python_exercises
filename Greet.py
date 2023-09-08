# Time module
import time

# taking hour time from your system in 24 hours format 
# by default Hour will be str so typecast it in int
Hour=int(time.strftime('%H'))

# Applying comditions
# you can change them according to you
if Hour>=4 and Hour<12:
    print("Hello Sir, Good Morning !!")
if 17>Hour>=12:
    print("Hello Sir, Good Afternoon !!")
if 19>Hour>=17:
    print("Hello Sir, Good Evening !!")
else:
    print("Hello Sir, Good Night !!")


# When you will run this......
# this program will greet you