'''후기
뒤집어진 정삼각형을 만드는 문제다
'''

n = int(input())

for i in range(n,0,-1) :
    print(' '*(n-i)+'*'*(2*i-1))