# graph - identify number of components

grid = [
['#', '#', '#', '#', '#', '#', '#', '#'],
['#', '.', '.', '#', '.', '.', '.', '#'],
['#', '.', '.', '#', '.', '#', '.', '#'],
['#', '#', '#', '.', '#', '#', '#', '#'],
['#', '.', '.', '.', '.', '.', '.', '#']
]
#up,down,left,right
directions = [[-1,0],[1,0],[0,-1],[0,1]]

m,n =len(grid),len(grid[0])
visited = [[False]*n for i in range (m)]  #2d visited matrix for grid

def dfs(x:int,y:int)->None:
    visited[x][y]=True
    for i in directions:
        next_x= x+i[0]
        next_y=y+i[1]
        if 0<=next_x<m and 0<=next_y<n and grid[next_x][next_y]=="." and not visited[next_x][next_y]:
            dfs(next_x,next_y)

def NumberofRooms(grid: list[list[str]])->int:
    rooms=0
    for i in range (m):
        for j in range(n):
            if grid[i][j] == "." and visited[i][j] ==False:
                dfs(i,j)
                rooms+=1 
    return rooms 
print(NumberofRooms(grid))   