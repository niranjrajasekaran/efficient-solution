from sys import stdin

for i in range(2, int(stdin.readline())):
    flag = False
    for j in range(2, i):
        if (i % j) == 0:
            flag = True
            break
    if flag is False:
        print(i, end=" ")
