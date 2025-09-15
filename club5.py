n=int(input('떡 개수: '))
m=int(input('떡 길이: '))
arr=list(map(int, input('').split()))

h=1  #우선 제일 작은 값부터 시작
while(True):
    newarr=[]  #떡 리스트들을 h만큼 잘랐을때의 길이들을 담자.
    for i in arr:
        if i>h:
            newarr.append(i-h)
        else:
            newarr.append(0)
    if m>=sum(newarr):  #기준 이하면 스탑
        break
    else:               #더 자를수 있으니 h값 1 증가
        h+=1

print(h)