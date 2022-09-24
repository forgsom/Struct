from random import random

def search(array, number):
    flag = False
    k = 0
    for i in array:
        k += 1
        if i == number:
            flag = True
            return flag, k

def binarySearch(array, number):
    first = 0
    last = len(array) - 1
    flag = False
    k = 0
    while first <= last and not flag:
        k += 1
        middle = (first + last) // 2
        guess = array[middle]
        if guess == number:
            flag = True
            return flag, k
        elif guess > number:
            last = middle - 1
        else:
            first = middle + 1
    return flag, k

array = []
for i in range(10):
    array.append(random()//0.01)

array = sorted(array)
print(array, "\n")
number = float(input("Enter number "))
print(search(array, number),"\n\n")
print(binarySearch(array, number))