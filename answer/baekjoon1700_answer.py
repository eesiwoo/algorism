''' 후기
어제 풀었던 그리디 알고리즘은 진짜 아무것도 아니였구나... 하는 생각이 들었다.
알고리즘을 풀면서 고려해야할게 정말 많았다.
이미 꽂혀있을 때 앞으로 사용될 것인지, 더이상 사용될 일이 없는지 등 고려해야할게 많았다.
처음에 풀었을 때 잘 작동했는데 자꾸 오류나서 멘붕이 좀 왔었다. 틀린 코드긴 했지만...ㅎ

결국 혼자 해결을 못해서 구글링을 했고 다양한 방법으로 푼 것을 참고해서 다시 풀었는데 백준에서 통과를 못했당...ㅎ
마지막엔 블로그 배껴서 했는데도 통과가 안되더라... 왜그러지..?
다른 블로그를 참고해서 아예 새롭게 알고리즘을 풀었다.

내가 가장 실수한 부분은 더이상 사용하지 않는 전선을 제거하지 않은 것, 뒤에서부터 제거하려고 했던 것이였다.
'''
from sys import stdin
N, K = stdin.readline().split()
N = int(N)
K = int(K)
multap = [0] * N
li = list(map(int, stdin.readline().split()))
res = swap = num = max_I = 0
for i in li:
    if i in multap:
        pass
    elif 0 in multap:
        multap[multap.index(0)] = i
    else:
        for j in multap:
            if j not in li[num:]:
                swap = j
                break
            elif li[num:].index(j) > max_I:
                max_I = li[num:].index(j)
                swap = j
        multap[multap.index(swap)] = i
        max_I = swap = 0
        res += 1
    num += 1
print(res)