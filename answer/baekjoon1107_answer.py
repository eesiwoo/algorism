'''후기
처음에 풀려고 했던 방법은 이랬다.
1. 입력받은 채널의 값을 한자리씩 쪼갠다 ex) 3254 -> 3,2,5,4
2. 동작하는 버튼만 남겨둔다.
3. 쪼갠 채널의 값과 동작하는 버튼의 값을 비교한다. 일치하면 그 버튼 사용, 불일치하면 가장 근사치를 사용
4. 4가지 버튼( 위의 경우에서 )을 결정하면 하나의 문자열로 합친 뒤 입력받은 채널의 값에서 뺀다.
5. 처음 누른 횟수와 뺀 값(+,- 버튼으로 움직인 값)을 더해 리턴한다.

3번을 구현하면서 잘못한걸 깨달았다. 만약 입력받은 값이 8일 때 내가 누를 수 있는 버튼이 0과 2라면, 내가 짠 코드는 2를 누르라고 할 것이다.
하지만 실제로는 0을 누르고 버튼을 2번 조절하는게 빠르다.

이걸 해결하려면 10을 사용해야하는데 그 순간부터 코드가 복잡하고 난잡해져서... 구글의 도움을 받았다.
시간이 오래 걸려도 브루트포스를 사용하는 문제라는걸 알았고 완전 탐색에 대해 알게 되었다.
'''
channel = int(input())      # Target
num_broken = int(input())   # 고장난 버튼 수
lst_broken = []             # 고장난 버튼 리스트
 
if num_broken >0:           # 0 < 일 경우에만 입력
    lst_broken = input().split()
 
start = 100     
MIN = abs(channel-start)    
lst_channels = []           # 조건에 맞는 채널만 담을 리스트
 
for num in range(0,1000000+1):      # 리스트 생성
    check = True
    for char in lst_broken:
        if char in str(num):
            check = False
            break
    if check:               # 조건에 부합할 경우 추가
       lst_channels.append(num)
 
for ch in lst_channels:     # 리스트에서 MIN 값 찾기
    if abs(ch-channel) +len(str(ch)) < MIN :
        MIN = abs(ch-channel) +len(str(ch))
 
 
print(MIN)