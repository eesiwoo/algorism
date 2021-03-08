'''후기
이 문제는 답을 보고 분석을 했다.
일요일에 하루 쉬면서 다양한 문제를 보기만 했는데 어떻게 풀어야할지 감이 잘 안왔다.
우선 다이나믹 프로그래밍 문제를 접하면서 감을 익혀야겠다고 생각했다.
그 첫번째 문제로 고른게  RGB거리 문제였다.

색깔별로 각각의 계산 루트를 만들어 그 중 가장 작은 값을 리턴하는 문제다.
문제에서 같은 집의 색깔이 연속되면 안된다고 했으므로 이전 값을 가져올 땐 나의 색깔은 가져오지 않는다.
각각의 루트를 하나의 배열처럼 만들어서 처음 입력받은 값과 따로 관리한다.
입력받은 값을 모두 계산하고 마지막 값에서 가장 작은 값을 리턴하면 최소 비용을 구할 수 있다.

처음에 풀이 보고 잉 이게 뭐지?? 하다가 하나씩 천천히 뜯어보면서 공부했다.
일단 나도 머릿속으로 생각하고 펜으로 대충 코딩해본 다음에 풀이를 보는데 내가 생각한 조건이 안나와서 당황했다.
전에 풀었던 1181번 문자 배열처럼 색깔마다 번호를 주나? 했는데 아니었다.
이미 배열에 index로 주어진 번호가 있으니까 ! 굳이 색깔별로 번호를 줄 필요가 없는거지...
한 번 구조를 이해한 다음 부터는 이해가 잘 되었다.
'''
N = int(input())
cost_per_home = []

for _ in range(N):
    cost_per_home.append(list(map(int, input().split())))
    
    dp = [cost_per_home[0]]

for i in range(1, N):
    cost_per_color = []

    temp_red = min(dp[i - 1][1], dp[i - 1][2])
    cost_per_color.append(temp_red + cost_per_home[i][0])

    temp_green = min(dp[i - 1][0], dp[i - 1][2])
    cost_per_color.append(temp_green + cost_per_home[i][1])

    temp_blue = min(dp[i - 1][0], dp[i - 1][1])
    cost_per_color.append(temp_blue + cost_per_home[i][2])
    
    dp.append(cost_per_color)
    
print(min(dp[N - 1]))