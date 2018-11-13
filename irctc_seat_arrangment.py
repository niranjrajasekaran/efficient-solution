"""
Says the seat number just opposite to the given seat number, 
Tested again 2S(Second Sitting) Coach
"""

from sys import stdin

for eachcase in range(test_cases):
    seat_number = int(stdin.readline())
    qu = seat_number // 6
    re = seat_number % 6
    if re == 0:
        if qu % 2 == 0:
            print(seat_number - 11, end='')
        else:
            print(seat_number + 1, end='')
        print(" WS")
    elif re == 1:
        if qu % 2 == 0:
            print(seat_number + 11, end='')
        else:
            print(seat_number - 1, end='')
        print(" WS")
    elif re == 2:
        if qu % 2 == 0:
            print(seat_number + 9, end='')
        else:
            print(seat_number - 3, end='')
        print(" MS")
    elif re == 5:
        if qu % 2 == 0:
            print(seat_number + 3, end='')
        else:
            print(seat_number -9, end='')
        print(" MS")
    elif re == 3:
        if qu % 2 == 0:
            print(seat_number + 7, end='')
        else:
            print(seat_number - 5, end='')
        print(" AS")
    elif re == 4:
        if qu % 2 == 0:
            print(seat_number + 5, end='')
        else:
            print(seat_number - 7, end='')
        print(" AS")
