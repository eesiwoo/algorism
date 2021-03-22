n = int(input())

arrival_HH = []
arrival_MM = []
departure_HH = []
departure_MM = []

for i in range(n) :
    time = input()
    arrival = time.split('~')[0].strip()
    arrival_HH.append(arrival.split(':')[0])
    arrival_MM.append(arrival.split(':')[1])
    
    departure = time.split('~')[1].strip()
    departure_HH.append(departure.split(':')[0])
    departure_MM.append(departure.split(':')[1])

max_H = arrival_HH.index(max(arrival_HH))
min_H = departure_HH.index(min(departure_HH))


if arrival_HH[max_H] > departure_HH[min_H] :
    print('-1')
    
elif  arrival_HH[max_H] == departure_HH[min_H] :
    ck_MM = [i for i, value in enumerate(arrival_HH) if value == max(arrival_HH)]
    for ii in ck_MM : 
        if arrival_MM[ii] >= departure_MM[min_H] :
            print('-1')

else :
    ck_MM = [i for i, value in enumerate(arrival_HH) if value == max(arrival_HH)]
    ck_MM2 = [i for i, value in enumerate(departure_HH) if value == min(departure_HH)]
    arrival_maxMM = arrival_MM[ck_MM[0]]
    departure_minMM = departure_MM[ck_MM2[0]]
    for ii in ck_MM :
        if arrival_maxMM < arrival_MM[ii] :
            arrival_maxMM = arrival_MM[ii]
    for iii in ck_MM2 :
        if departure_minMM < departure_MM[iii] :
            departure_minMM = departure_MM[iii]
      
    print('{}:{} ~ {}:{}'.format(arrival_HH[max_H],arrival_maxMM, departure_HH[min_H],departure_minMM))
