n=int(input('회사의 수: '))   
m=int(input('도로의 수: '))

road=[]   #전체 길들을 담자
for _ in range(m):
    a,b=map(int, input().split())
    road.append([a,b])


x,k=map(int, input().split())

def shortcut(s): #s번째 건물에서 거리가 1인 곳들을 리스트로 반환하는 함수
    path=[]      #s번째 건물에서 거리가 1인 곳들의 리스트
    for a, b in road:
        if a==s:
            path.append(b)
        elif b==s:
            path.append(a)
    return path


arr=shortcut(1)   #1번 건물에서 거리가 1인 곳들의 리스트
shortcut1=1       #거리를 재기 위해 선언한 정수
while(True):
    if x in arr:  #리스트에 x번 건물이 있다면 stop
        break
    if shortcut1>=n:  #최대거리는 n개이다. 그 이상이면 사실상 못 간다.
        shortcut1=-1
        break
    newarr=[]     #리스트에 arr들의 shortcut()들을 담자
    for routes in arr:
        newarr.extend(shortcut(routes))
    arr=newarr    #덮어씌우자
    shortcut1+=1

arr=shortcut(x)  #x번 건물에서 거리가 1인 곳들의 리스트 (이하 동문)
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