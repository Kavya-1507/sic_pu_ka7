str1=input()
str2=input()
if len(str1)!=len(str2):
    print(-1) 
else:
    temp=str1+str2
    if str2 in temp:
        print(1) 
    else:
        print(-1)
