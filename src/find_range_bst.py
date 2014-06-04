import basic_bst

class RangeFinder(object):
  ''' Interface/Abstract class '''
  def __init__(self, bst, a, b):
    self.bst = bst 
    self.a = a
    self.b = b
     
  def nodes_in_range(self):
    raise NotImplementedError('This is an abstract class.')

  def count_range(self):
    lst = []
    self.nodes_in_range(self.bst.root, lst)
    return len(lst)

  def print_range(self):
    lst = []
    self.nodes_in_range(self.bst.root, lst)   
    print(lst)

class RangeFinderInOrderStrategy(RangeFinder):
  '''uses in_order recursion and when it found a node
    in the range, it prints it! O(n)
  '''
  def __init__(self, bst, a, b):
    RangeFinder.__init__(self, bst, a, b)

  def nodes_in_range(self, node, lst):
    if node == None: 
      return
    self.nodes_in_range(node.left_child, lst)
    if node.data >= self.a and node.data <= self.b:
      lst.append(node.data)
    self.nodes_in_range(node.right_child, lst)

class RangeFinderCompareStrategy(RangeFinder):
  '''
  compares the value of the node to the range and
  does not go down to some subtrees as a result. O(k)
  '''
  def __init__(self, bst, a, b):
    RangeFinder.__init__(self, bst, a, b)

  def nodes_in_range(self, node, lst):
    if node == None:
      return
    if node.left_child != None:
      if self.a <= node.data:
        self.nodes_in_range(node.left_child, lst)
    if self.a <= node.data <= self.b:
      lst.append(node.data)
    if node.right_child != None:
      if node.data <= self.b:
        self.nodes_in_range(node.right_child, lst) 

class RangeFinderGetNextStrategy(RangeFinder):
  def __init__(self, bst, a, b):
    RangeFinder.__init__(self, bst, a, b)

  def nodes_in_range(self, node, lst):
    '''
    first finds a node <= a then call get next until reach to
    b. O(log(n) + k)
    '''
    if node == None:
      return
    found = self.bst.closest_node(self.a)
    found_data = -1
    if found.data < self.a and found != None:
      found_data = self.bst.get_next(found.data)
    elif self.a <= found.data <= self.b and found != None:
      found_data = found.data
    while self.a <= found_data <= self.b:
      lst.append(found_data)
      found_data = self.bst.get_next(found_data)  


