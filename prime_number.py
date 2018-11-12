"""
input() - will be the input to which the 
          range of prime numbers must be generated
print(.., end=' ') - will generate the ouput in the same line
"""
for i in range(2, int(input())):
    flag = False
    for j in range(2, i):
        if (i % j) == 0:
            flag = True
            break
    if flag is False:
        print(i, end=" ")
