import sys
from collections import deque

def solve():
    # Use fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    n, m = int(input[0]), int(input[1])
    adj = [[] for _ in range(n + 1)]
    
    # Building the adjacency list
    idx = 2
    for _ in range(m):
        u, v = int(input[idx]), int(input[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # BFS structures
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    
    # BFS Loop
    found = False
    while queue:
        u = queue.popleft()
        
        if u == n:
            found = True
            break
            
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
                
    # Path Reconstruction
    if not found:
        print("IMPOSSIBLE")
    else:
        path = []
        curr = n
        while curr != 0:
            path.append(curr)
            curr = parent[curr]
        
        path.reverse()
        print(len(path))
        print(*(path))

if __name__ == '__main__':
    solve()