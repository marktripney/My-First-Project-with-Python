# Importing the necessary math library
import math


# Function to find the largest power of 2 less than or equal to 'n'
def largestPower(n):
    # Start coding here
    exp = 1
    while math.pow(2, exp) <= n:
        if math.pow(2, exp + 1) <= n:
            exp += 1
        else:
            return math.pow(2, exp)


# Take the input n
n = int(input())

print(int(largestPower(n)))

# Smart solution! 👇 (but doesn't use while loop)...
# Binary logarithm is is the power to which the number 2 must be raised to obtain the value n.

# def largestPower(n):
#     return 2 ** math.floor(math.log2(n))
#
# # Take the input n
# n = int(input())
#
# print(largestPower(n))
