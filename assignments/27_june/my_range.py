def my_range(*args):
    if len(args)== 0 or len(args)<3 or type(agrs[0]) is not int:
        raise TypeError
    if len(args)==1:
        i=0
        while i<args[0]:
            yield i 
            i +=1
    elif len(args)== 2 :
        i=args[0]
        while i<args[1]:
            yield i
            i +=1
    elif len(args)==3 :
        

number_lines=int(input("enter number of lines:"))
for i in my_range(n):
    print('@'*number_lines)