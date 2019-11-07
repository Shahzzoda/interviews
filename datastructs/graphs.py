from collections import defaultdict
from queue import Queue as queue
# Given a list of pairs that represent edges in an undirected graph, create an adj list out of that. 
edges = [(1, 2), (1, 5), (2, 5), (2, 4), (2, 3), (3, 8)]

def repGraph(eges):
  alist = defaultdict(list)
  for v1, v2 in edges:
    alist[v1].append(v2)
    alist[v2].append(v1)
  print alist

repGraph(edges)

# def bfs(edges):
#   q

