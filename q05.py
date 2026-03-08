NM = input().split()

N = int(NM[0])
M = int(NM[1])

arr = list(map(int,input().split()))

ans = 0
low, high = 0, max(arr)

while (high >= low):

    tot = 0
    mid = (high + low)//2

    for i in arr:
        if (i > mid):
            tot += (i - mid)

    if tot < M:
        high = mid - 1
    else:
        ans = mid
        low = mid + 1


print(ans)
