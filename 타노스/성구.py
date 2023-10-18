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
