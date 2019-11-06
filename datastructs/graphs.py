# Given a list of pairs that represent edges in an undirected graph, create an adj list out of that. 
class Node:
  def __init__(self, val):
    self.val = val
    self.adj = []
    
  def __str__(self):
    return str(self.val) + " : " + str(self.adj)

  def __eq__(self, p2):
    return p2.val == self.val

def repGraph(edges)
  alist = []
  for n1, n2 in edges:
    temp = Node(n1)
    if alist.count(temp) == 1:
      i = alist.index(temp)
      alist[i].adj.append(n2)
    else:
      alist.append(temp)
      i = alist.index(temp)
      alist[i].adj.append(n2)
    temp = Node(n2)
    if alist.count(temp) == 1:
      i = alist.index(temp)
      alist[i].adj.append(n1)
    else:
      alist.append(temp)
      i = alist.index(temp)
      alist[i].adj.append(n1)
  return alist

# Test the function
edges = [(1, 2), (1, 5), (2, 5), (2, 4), (2, 3), (3, 8)]
alist = repGraph(edges)
for node in alist:
  print node
  
