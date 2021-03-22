n, m = map(int, input().split())

store_map = []
total_dress = []


for _ in range(m):
    store_map.append(list(map(int, input().split())))

for i in range(n) :
    total = 0
    if i > 0 :
        for j in range(i) :
            total += store_map[0][j]
    for ii in range(m) :
        total += store_map[ii][i]
    if i < n :
        for iii in range(i+1,n) :
            total += store_map[m-1][iii]
    total_dress.append(total)
    
    
print(total_dress)