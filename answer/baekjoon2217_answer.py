'''후기
알고리즘 푸는건 재밌는데 값 입력을 어떻게 받아야 하는지 몰라서 아직 시작할 때 헤맨다...
이번 문제를 풀 때 문제는 이해했는데 값을 어떻게 받으라는거지...? 하는 생각때문에 값 입력 부분만 찾아보고 했다.
첫번쨰 for문 까지만 ! 뒷부분은 내가 생각하면서 풀었는데 한 번에 맞아서 좋았다.
2748번은 세 번이나 틀렸었는데...ㅎ
꾸준하게 열심히 풀어봐야겠다.
'''

def solve():
    n = int(input())
    rope(n)
    
    
def rope(n):
    arr = []
    answer = []
    for count in range(n):
        arr.append(int(input()))
        
    arr.sort(reverse = True)
    
    for i in range(n):
        answer.append(arr[i] * (i+1))
        
    answer.sort(reverse = True)
    print(answer[0])

solve()