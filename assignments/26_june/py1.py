import math

# Input from the user
num = int(input("Enter a number: "))

# Find square root and check if it's an integer
if math.isqrt(num) ** 2 == num:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")
