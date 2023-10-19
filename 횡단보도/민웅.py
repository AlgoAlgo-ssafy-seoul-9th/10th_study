# 24042_횡단보도_Crosswalk
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

cw = [[] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    cw[s].append([e, i])
    cw[e].append([s, i])

time = [float('inf')] * (N+1)

q = []
heapq.heappush(q, (0, 1))

while q:
    t, node = heapq.heappop(q)

    if t > time[node]:
        continue
    else:
        temp = []
        for n in cw[node]:
            if t%M == n[1]:
                weight = t + 1
            elif t%M < n[1]:
                weight = t + (n[1]-t%M)
            else:
                weight = t + (M - t % M) + n[1]

            if weight < time[n[0]]:
                time[n[0]] = weight
                heapq.heappush(q, (weight, n[0]))
if time[-1]+1 == 2:
    print(1)
else:
    print(time[-1]+1)
