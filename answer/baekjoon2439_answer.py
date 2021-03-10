'''후기
처음에 주석처럼 풀어서 출력 오류가 났다 !
문제는 print할 때 , 를 사용하는 바람에 공백이 하나가 더 생긴 거였다.
, 대신에 +를 사용해서 다시 제출했다.
사소한 실수를 줄이자 !
'''

# n = int(input())
#
# for i in range(1, n+1) :
#     print(' '*(n-i),'*'*i)
    


n = int(input())

for i in range(1, n+1) :
    print(' '*(n-i)+'*'*i)