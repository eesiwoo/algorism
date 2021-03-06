'''후기
문제를 보고 처음 생각했던 풀이 방법은 중복을 제거하고 정렬을 2번 하는 것이었다.

1. 값을 입력 받은 후 abc 순서로 정렬하기
2. 정렬된 값의 글자 수를 비교해 재정렬하기

내가 생각한 방법대로 풀어서 제출했더니 시간초과가 나왔다.
아마도 2번을 입력받은 단어의 수만큼 재정렬해서 그런 것 같다. 최대 2만개까지 가능했으니...
일렬로 쭉 단어를 새워두고 자리를 바꿀 때 다음 번호랑 이전 번호를 함께 비교할 수 있었으면 시간초과가 안나왔을 것 같은데..!
생각보다 어려웠다.

다른 사람들이 푼 방법을 찾아 봤는데 list를 만들 때 글자수를 함께 주고 한 번에 정렬하는 방법을 많이 썼다.
보자마자 아...! 하고 깨달았다. 이렇게 쉬운 길을 두고 한참 돌아갔다니...ㅋㅋㅋㅋ

조금 아쉬웠다!

'''

def solve() :
    n = int(input())
    wordList = []
    for _ in range(n) :
        wordList.append(input())
    sort(wordList)
    
def sort(wordList) :
    wordList = set(wordList)
    wordList = list(wordList)
    answer = []
    
    for word in wordList :
        answer.append((len(word), word))
    
    answer.sort(key = lambda word: (word[0], word[1]))
    
    for word in answer :
        print(word[1])

    
solve()