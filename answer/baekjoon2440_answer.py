'''후기
감소하는 for문에 대한 문제였다 !
Java였으면 쉽게 풀었을텐데 Python에서 감소하는 for문을 사용해 본 적이 없어서 잠깐 띠용 했다.
처음에 for문 형식을 어떻게 줘야하나 고민하다가 증가값을 음수로 주고 시작점을 n으로 해서 구현했다.
아무래도 Java를 배우고 Python은 찍먹 수준으로 배운 뒤 데이터 분석으로 넘어가서... 기본기가 좀 부족하구나 하고 느꼈다.
'''

n = int(input())

for i in range(n, 0, -1) :
    print('*' * i)