'''후기
역순 + 공백과 함께 찍는 문제이다. 아직까진 어려움 없음!
'''

n = int(input())

for i in range(n, 0, -1) :
    print(' '*(n-i)+'*' * i)