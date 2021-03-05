''' 문제
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 

수빈이가 지금 보고 있는 채널은 100번이다.
'''
def solve():
    n = input()
    m = int(input())
    brokenBtn = 0
    if m != 0 :
        brokenBtn = list(map(int, input().split()))
    
    if n == 100: # 요청받은 채널이 100이면 버튼을 누를 필요 없음
        return print(0)
    
    else : # 0이 아니라면 버튼을 조작함
        btnList = FindBtn(brokenBtn)
        targetList = SplitChannel(n)
        setChannel(btnList, targetList)

def SplitChannel(n) : # 입력 받은 채널을 한자리씩 나누기
    targetList = []
    for i in n:
        targetList.append(i)
    return targetList

def FindBtn(brokenBtn) : # 어떤 버튼이 멀쩡한지 찾기
    btnList = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(brokenBtn)) :
        if brokenBtn[i] in btnList  :
            btnList.remove(brokenBtn[i])
    return btnList

def setChannel(btnList, targetList) :
    count = 0
    btnSet = []
    for i in targetList :
        if i in btnList :
            btnSet.append(i)
        else :
            pass
            # 잘못풀었땅 ㅎ
