'''후기
어떻게 만들까 고민을 좀 하다가 for문 2개를 이용하기로 했다.
숫자가 올라갔다가 내려가야 하는데 좋은 방법이 생각나지 않았다ㅠ
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