#my_number = 72930 # Change this number to test different values

# Convert the number to a string, then convert each character to an integer, and find the maximum
#biggest_digit = max(map(int, str(abs(my_number))))

#print(f"The biggest digit in {my_number} is: {biggest_digit}")



my_number = int(input("enter a number :"))

num_str = str(abs(my_number))

if not num_str: 
    biggest_digit = None 
else:
    biggest_digit = -1 

    for digit_char in num_str:
        digit = int(digit_char)
        if digit > biggest_digit:
            biggest_digit = digit


print(f"The number is: {my_number}")
print(f"The biggest digit in {my_number} is: {biggest_digit}")

