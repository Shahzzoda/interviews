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
  # represent the graph as an adj list
  adjList = repGraph(edges)
  # add the starting point into the queue
  visit = deque()
  visit.append(s)
  # keep track of all the visited node
  visited = set()
  while len(visit) > 0:
    # get the node leftmost, print it, and add it to the visited set
    currNode = visit.popleft()
    print(currNode)
    visited.add(currNode)
    # find all the neighbors of the current node
    neighbors = adjList[currNode]
    # for each neighbor, we want to add it to queue if not visited before
    for neighbor in neighbors:
      if neighbor not in visited:
        visit.append(neighbor)



bfs(edges, 2)