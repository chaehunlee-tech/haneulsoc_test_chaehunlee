n, m = map(int, input("N M = ").split()) #NM값 받기
graph = [] #

for _ in range(n):
    row = list(map(int, input().strip()))
    graph.append(row)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: #범위 밖일땐 false
        return False
    if graph[x][y] == 0: #0찾으면 주변 0 전부 1로 바꾼다 -> 같은 그룹 중복으로 세는걸 방지하기 위해
        graph[x][y] = 1 #탐색이 끝난 경로는 1로 바꾼다
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 아이스크림 개수 세기
result = 0
for i in range(n): 
    for j in range(m):
        if dfs(i, j): #True값을 받을때 마다 개수를 센다
            result += 1

print('아이스크림 개수: ',result)
