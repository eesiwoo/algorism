'''문제
서로 대칭인 직각삼각형 두 개를 출력하는 함수 만들기
'''

n = int(input())

for i in range(1,n+1) :
    print('*'*i + ' '*(n*2-i*2) + '*'*i)
for i in range(n-1,0,-1) :
    print('*'*i + ' '*(n*2-i*2) + '*'*i)