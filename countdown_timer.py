'''
A program to create a countdown timer using generator
------------
Python 3.7.0
------------
1.Create a Generator function countdown_timer
2.Iterate through the function a print countdown 

'''
import time
def countdown_timer(number):
    while number > 0:
        yield number
        number = number - 1
        time.sleep(1)

print("Starting countdown...")
for item in countdown_timer(5):
    print(item)

