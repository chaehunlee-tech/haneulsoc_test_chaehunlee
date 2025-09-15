n=int(input('떡 개수: '))
m=int(input('떡 길이: '))
arr=list(map(int, input('').split()))

h=1
while(True):
    newarr=[]
    for i in arr:
        if i>h:
            newarr.append(i-h)
        else:
            newarr.append(0)
    if m>=sum(newarr):
        break
    else:
        h+=1

print(h)