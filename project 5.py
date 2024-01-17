graph1={'A':set(['B','C']),
        'B':set(['A','D','E']),
        'C':set(['A','F']),
        'D':set(['B']),
        'E':set(['B','F']),
        'F':set(['C','E'])}
visited = []
queue = []
def bfs(visited,graph,node):
 visited.append(node)
 queue.append(node)
 while queue:
  m=queue.pop(0)
  print(m,end = " ")
  for neighbour in graph[m]:
   if neighbour not in visited:
      visited.append(neighbour)
      queue.append(neighbour)
print("Following is the Breadth First")
bfs(visited,graph1,'A')