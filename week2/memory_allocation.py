
n = int(input("Enter the number of requests: "))
server1 = 0
server2 = 0

print("Enter the requests (positive for allocation, negative for deallocation):")
for i in range(n):
    req = int(input())

    if i % 2 == 0:  
        server1 += req
    else:           
        server2 += req

print(f"Server 1 Memory Usage: {server1}")
print(f"Server 2 Memory Usage: {server2}")
