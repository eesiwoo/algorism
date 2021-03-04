''' 문제
기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다.

준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다.

그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.

예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면, 

키보드
헤어드라이기
핸드폰 충전기
디지털 카메라 충전기
키보드
헤어드라이기

키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다. 
'''
def solve():
    n, m = map(int, input().split())
    stuff = list(map(int, input().split()))
    reverseStuff = list(reversed(stuff))
    multitab = []
    for i in range(n):
        multitab.append(stuff[i])
    greedy(n, m, multitab, stuff, reverseStuff)  
    
# 3구 멀티탭 / 사용할 stuff 1 2 3 4 2 5 2 1 4 2 3 1 5
#  234 / 254 / 214 / 214에서 3을 꼽아야하는데 기존 로직은 1을 뽑으라고 함. 그러면 일을 또 해야하므로 기존 로직을 뒤집어야함     
def greedy(n, m, multitab, stuff, reverseStuff):
    result = 0
    for i in range(m): # stuff 순서대로 멀티탭에 꼽기
        for ii in range(len(multitab)): # stuff가 이미 multitab에 있는지 확인
            if stuff[i] == multitab[ii] : # 이미 꼽혀있다면 아무것도 하지 않음
                pass
            
            else : # 꼽혀있지 않다면 기존 것을 제거하고 새로 꼽음
                if m - i > n : # 나중에 쓰일 stuff부터 제거하고 꼽기
                    for iii in range(len(reverseStuff)):
                        if reverseStuff[iii] != multitab[ii] :
                            continue
                        else :
                            multitab[ii] = stuff[i]
                            result += 1
                            break
                else : # 남은 stuff의 갯수가 multitab의 수보다 작으면 비교 방식이 바뀜
                    for iii in range(len(reverseStuff)):
                        if reverseStuff[iii] == multitab[ii] :
                            pass
                        else :
                            multitab[ii] = stuff[i]
                            result += 1
                            break
    print(result)
    
solve()