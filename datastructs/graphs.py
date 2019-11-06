# Given a list of pairs that represent edges in an undirected graph, create an adj list out of that. 
edges = [(1, 2), (1, 5), (2, 5), (2, 4), (2, 3), (3, 8)]

# given a list of edges, make an adj list
class Node:
  # we want to initialize 
  def __init__(self, val):
    self.val = val
    self.adj = []
  # we want to be able to print it
  def __str__(self):
    return str(self.val) + " : " + str(self.adj)
  # we want to be able to find a match with count
  def __eq__(self, n2):
    return self.val == n2.val


alist = []

def repGraph(edges):
  for n1, n2 in edges:
    # print "in for"
    # for x in alist:
    #   print x
    temp = Node(n1)
    if alist.count(temp) == 1:
      i = alist.index(temp)
      alist[i].adj.append(n2)
      # print(n1, "found")
    else:
      temp.adj.append(n2)
      alist.append(temp)
      # print(n1, "not found")
    temp = Node(n2)
    if alist.count(temp) == 1:
      i = alist.index(temp)
      alist[i].adj.append(n1)
      # print(n2, "found")
    else:
      temp.adj.append(n1)
      alist.append(temp)
      # print(n2, "not found")


repGraph(edges)
for node in alist:
  print node