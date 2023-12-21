# bfs
from collections import deque
def bfs(i):
    deq = deque()
    dist = [-1] * N
    deq.append(i)
    dist[i] = 0
    while deq:
        v = deq.popleft()
        for e in edge[v]:
            if dist[e] != -1:
                continue
            dist[e] = dist[v] + 1
            deq.append(e)
    return dist

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)