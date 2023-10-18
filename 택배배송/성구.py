# 5972 택배 배송
# dijkstra 구현
# 50400 KB 184 ms python
import sys, heapq

input = sys.stdin.readline


def solution():
    # input
    N, M = map(int, input().split())
    # define
    graph = [[] for _ in range(N + 1)]
    # input & graph setting
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
    # 방문처리용 list
    visited = [0] * (N + 1)

    que = []

    for node, w in graph[1]:
        heapq.heappush(que, (w, node))

    while que:
        cost, current = heapq.heappop(que)
        if current == N:
            print(cost)
            return
        if visited[current]:
            continue
        visited[current] = 1
        for next, w in graph[current]:
            if visited[next]:
                continue
            heapq.heappush(que, (cost + w, next))


if __name__ == "__main__":
    solution()

""" bfs 구현
# 50036 KB 1484 ms python
import sys
from collections import deque

input = sys.stdin.readline

def solution():
    # input
    N, M = map(int, input().split())
    # define
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))

    visited = [50000001] * (N + 1)
    que = deque([])

    for a, c in graph[1]:
        visited[a] = c
        que.append(a)


    while que:
        now = que.popleft()
        for next, weight in graph[now]:
            if visited[now] + weight < visited[next]:
                que.append(next)
                visited[next] = visited[now] + weight
    print(visited[N])

if __name__ == "__main__":
    solution()
"""
