# 24042_택배배송_delivery-service
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [float('inf')]*(N+1)
visited[1] = 0
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    s, g, c = map(int, input().split())
    adjL[s].append([g, c])
    adjL[g].append([s, c])

q = []
heapq.heappush(q, (0, 1))
while q:
    cost, node = heapq.heappop(q)
    if visited[node] < cost:
        continue

    for v in adjL[node]:
        c = cost + v[1]

        if visited[v[0]] > c:
            visited[v[0]] = c
            heapq.heappush(q, (c, v[0]))

print(visited[-1])