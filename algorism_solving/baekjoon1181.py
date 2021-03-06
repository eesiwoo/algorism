'''문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로


'''

def solve() :
    n = int(input())
    wordList = []
    for _ in range(n) :
        wordList.append(input())
    sort(wordList,n)
    
def sort(wordList,n) :
    answer = set(wordList)
    answer = list(answer)
    answer = sorted(sorted(answer), key=lambda x :[0])
    
    for _ in range(n) :
        for i in range(len(answer)-1) :
            if len(answer[i]) > len(answer[i+1]) :
                answer[i], answer[i+1] = answer[i+1], answer[i]
        
    
    return print(answer)

    
solve()