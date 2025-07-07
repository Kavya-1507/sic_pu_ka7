
n = int(input("Enter size: "))
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
print("Sorted array:", arr)
x = int(input("Enter element to search: "))
def bs(arr, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return bs(arr, mid + 1, high, x)
    else:
        return bs(arr, low, mid - 1, x)

res = bs(arr, 0, n - 1, x)

if res != -1:
    print("Found at index", res)
else:
    print("Not found")
