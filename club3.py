n, m = map(int, input("N M = ").split())
graph = [list(map(int, input().strip())) for _ in range(n)]

def bfs(x, y):
    arr = []
    graph[x][y] = 0 
    if x > 0 and graph[x-1][y] == 1:
        arr.append((x-1, y))
    if x < n-1 and graph[x+1][y] == 1:
        arr.append((x+1, y))
    if y < m-1 and graph[x][y+1] == 1:
        arr.append((x, y+1))
    if y > 0 and graph[x][y-1] == 1:
        arr.append((x, y-1))
    return arr

arr1 = bfs(0, 0)
steps = 1

while True:
    if (n-1, m-1) in arr1:
        break
    new_arr = []
    for x, y in arr1:
        new_arr.extend(bfs(x, y))
    arr1 = new_arr
    steps += 1

print(steps)