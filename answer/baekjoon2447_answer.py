'''후기
재귀 또는 분할 정복으로 푸는 문제였다.
빈 공간의 경우 3으로 나눈 나머지값이 1인 경우 빈 공간인 규칙이였다.
생각을 구현하는게 꽤 어려워서 인터넷의 도움을 받았다.
'''
n = int(input())
k = 0


while n != 3:
    n = int(n / 3)
    k += 1

def stars(star):
    matrix=[]
    for i in range(3 * len(star)):
        print(i)
        if i // len(star) == 1:
            matrix.append(star[i % len(star)] + " " * len(star) + star[i % len(star)])
        else:
            matrix.append(star[i % len(star)] * 3)
    return(list(matrix))

star = ["***","* *","***"]
for i in range(k):
    star = stars(star)
for i in star:
    print(i)