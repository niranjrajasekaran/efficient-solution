"""
Minimum Iteration required to make the two strings anagram
"""
from sys import stdin

def diff(l1, l2, unique_only=False):
    repeater_count, mismatch_count = 0, 0
    for i in set(l1):
        if i != '\n':
            if unique_only:
                if l1.count(i) != l2.count(i) and i in l2:
                    repeater_count += abs(l1.count(i) - l2.count(i))
            if i not in l2:
                mismatch_count += abs(l1.count(i) - l2.count(i))
    return repeater_count + mismatch_count

test_cases = int(stdin.readline())
for _ in range(test_cases):
    str1 = stdin.readline()[0:-1]
    str2 = stdin.readline()
    print(diff(str1, str2) + diff(str2, str1, unique_only=True))
