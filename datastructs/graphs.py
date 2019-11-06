# Given a list of pairs that represent edges in an undirected graph, create an adj list out of that. 
edges = [(1, 2), (1, 5), (2, 5), (2, 4), (2, 3), (3, 8)]

class Node:
  def __init__(self, val):
    self.val = val
    self.adj = []
  def __str__(self):
    return str(self.val) + " : " + str(self.adj)
  def __eq__(self, n2):
    return self.val == n2.val

def repGraph(edges):
  alist = []
  for n1, n2 in edges:
    temp = Node(n1)
    if alist.count(temp) == 1:
      i = alist.index(temp)
      alist[i].adj.append(n2)
    else:
      temp.adj.append(n2)
      alist.append(temp)
    temp = Node(n2)
    if alist.count(temp) == 1:
      i = alist.index(temp)
      alist[i].adj.append(n1)
    else:
      temp.adj.append(n1)
      alist.append(temp)
  return adjlist

def printlist(alist)
  for node in alist:
    print node



# how does one do a BFS?
# we need a start node, we need a visited set and we 
# need queue to keep track of what gets printed when

