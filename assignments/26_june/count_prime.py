number=int(input("Enter a number"))
unique_digits=set(map(int , str(abs(number))))
count=0
for digit in unique_digits:
    if digit<=1 :
        print("not a prime ")
    else:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime number")
        else:
            print("Not a prime number")
count+=1

        