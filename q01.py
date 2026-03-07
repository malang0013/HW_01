while True:

    n = int(input())
    if((n>= 1) and (n<= 100)):
        break
    
while True:
    arr = list(input().split())
    if((len(arr)>= 1) and (len(arr)<= 100)):
        break

x = y = 1

for i in range(0,len(arr)):
    if((y == 1) and (arr[i] == 'L')):
        y = 1
    elif(arr[i] == 'L'):
        y -= 1

    if((y == n)) and (arr[i] == 'R'):
        y = n
    elif(arr[i] == 'R'):
        y += 1

    if((x == 1)) and (arr[i] == 'U'):
        x = 1
    elif(arr[i] == 'U'):
        x -= 1
    
    if((x == n)) and (arr[i] == 'D'):
        x = n
    elif(arr[i] == 'D'):
        x += 1


print(x, y)