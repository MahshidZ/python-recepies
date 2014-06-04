'''
A Binary Search Tree class.
''' 

class BST(object):

  def __init__(self):
    self.root = None
  
  def insert(self, data):
    new_node = Node(data)
    if self.root == None:
      self.root = new_node
    else:
      near = self.closest_node(data)
      if(near.data > data):
        near.left_child = new_node
        new_node.parent = near
      elif near.data <= data:
        near.right_child = new_node
        new_node.parent = near

  def print_in_order(self, node):
    if node == None:
      return 
    self.print_in_order(node.left_child) 
    print node.data,
    self.print_in_order(node.right_child)
       
  def get_next(self, key):
    a_node = self.find(key)
    if a_node == -1:
      return -1 
    if a_node.right_child != None:
      walking_node = a_node.right_child
      while(walking_node.left_child != None):
        walking_node = walking_node.left_child
      return walking_node.data
    elif a_node.right_child == None:
      walking_node = a_node
      while (walking_node != None and walking_node.parent != None):
        if walking_node == walking_node.parent.left_child:
          return walking_node.parent.data
        else:
          walking_node = walking_node.parent
      if walking_node == None:
        return -1
      if walking_node.parent == None:
        return -1

  def find(self, data):
    walking_node = self.root
    if walking_node.data == None:
      return 0
    while walking_node != None:
      if walking_node.data == data:
        return walking_node
      elif walking_node.data > data:
        if walking_node.left_child != None:
          walking_node = walking_node.left_child
        elif walking_node.left_child == None:
          return 0
      elif walking_node.data < data:
        if walking_node.right_child != None:
          walking_node = walking_node.right_child
        elif walking_node.right_child == None:
          return 0

  def closest_node(self, data): 
    '''
    Returns either the largest smaller nodes before, or the smallest larger
    nodes after. If the data equals a node, returns that node.
    '''
    walking_node = self.root
    while(walking_node != None):
      if walking_node.data == data:
        return walking_node
      elif walking_node.data > data:
        if walking_node.left_child != None:
          walking_node = walking_node.left_child
        elif walking_node.left_child == None:
          return walking_node
      elif walking_node.data < data:
        if walking_node.right_child != None:
          walking_node = walking_node.right_child
        elif walking_node.right_child == None:
          return walking_node 
 
  def find_smallest_node(self):
    if self.root == None:
      return
    walking_node = self.root
    smallest_node = self.root
    while walking_node != None:
      if walking_node.data <= smallest_node.data:
        smallest_node = walking_node
      if walking_node.left_child != None:
        walking_node = walking_node.left_child
      elif walking_node.left_child == None:
        walking_node = None
    return smallest_node

  def find_k_smallest(self, k):
    k_smallest_node = self.find_smallest_node()
    if k_smallest_node == None:
      return 
    else:
      k_smallest_data = k_smallest_node.data
    count = 1 # already found the first one
    while count < k:
      k_smallest_data = self.get_next(k_smallest_data)
      count += 1
    return k_smallest_data

class Node(object):

  def __init__(self, data):
    self.data = data
    self.right_child = None
    self.left_child = None
    self.parent = None

  def set_right_child(self, rightnode):
    self.right_child = rightnode

  def set_left_child(self, leftnode):
    self.left_child = leftnode

