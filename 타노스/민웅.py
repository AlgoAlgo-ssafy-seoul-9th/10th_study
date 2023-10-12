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

