'''문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
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