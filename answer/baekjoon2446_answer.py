'''후기
코딩 후 자꾸 출력형식 오류가 떴었다. 왜지..? 하고 고민하다가 문제 질문 예제들을 찾아봤다.
알고보니 별 오른쪽 부분에는 공백이 없었다..ㅎ 왜 당연히 있을거라고 생각했지..?
앞으로 출력 예제를 더 꼼꼼하게 봐야겠다.
'''

n = int(input())


for i in range(n,0,-1) :
    print(' '*(n-i) + '*'*((i*2)-1))

for i in range(2,n+1) :
    print(' '*(n-i) + '*'*((i*2)-1))