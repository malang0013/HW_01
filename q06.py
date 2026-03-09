n = int(input())

arr = [0]* 91

arr[1] = 1
arr[2] = 1

def fibo(x):
    if (x == 1) or (x == 2):
        return 1
    
    if arr[x] != 0:
        return arr[x]
    
    arr[x] = fibo(x-1) + fibo(x-2)
    return arr[x]

fibo(n)

for i in range(n):
    print(arr[i], end=", ")

print(arr[n])