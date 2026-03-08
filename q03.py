from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            xs = x + dx[i]
            ys = y + dy[i]

            if((xs < 0) or (xs >= N) or (ys < 0) or (ys >= M)):
                continue
            
            if(graph[xs][ys] == 0):
                continue
            
            if(graph[xs][ys] == 1):
                graph[xs][ys] = graph[x][y] + 1
                queue.append((xs,ys))

    return graph[N-1][M-1]
               
    
NM = input().split()

N = int(NM[0])
M = int(NM[1])

graph = []

for i in range(N):
    graph.append(list(map(int,input()))) 


print(bfs(0,0))