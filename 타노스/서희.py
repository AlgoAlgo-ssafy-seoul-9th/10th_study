import sys
input = sys.stdin.readline

S = list(input())

zero = S.count("0") // 2
one = S.count("1") //2

# 0은 뒤에서부터 지우고 1은 앞에서부터 지워서 합치기
for _ in range(zero):
    S.pop(-S[::-1].index("0")-1)
for _ in range(one):
    S.pop(S.index("1"))
    
print("".join(S))
