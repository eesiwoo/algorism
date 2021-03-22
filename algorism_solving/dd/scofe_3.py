n, m = map(int, input().split())

store_map = []
total_dress = []


for _ in range(m):
    store_map.append(list(map(int, input().split())))

for z in range(m) :
    zzz = []
    for i in range(n) :
        total = 0
        for ii in range(z,m) :
            total += store_map[ii][i]
        if i < n :
            for iii in range(i+1,n) :
                total += store_map[m-1][iii]
        zzz.append(total)
    total_dress.append(zzz)    
    
print(total_dress)