n=int(input('N개: '))
k=int(input('K번: '))

arra = list(map(int, input().split()))
arrb = list(map(int, input().split()))

arra.sort()              
arrb.sort(reverse=True)  

for i in range(k):
    if arra[i]<arrb[i]:
        arra[i],arrb[i]=arrb[i],arra[i]

print(sum(arra))