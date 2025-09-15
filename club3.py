n, m = map(int, input("N M = ").split()) #MN값 받기
graph = [list(map(int, input().strip())) for _ in range(n)]

def bfs(x, y): #해당 좌표에서 한칸 거리의 좌표들을 찾기 위한 함수
    arr = [] #반환 받을 배열을 선언
    graph[x][y] = 0 #자기가 간 길을 돌아가지 않기 위해 0처리
    if x > 0 and graph[x-1][y] == 1:
        arr.append((x-1, y))   #상하좌우 탐색해서 1인 곳을 찾으면 배열에 넣는다
    if x < n-1 and graph[x+1][y] == 1:
        arr.append((x+1, y))
    if y < m-1 and graph[x][y+1] == 1:
        arr.append((x, y+1))
    if y > 0 and graph[x][y-1] == 1:
        arr.append((x, y-1))
    return arr

arr1 = bfs(0, 0)  #arr1:n번 움직이는것이 최소인 모든 좌표들을 모아보자
steps = 1  #몇번 움직였는가를 

while True:
    if (n-1, m-1) in arr1:  #만약 해당 좌표가 도착점이라면 스탑
        break
    new_arr = []  #n+1번째 좌표들을 담기
    for x, y in arr1: #n번째 좌표들의 bfs들
        new_arr.extend(bfs(x, y))  
    arr1 = new_arr #덮어씌우기
    steps += 1 #n+1번째

print(steps)