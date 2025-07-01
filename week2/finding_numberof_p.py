n= int(input())
x=int(input())
y=int(input())
a = list(map(int, input().split()))
a.sort()
print(a)

left = a[n - x - 1]
right = a[n - x]

if left < right:
    print(right - left - 1)
else:
    print(0)

