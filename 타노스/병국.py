import copy
from collections import deque

S = list(input())
cnt_1 = 0
cnt_0 = 0
for i in range(len(S)):
    if S[i] == '1':
        cnt_1 += 1
    else:
        cnt_0 += 1
# 0 배치 먼저 하고 그다음 1 배치
cnt_1 //= 2
cnt_0 //= 2

check_0 = 0
check_1 = 0

new_arr = copy.copy(S)
del_arr = [0]*len(S)
for i in range(len(S)):
    if S[i] == '1' and check_1 < cnt_1:
        del_arr[i] = 1
        check_1 += 1
    else:
        pass
    if i >= 1 and S[-i] == '0' and check_0 < cnt_0:
        del_arr[-i] = 1
        check_0 += 1
    else:
        pass
# del_arr에서 1이면 삭제한다는거
# print(del_arr)



answer = ''
for i in range(len(del_arr)):
    if del_arr[i] == 0:
        # print(new_arr[i])
        answer += new_arr[i]
# print(del_arr)
print(answer)

