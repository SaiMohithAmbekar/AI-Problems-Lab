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
visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end="\n")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
t0 = time()
bfs(visited, graph, 'Homepage')
t1 = time() - t0
print('Time for BFS :', t1, 'seconds')
