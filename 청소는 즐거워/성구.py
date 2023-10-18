import sys
import math as Math
input = sys.stdin.readline

def dust_cal(direction, i, j, length, direc):
    # 먼지 계산
    global field, n
    out_dust = 0
    if direction == 0:
        ni, nj = i, j
        for t in range(length):
            ni, nj = ni + direc[direction][0], nj + direc[direction][1]
            if ni <= 0 and nj <= -1:
                return out_dust
            per1 = Math.floor(field[ni][nj] * 0.01)
            per2 = Math.floor(field[ni][nj] * 0.02)
            per5 = Math.floor(field[ni][nj] * 0.05)
            per7 = Math.floor(field[ni][nj] * 0.07)
            per10 = Math.floor(field[ni][nj] * 0.1)
            per_rest = field[ni][nj] - (per1*2 + per2*2 + per5 + per7*2 + per10*2)
            field[ni][nj] = 0
            # percent 1
            if 0 <= ni-1 < n and 0 <= nj +1 < n:
                field[ni-1][nj+1] += per1
            else:
                out_dust += per1
            if 0 <= ni+1 < n and 0 <= nj +1 < n:
                field[ni+1][nj+1] += per1
            else:
                out_dust += per1
            # percent 2
            if 0 <= ni -2 < n and 0<= nj < n:
                field[ni-2][nj] += per2
            else:
                out_dust += per2
            if 0 <= ni +2 < n and 0<= nj < n:
                field[ni+2][nj] += per2
            else:
                out_dust += per2

            # percent 5
            if 0 <= ni < n and 0 <= nj -2 < n:
                field[ni][nj-2] += per5
            else:
                out_dust += per5
            # percent 7
            if 0 <= ni+1 < n and 0 <= nj < n:
                field[ni+1][nj] += per7
            else:
                out_dust += per7
            if 0 <= ni-1 < n and 0 <= nj < n:
                field[ni-1][nj] += per7
            else:
                out_dust += per7
            # percent 10
            if 0 <= ni-1 < n and 0 <= nj-1 < n:
                field[ni-1][nj-1] += per10
            else:
                out_dust += per10
            if 0 <= ni+1 < n and 0 <= nj-1 < n:
                field[ni+1][nj-1] += per10
            else:
                out_dust += per10
            # rest
            if 0 <= ni < n and 0 <= nj-1 < n:
                field[ni][nj-1] += per_rest
            else:
                out_dust += per_rest

            
    elif direction == 1:
        ni, nj = i, j
        for t in range(1, length+1):
            ni, nj = ni + direc[direction][0], nj + direc[direction][1]
            per1 = Math.floor(field[ni][nj] * 0.01)
            per2 = Math.floor(field[ni][nj] * 0.02)
            per5 = Math.floor(field[ni][nj] * 0.05)
            per7 = Math.floor(field[ni][nj] * 0.07)
            per10 = Math.floor(field[ni][nj] * 0.1)
            per_rest = field[ni][nj] - (per1*2 + per2*2 + per5 + per7*2 + per10*2)
            field[ni][nj] = 0
            # percent 1
            if 0 <= ni-1 < n and 0 <= nj -1 < n:
                field[ni-1][nj-1] += per1
            else:
                out_dust += per1
            if 0 <= ni-1 < n and 0 <= nj +1 < n:
                field[ni-1][nj+1] += per1
            else:
                out_dust += per1
            # percent 2
            if 0 <= ni < n and 0<= nj-2 < n:
                field[ni][nj-2] += per2
            else:
                out_dust += per2
            if 0 <= ni < n and 0<= nj+2 < n:
                field[ni][nj+2] += per2
            else:
                out_dust += per2
            # percent 5
            if 0 <= ni+2 < n and 0 <= nj < n:
                field[ni+2][nj] += per5
            else:
                out_dust += per5
            # percent 7
            if 0 <= ni < n and 0 <= nj-1 < n:
                field[ni][nj-1] += per7
            else:
                out_dust += per7
            if 0 <= ni < n and 0 <= nj+1 < n:
                field[ni][nj+1] += per7
            else:
                out_dust += per7
            # percent 10
            if 0 <= ni+1 < n and 0 <= nj-1 < n:
                field[ni+1][nj-1] += per10
            else:
                out_dust += per10
            if 0 <= ni+1 < n and 0 <= nj+1 < n:
                field[ni+1][nj+1] += per10
            else:
                out_dust += per10
            # rest
            if 0 <= ni+1 < n and 0 <= nj < n:
                field[ni+1][nj] += per_rest
            else:
                out_dust += per_rest

    elif direction == 2:
        ni, nj = i, j
        for t in range(1, length+1):
            ni, nj = ni + direc[direction][0], nj + direc[direction][1]
            per1 = Math.floor(field[ni][nj] * 0.01)
            per2 = Math.floor(field[ni][nj] * 0.02)
            per5 = Math.floor(field[ni][nj] * 0.05)
            per7 = Math.floor(field[ni][nj] * 0.07)
            per10 = Math.floor(field[ni][nj] * 0.1)
            per_rest = field[ni][nj] - (per1*2 + per2*2 + per5 + per7*2 + per10*2)
            field[ni][nj] = 0
            # percent 1
            if 0 <= ni-1 < n and 0 <= nj -1 < n:
                field[ni-1][nj-1] += per1
            else:
                out_dust += per1
            if 0 <= ni+1 < n and 0 <= nj -1 < n:
                field[ni+1][nj-1] += per1
            else:
                out_dust += per1
            # percent 2
            if 0 <= ni -2 < n and 0<= nj < n:
                field[ni-2][nj] += per2
            else:
                out_dust += per2
            if 0 <= ni +2 < n and 0<= nj < n:
                field[ni+2][nj] += per2
            else:
                out_dust += per2
            # percent 5
            if 0 <= ni < n and 0 <= nj+2 < n:
                field[ni][nj+2] += per5
            else:
                out_dust += per5
            # percent 7
            if 0 <= ni-1 < n and 0 <= nj < n:
                field[ni-1][nj] += per7
            else:
                out_dust += per7
            if 0 <= ni+1 < n and 0 <= nj < n:
                field[ni+1][nj] += per7
            else:
                out_dust += per7
            # percent 10
            if 0 <= ni-1 < n and 0 <= nj+1 < n:
                field[ni-1][nj+1] += per10
            else:
                out_dust += per10
            if 0 <= ni+1 < n and 0 <= nj+1 < n:
                field[ni+1][nj+1] += per10
            else:
                out_dust += per10
            # rest
            if 0 <= ni < n and 0 <= nj+1 < n:
                field[ni][nj+1] += per_rest
            else:
                out_dust += per_rest
    else:
        ni, nj = i, j
        for t in range(1, length+1):
            ni, nj = ni + direc[direction][0], nj + direc[direction][1]
            per1 = Math.floor(field[ni][nj] * 0.01)
            per2 = Math.floor(field[ni][nj] * 0.02)
            per5 = Math.floor(field[ni][nj] * 0.05)
            per7 = Math.floor(field[ni][nj] * 0.07)
            per10 = Math.floor(field[ni][nj] * 0.1)
            per_rest = field[ni][nj] - (per1*2 + per2*2 + per5 + per7*2 + per10*2)
            field[ni][nj] = 0
            # percent 1
            if 0 <= ni+1 < n and 0 <= nj -1 < n:
                field[ni+1][nj-1] += per1
            else:
                out_dust += per1
            if 0 <= ni+1 < n and 0 <= nj +1 < n:
                field[ni+1][nj+1] += per1
            else:
                out_dust += per1
            # percent 2
            if 0 <= ni < n and 0<= nj-2 < n:
                field[ni][nj-2] += per2
            else:
                out_dust += per2
            if 0 <= ni < n and 0<= nj+2 < n:
                field[ni][nj+2] += per2
            else:
                out_dust += per2
            # percent 5
            if 0 <= ni-2 < n and 0 <= nj < n:
                field[ni-2][nj] += per5
            else:
                out_dust += per5
            # percent 7
            if 0 <= ni < n and 0 <= nj-1 < n:
                field[ni][nj-1] += per7
            else:
                out_dust += per7
            if 0 <= ni < n and 0 <= nj+1 < n:
                field[ni][nj+1] += per7
            else:
                out_dust += per7
            # percent 10
            if 0 <= ni-1 < n and 0 <= nj-1 < n:
                field[ni-1][nj-1] += per10
            else:
                out_dust += per10
            if 0 <= ni-1 < n and 0 <= nj+1 < n:
                field[ni-1][nj+1] += per10
            else:
                out_dust += per10
            # rest
            if 0 <= ni-1 < n and 0 <= nj < n:
                field[ni-1][nj] += per_rest
            else:
                out_dust += per_rest
    return out_dust


def solution(n, field):
    # 회전 이동
    out_dust = 0
    # 방향 좌, 아래, 우, 위
    direc = [(0, -1), (1,0), (0,1), (-1,0)]
    length = cnt = 1
    # 현재 위치
    curr_i, curr_j = n//2, n//2
    while length <= n:        
        if length % 2:
            out_dust += dust_cal(0, curr_i, curr_j, length,direc)
            curr_i += direc[0][0]*length
            curr_j += direc[0][1]*length
            # print(out_dust)
            if length == n:
                break
            out_dust += dust_cal(1, curr_i, curr_j, length,direc)
            curr_i += direc[1][0]*length
            curr_j += direc[1][1]*length
            # print(out_dust)
        else:
            out_dust += dust_cal(2, curr_i, curr_j, length,direc)
            curr_i += direc[2][0]*length
            curr_j += direc[2][1]*length
            # print(out_dust)
            out_dust += dust_cal(3, curr_i, curr_j, length,direc)
            curr_i += direc[3][0]*length
            curr_j += direc[3][1]*length
            # print(out_dust)
        length += 1

    print(out_dust)


if __name__ == "__main__":
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]

    solution(n, field)