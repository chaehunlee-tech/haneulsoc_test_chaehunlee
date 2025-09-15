n, m = map(int, input("N M = ").split())
graph = []

for _ in range(n):
    row = list(map(int, input().strip()))
    graph.append(row)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: #범위 밖일땐 false
        return False
    if graph[x][y] == 0: #0찾으면 주변 0 전부 1로 바꾼다.
        graph[x][y] = 1 
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
        if dfs(i, j):
            result += 1

print('아이스크림 개수: ',result)
