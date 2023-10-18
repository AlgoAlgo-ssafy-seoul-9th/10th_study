# 24042 횡단보도
# 296144 KB 2692 ms
import sys, heapq

input = sys.stdin.readline


def solution():
    # input
    N, M = map(int, input().split())
    # define
    graph = [[] for _ in range(N + 1)]
    # input & 그래프 생성
    for i in range(1, M + 1):
        s, e = map(int, input().split())
        graph[s].append((e, i))
        graph[e].append((s, i))
    # 방문 처리용 배열
    visited = [0] * (N + 1)
    # heapq 용 list
    que = []
    # 초기 setting (여태 걸린 시간, 차례, 위치)
    for next, w in graph[1]:
        heapq.heappush(que, (w, w, next))
    # dijkstra 시작
    while que:
        # 여태 걸린 시간, 차례, 현재 위치
        minute, idx, current = heapq.heappop(que)
        # 만약 도착 했다면 걸린 시간 print
        if current == N:
            print(minute)
            return
        # 이미 지나온 길이면 pass
        if visited[current]:
            continue
        # 지나온 길 체크
        visited[current] = 1
        # 갈 수 있는 곳 체크
        for next, w in graph[current]:
            # 지나온 길은 pass
            if visited[next]:
                continue
            # 만약 지금 차례가 다음 차례보다 작거나 같으면 다음 차례까지 기다려하므로 그 차이만큼 더해줌
            if idx >= w:
                heapq.heappush(que, (minute + (M - idx + w), w, next))
            # 만약 지금 차례가 다음 차례보다 크면 다음 차례와 현재 차례의 차이만큼만 더해줌
            else:
                heapq.heappush(que, (minute + (w - idx), w, next))

if __name__ == "__main__":
    solution()
