n=int(input('회사의 수: '))
m=int(input('도로의 수: '))

road=[]
for _ in range(m):
    a,b=map(int, input().split())
    road.append([a,b])


x,k=map(int, input().split())

def shortcut(s):
    path=[]
    for a, b in road:
        if a==s:
            path.append(b)
        elif b==s:
            path.append(a)
    return path


arr=shortcut(1)
shortcut1=1
while(True):
    if x in arr:
        break
    if shortcut1>=n:
        shortcut1=-1
        break
    newarr=[]
    for routes in arr:
        newarr.extend(shortcut(routes))
    arr=newarr
    shortcut1+=1

arr=shortcut(x)
shortcut2=1
while(True):
    if k in arr:
        break
    if shortcut2>=n:
        shortcut2=-1
        break
    newarr=[]
    for routes in arr:
        newarr.extend(shortcut(routes))
    arr=newarr
    shortcut2+=1

print(shortcut1,shortcut2)