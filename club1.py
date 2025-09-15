pos = [0,0]
maxnum=int(input('N의 값을 입력하시오:'))
usr=input('R L U D 를 입력하시오: ').upper().split()

for i in range(len(usr)):
    if usr[i]=='R' and 0<=pos[1]<(maxnum-1):
        pos[1]+=1

    elif usr[i]=='L' and 0<pos[1]<=(maxnum-1):
        pos[1]-=1

    elif usr[i]=='U' and 0<pos[0]<=(maxnum-1):
        pos[0]-=1

    elif usr[i]=='D' and 0<=pos[0]<(maxnum-1):
        pos[0]+=1

pos[0]+=1
pos[1]+=1

print('최종 위치: ',pos)