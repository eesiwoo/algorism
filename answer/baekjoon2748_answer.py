''' 후기
나는 처음 풀 때 정석을 몰랐고... 내 생각대로 풀었다.
나중에 찾아보면서 피보나치의 정석은 재귀함수를 이용하는 것이라고 알게 되었고, 그렇게 풀면 백준에서는 정답이 아니라는 것도 알게 되었다ㅋㅋㅋ
'''

def solve():
    random = int(input())
    if random == 0 :
        print(0)   
    elif random == 1 :
        print(1)
    else :
        Fibonacci(random)
        
        
def Fibonacci(random):
    count = 2
    a = 0
    b = 1
    c = a+b

    while count < random :      
        a = b
        b = c
        c = a+b
        count += 1
    else : 
        print(c)       
            
solve()
