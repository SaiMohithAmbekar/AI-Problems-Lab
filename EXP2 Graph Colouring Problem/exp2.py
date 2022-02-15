def addEdge(adj, u, v):
 
    adj[u].append(v)
    adj[v].append(u)
 
# Function to check whether a graph is
# bipartite or not
def isBipartite(adj, v, visited, color):
 
    for u in adj[v]:
  
        if (visited[u] == False):
  
            visited[u] = True
  
            color[u] = not color[v]
  
    
            if (not isBipartite(adj, u, visited, color)):
                return False
                 
        elif (color[u] == color[v]):
            return False
     
    return True
 
# Driver Code
if __name__=='__main__':
 
    # No of nodes
    N = 6
  
    adj = [[] for i in range(N + 1)]
  
    visited = [0 for i in range(N + 1)]
    color = [0 for i in range(N + 1)]
  
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 4, 5)
    addEdge(adj, 5, 6)
    addEdge(adj, 6, 1)
  
    visited[1] = True
    color[1] = 0

    if (isBipartite(adj, 1, visited, color)):
        print("Graph is Bipartite")
    else:
        print("Graph is not Bipartite")