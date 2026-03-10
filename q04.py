Nk= input().split()

N = int(Nk[0])
k = int(Nk[1])

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

for i in range(N):
    min = i
    for j in range(i+1, N):
        if (arr1[j] < arr1[min]):
            min = j
            arr1[i], arr1[min] = arr1[min], arr1[i]


for i in range(N):
    max = i
    for j in range(i+1, N):
        if (arr2[j] > arr2[max]):
            max = j
            arr2[i], arr2[max] = arr2[max], arr2[i]


for i in range(k):
    if (arr1[i] < arr2[i]):
        arr1[i], arr2[i] = arr2[i], arr1[i]

    else:
        break

print(sum(arr1))