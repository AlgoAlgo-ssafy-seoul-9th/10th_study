# 10th_study

[백준 문제집](https://www.acmicpc.net/workbook/view/17097)

[코드트리 문제](https://www.codetree.ai/training-field/frequent-problems/problems/cleaning-is-joyful/submissions?page=2&pageSize=20)

<br><br>

# 청소는 즐거워

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./청소는 즐거워/민웅.py>)

```py
import sys
input = sys.stdin.readline
from collections import deque
import math

# 왼
dir1 = [(1, 0, 7), (2, 0, 2), (-1, 0, 7), (-2, 0, 2), (1, -1, 10), (-1, -1, 10), (1, 1, 1), (-1, 1, 1), (0, -2, 5),
        (0, -1, 0)]
# 아
dir2 = [(0, 1, 7), (0, 2, 2), (0, -1, 7), (0, -2, 2), (1, -1, 10), (1, 1, 10), (-1, -1, 1), (-1, 1, 1), (2, 0, 5),
        (1, 0, 0)]
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
ans = 0

direction = deque()
for i in range(1, N + 1):
    if i != N:
        direction.append(i)
        direction.append(i)
    else:
        direction.append(i)

now_direction = [0, 1, 2, 3]
left_down = True
s = N // 2

i, j = s, s
stack = []
stack.append([i, j])
d_idx = 0

while stack:
    x, y = stack.pop()
    if x == 0 and y == -1:
        break

    length = direction.popleft()
    way = d_idx % 4
    while length:
        move_x, move_y = move[way][0], move[way][1]
        x = x + move_x
        y = y + move_y
        dust = field[x][y]
        field[x][y] = 0
        if way == 0:
            temp = 0
            for d in dir1:
                mx, my, p = x + d[0], y + d[1], d[2]

                if 0 <= mx <= N - 1 and 0 <= my <= N - 1:
                    if p == 0:
                        field[mx][my] = field[mx][my] + (dust - temp)
                    else:
                        field[mx][my] = field[mx][my] + int(math.floor((dust * p / 100)))
                        temp += int(math.floor((dust * p / 100)))
                else:
                    if p == 0:
                        ans += (dust - temp)
                    else:
                        ans += int(math.floor((dust * p / 100)))
                        temp += int(math.floor((dust*p/100)))
        elif way == 1:
            temp = 0
            for d in dir2:
                mx, my, p = x + d[0], y + d[1], d[2]

                if 0 <= mx <= N - 1 and 0 <= my <= N - 1:
                    if p == 0:
                        field[mx][my] = field[mx][my] + (dust - temp)
                    else:
                        field[mx][my] = field[mx][my] + int(math.floor((dust * p / 100)))
                        temp += int(math.floor((dust * p / 100)))
                else:
                    if p == 0:
                        ans += (dust - temp)
                    else:
                        ans += int(math.floor((dust * p / 100)))
                        temp += int(math.floor((dust*p/100)))
        elif way == 2:
            temp = 0
            for d in dir1:
                mx, my, p = x + d[0], y + -1 * d[1], d[2]

                if 0 <= mx <= N - 1 and 0 <= my <= N - 1:
                    if p == 0:
                        field[mx][my] = field[mx][my] + (dust - temp)
                    else:
                        field[mx][my] = field[mx][my] + int(math.floor((dust * p / 100)))
                        temp += int(math.floor((dust * p / 100)))
                else:
                    if p == 0:
                        ans += (dust - temp)
                    else:
                        ans += int(math.floor((dust * p / 100)))
                        temp += int(math.floor((dust*p/100)))
        else:
            temp = 0
            for d in dir2:
                mx, my, p = x + -1 * d[0], y + d[1], d[2]

                if 0 <= mx <= N - 1 and 0 <= my <= N - 1:
                    if p == 0:
                        field[mx][my] = field[mx][my] + (dust - temp)
                    else:
                        field[mx][my] = field[mx][my] + int(math.floor((dust * p / 100)))
                        temp += int(math.floor((dust * p / 100)))
                else:
                    if p == 0:
                        ans += (dust - temp)
                    else:
                        ans += int(math.floor((dust * p / 100)))
                        temp += int(math.floor((dust*p/100)))

        length -= 1
    stack.append([x, y])
    d_idx += 1
print(ans)

```

## [병국](<./청소는 즐거워/병국.py>)

```py

```

## [상미](<./청소는 즐거워/상미.py>)

```py

```

## [서희](<./청소는 즐거워/서희.py>)

```py

```

## [성구](<./청소는 즐거워/성구.py>)

```py


```

</div>

</details>

<br><br>

# 타노스

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./타노스/민웅.py)

```py
# 20310_타노스_thanos
import sys
input = sys.stdin.readline

zeroone = list(input().strip())

zero = zeroone.count('0')
one = zeroone.count('1')

zero = zero//2
one = one//2
idx, idx2 = 0, len(zeroone)-1

while True:
    if one == 0:
        break

    if zeroone[idx] == '1':
        zeroone.pop(idx)
        one -= 1
        idx2 -= 1
    else:
        idx += 1

while True:
    if zero == 0:
        break

    if zeroone[idx2] == '0':
        zeroone.pop(idx2)
        zero -= 1
        idx2 -= 1
    else:
        idx2 -= 1

print(''.join(zeroone))


```

## [병국](./타노스/병국.py)

```py


```

## [상미](./타노스/상미.py)

```py

```

## [서희](./타노스/서희.py)

```py


```

## [성구](./타노스/성구.py)

```py
# 20310 타노스
import sys

input = sys.stdin.readline

# input
S = input().strip()

# 1과 0 개수
one = S.count("1")
zero = S.count("0")

# 날릴 절반 구하기
one //= 2
zero //= 2

# 길이 미리 저장
length = len(S)
# 바뀐 값 저장할 S list 생성
S_list = list(S)

# 투 포인터 구현
i = 0
j = length - 1

while i < length and j >= 0:
    # 마지막 인덱스부터 첫번째 인덱스까지 총 0개수의 절반만큼 0을 발견하면 제거
    if S[j] == "0" and zero:
        S_list[j] = ""
        zero -= 1
    # 첫번째 인덱스부터 마지막 인덱스까지 총 1개수의 절반만큼 1을 발견하면 제거
    if S[i] == "1" and one:
        S_list[i] = ""
        one -= 1
    i += 1
    j -= 1
print("".join(S_list))

```

</div>

</details>

<br><br>

# 택배배송

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./택배배송/민웅.py)

```py
# 24042_택배배송_delivery-service
# python3 - 280ms
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
```

## [병국](./택배배송/병국.py)

```py


```

## [서희](./택배배송/서희.py)

```py

```

## [성구](./택배배송/성구.py)

```py


```

</div>

</details>

<br><br>

# 횡단보도

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./횡단보도/민웅.py)

```py


```

## [병국](./횡단보도/병국.py)

```py

```

## [상미](./횡단보도/상미.py)

```py

```

## [서희](./횡단보도/서희.py)

```py

```

## [성구](./횡단보도/성구.py)

```py

```

</div>

</details>

<br><br>
