from collections import defaultdict
from collections import deque
# Given a list of pairs that represent edges in an undirected graph, create an adj list out of that. 
edges = [(1, 2), (1, 5), (2, 5), (2, 4), (2, 3), (3, 8)]

def repGraph(eges):
  alist = defaultdict(list)
  for v1, v2 in edges:
    alist[v1].append(v2)
    alist[v2].append(v1)
  print(alist)
  return alist

# to do a bfs, we visit nodes closest to current nodes for every node that has not been visited
# we'll need a set of visited nodes
# we'll need a queue of keep track of the order 
# {
#  n: [n, n, n],
#  n: [n, n],
#  n: [n, n, n, n],
# }
def bfs(edges, s):
  adjList = repGraph(edges)
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



bfs(edges, 2)