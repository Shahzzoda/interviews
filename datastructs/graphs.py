# Graphs are great for representing pairwise relationships between many objects.
# A social network is a classic example of graphs! Graphs can be directed or 
# undirected. though rees are graphs, not all graphs are trees  interviews, 
# you are often given this in a list of pairs that represent connections
# between nodes, also known as edges. There are two main ways of
# representing graphs, adjacency list and an adjacency matrix.
from collections import defaultdict
from collections import deque

# default dictionary is nice bc if the keys are not found, it will not complain
# like the built in map, but instead just create the key-value pair. as you see
# below, the default dictionary must know what the value types will be, i believe 
# this is for memory allocation purposes. our will be a list. 
def adjListRep(edges):
  alist = defaultdict(list)
  for v1, v2 in edges:
    alist[v1].append(v2)
    alist[v2].append(v1)
  print("adj list:", alist)
  return alist 

# There are some basic traversals we also have to know for virtually every 
# graph problem we will be given. There are two main traversals for graphs: 
# BFS and DFS. There are a LOT of similarities, and only a few differences. 

# Note: BFS and DFS are incredibly powerful and are given very very often in 
# interviews! you can run these on matrixes/grids, trees, and ofc graphs. 
# Both of these runtimes are O(n), because at worst case it visits all nodes 
# but never one node twice, bc, as you'll see, we maintain a set for this reason. 


# Breadth First Traversals: you vist one node, visit all its 
# neighbors, and then visit the neighbor's neighbors. We do this until we 
# have visited all the nodes in the trees. 
# When BFS -> Think Queue
def bfs(edges, s):
  adjList = adjListRep(edges)
  visit = deque()
  visit.append(s)
  visited = set()
  while len(visit) > 0:
    currNode = visit.popleft()
    print(currNode)
    visited.add(currNode)
    neighbors = adjList[currNode]
    for neighbor in neighbors:
      if neighbor not in visited:
        visit.append(neighbor)

# Depth First Search  will start at one node and go as deep as it can. So it'll 
# visit one node, then one of its neighbor, then another one of its neighbor
# and do that until it gets to a node that has no more unvisited neigbors. 
# When it has no more unvisited neighbors, it will backtrack to the previously
# visited node that has neighbors and go deep down until it hits another with 
# no more neighbors and redo all of that. 
# When DFS -> Think Stack.
def dfs(edges, s):
  adjList = adjListRep(edges)
  visit = deque()
  visit.append(s)
  visited = set()
  while len(visit) > 0:
    currNode = visit.pop()
    print(currNode)
    visited.add(currNode)
    neighbors = adjList[currNode]
    for neighbor in neighbors:
      if neighbor not in visited:
        visit.append(neighbor)


# Edges of an undirected graph.
edges = [(1, 2), (1, 5), (2, 5), (2, 4), (2, 3), (3, 8)]
dfs(edges, 3)