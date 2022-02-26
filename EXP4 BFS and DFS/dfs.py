from time import time

graph = {
    'Homepage': ['AboutAuthor', 'RecipesIndex'],
    'AboutAuthor': ['Summary', 'Contact'],
    'Summary': [],
    'Contact': [],
    'RecipesIndex': ['Veg'],
    'Veg': ['BreakfastIndex', 'LunchIndex', 'DinnerIndex'],
    'BreakfastIndex': ['Idli', 'Dosa'],
    'LunchIndex': ['RiceVariety', 'sambar', 'Curd'],
    'DinnerIndex': ['Chappathi', 'Naan', 'Phulka', 'AlooMutterMasala'],
    'Idli': [],
    'Dosa': [],
    'RiceVariety': [],
    'sambar': [],
    'Curd': [],
    'Chappathi': [],
    'Naan': [],
    'Phulka': [],
    'AlooMutterMasala': []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
t0 = time()
dfs(visited, graph, 'Homepage')
t1 = time() - t0
print('Time for DFS :', t1, 'seconds')
