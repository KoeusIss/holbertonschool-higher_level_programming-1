#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    a = number * -1 % 10
    a = -a
else:
    a = number % 10
if a == 0:
    print("Last digit of {} is {} and is 0".format(number, a))
elif a < 6:
    print("Last digit of {} is {} and is\
 less than 6 and not 0".format(number, a))
else:
    print("Last digit of {} is {} and is greater than 5".format(number, a))
