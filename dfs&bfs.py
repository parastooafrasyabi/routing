#parastoo afrasyabi
graph = {'Arad': set(['zerind', 'timisoara', 'sibiu']),
         'zerind': set(['Arad', 'oradea']),
         'timisoara': set(['Arad', 'lugoj']),
         'sibiu': set(['Arad', 'fagaras','rimnicu','oradea']),
         'oradea': set(['zerind', 'sibiu']),
         'lugoj': set(['timisoara', 'mehadia']),
         'mehadia': set(['lugoj', 'dobreta']),
         'dobreta': set(['mehadia', 'craiova']),
         'craiova': set(['dobreta', 'rimnicu']),
         'rimnicu': set(['craiova', 'sibiu']),
         'fagaras': set(['sibiu', 'bucharest']),
         'bucharest': set(['pitesti', 'fagaras','giu','urziceni']),
         'pitesti': set(['rimnicu', 'bucharest']),
         'giu': set(['bucharest']),
         'urziceni': set(['bucharest', 'hirsova','vaslui']),
         'vaslui': set(['urziceni', 'lasi']),
         'lasi': set(['vaslui', 'neamt']),
         'neamt': set(['lasi']),
         'hirsova': set(['efo', 'urziceni']),
         'efo': set(['hirsova'])}
		 
		 
		 
		 
		 
		 
		 def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'Arad')





def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

dfs(graph, 'sibiu') 









def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

list(dfs_paths(graph, 'Arad', 'bucharest'))







def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

list(dfs_paths(graph, 'sibiu', 'bucharest')) 







def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'Arad') 




def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_paths(graph, 'Arad', 'bucharest')) 





def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

shortest_path(graph, 'Arad', 'bucharest') 