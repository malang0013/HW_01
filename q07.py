NM = input().split()

N = int(NM[0])
M = int(NM[1])

INF = int(1e9)

graph =[]

for i in range(N+1):
    graph.append([INF]*(N+1))

for i in range(1, N+1):
    graph[i][i] = 0

for i in range (M) :
    ab = input().split()

    a = int(ab[0])
    b = int(ab[1])

    graph[a][b] = 1
    graph[b][a] = 1

XK = input().split()

X = int(XK[0])
K = int(XK[1])

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][X] + graph[X][K]

if (distance >= INF):
    print("-1")

else: 
    print(distance)