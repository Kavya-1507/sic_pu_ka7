arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter the element to search: "))

low = 0
high = len(arr) - 1
found = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        found = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found != -1:
    print("Element found at index", found)
else:
    print("Element not found")
