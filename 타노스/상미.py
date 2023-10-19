S = str(input())

# 사전순 정렬을 위해 0은 앞에 최대한 많아야함
# 0과 1의 개수를 찾고
zero = 0 
one = 0
for s in S:
    if s == '0':
        zero += 1
    else:
        one += 1

# 0을 앞에서부터 제거/ 1은 뒤에서부터 제거
# 라고 생각했는데 반대가 맞음
cnt_0 = 0
cnt_1 = 0
for i in range(len(S)):
    if S[i] == '1':
        if i == 0:
            S = S[1:]
        else:
            S = S[:i] + S[i+1:]
        cnt_1 += 1
        if cnt_1 == one//2:
            break
for i in range(len(S)-1, 0, -1):
    if S[i] == '0':
        if i == len(S)-1:
            S = S[:-1]
        else:
            S = S[:i] + S[i+1:]
        cnt_0 += 1
        if cnt_0 == zero//2:
            break

print(S)