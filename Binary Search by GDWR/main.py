# Binary Search Algorithm
# by GDWR


import random

list = []
num = random.randrange(1, 100)


# gets a list of numbers between 0 and 100 with a difference of 2 between each number.
running = True
while running:
    if num <= 100:
        list.append(num)
        num += 2
        continue
    else:
        running = False


def half(list, x):
    if x == 100:
        half = len(list) // 2 # int of half the list
        temp = list[half:len(list)] # gets from 0 to half of the list
        return temp
    if x == 0:
        half = len(list) // 2 # int of half the list
        temp = list[0:half] # gets from 0 to half of the list
        return temp


def middle(list):
    half = len(list) // 2 # int of half the list
    temp = list[half] # gets middle number of list
    return temp

print('pick a number 1 to 100')
input = int(input())

running2 = True
while running2:

    if len(list) == 0 or len(list) == 1:
        print('not in list')
        running2 = False
        break

    middleNum = middle(list)


    if input == middleNum:
        print('its in the list')

        running2 = False


    if input > middleNum:
        list = half(list, 100)

        continue

    if input < middleNum:
        list = half(list, 0)

        continue
