def dfs(x, y):
    if((x < 0) or (x >= N) or (y < 0) or (y >= M)):
        return
    
    if(graph[x][y] == '1'):
        return
    
    graph[x][y] = '1'

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    
NM = input().split()

N = int(NM[0])
M = int(NM[1])

graph = []

for i in range(N):
    graph.append(list(input()))


count = 0

for i in range(N):
    for j in range(M):
        if(graph[i][j] == '0'):
            dfs(i, j)
            count += 1

print(count)