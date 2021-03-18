'''문제
마름모 모양으로 별 찍기
'''

def solve():
    n = int(input())
    star(n)


def star(n):
    for i in range(1,n) :
        print(' '*(n-i)+'*'*(2*i-1))
    for i in range(n,0,-1) :
        print(' '*(n-i)+'*'*(2*i-1))
        
solve()