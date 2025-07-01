number=int(input("Enter the number:"))
each_digit=set(map(int , str(abs(number)))) 
sorted_each_digit=sorted(each_digit)
if len(sorted_each_digit)<2:
    if number==0:
        print("there are no digits in th enumber")
    else :
        print("digits in number are lesser than 2 to compare")
else :
    second_smallest=sorted_each_digit[1]
    print(second_smallest)


    

