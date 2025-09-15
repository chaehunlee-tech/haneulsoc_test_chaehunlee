n=int(input('피보나치수:'))
fibo=[0,1]
for i in range(n+1):
    print(fibo[0], end=' ')
    fibo[0],fibo[1]=fibo[1],fibo[0]+fibo[1]



