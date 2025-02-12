"""
Generate Array with Bitwise OR Condition:
Given two integers n and x, create an array of n positive integers such that
The array is strictly increasing.
For each number num[i] in the array, it satisfies the condition:
(num[i]|x)=x)
Return the last number in the generated array.
"""


def bitwise_or(n: int, x: int):
    array = []
    num = 1
    
    while len(array) < n:
        if (num|x) == x:
            array.append(num)
            num += 1
    return array

n = 4
x = 7

print(bitwise_or(n,x))


