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
