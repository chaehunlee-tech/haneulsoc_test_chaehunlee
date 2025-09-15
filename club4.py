n=int(input('N개: '))
k=int(input('K번: '))

arra = list(map(int, input().split()))
arrb = list(map(int, input().split()))

arra.sort()              #내림차순으로 정렬
arrb.sort(reverse=True)  #오름차순으로 정렬

for i in range(k):
    if arra[i]<arrb[i]:
        arra[i],arrb[i]=arrb[i],arra[i]

print(sum(arra))