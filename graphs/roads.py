import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

def solve():
    # Use fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    m = int(input[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input[idx])
        v = int(input[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    visited = [False] * (n + 1)
    representatives = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                
    # Traverse the graph to find all connected components
    for i in range(1, n + 1):
        if not visited[i]:
            # This node is the 'representative' of a new component
            representatives.append(i)
            dfs(i)
            
    # The number of new roads needed is (number of components - 1)
    print(len(representatives) - 1)
    
    # Print the roads connecting each component to the next
    for i in range(len(representatives) - 1):
        print(f"{representatives[i]} {representatives[i+1]}")

if __name__ == "__main__":
    solve()