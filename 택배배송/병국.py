import heapq


def djk(graph,start):
    INF = float('inf')
    distance = [INF]*(n+1)
    distance[start] = 0
    q = [(distance[start],start)]
    while q:
        now_dist, now = heapq.heappop(q)
        if now_dist > distance[now]: # 길면 볼필요없고 짧아야 볼건데,,
            continue
        for next, next_dist in graph[now]: # 그래프에서 꺼내서
            dist = now_dist+next_dist
            if dist < distance[next]:
                distance[next] = dist
                heapq.heappush(q,(dist,next))
    return distance


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
# print(graph)
print(djk(graph,1)[-1])