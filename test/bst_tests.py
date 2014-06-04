from nose.tools import *
from bst import *

def test_insert():
  my_bst = BST()
  my_bst.insert(3)
  my_bst.insert(5)  
  my_bst.insert(4)
  my_bst.insert(2) 
  my_bst.print_in_order(my_bst.root)

def test_find():
  my_bst = BST()
  my_bst.insert(3)
  my_bst.insert(5)  
  my_bst.insert(4)
  my_bst.insert(2) 
  my_node = Node(-1)
  my_node = my_bst.find(5)
  assert_equal(my_node.data,5)
  assert_equal(my_node.left_child.data, 4)

def test_range_count():
  my_bst_range_count = BST()
  my_bst_range_count.insert(3)
  my_bst_range_count.insert(5)  
  my_bst_range_count.insert(4)
  my_bst_range_count.insert(2) 
  count = my_bst_range_count.count_range(2, 4)
  assert_equal(count, 3)

def test_print_range():
  my_range_bst = BST()
  my_range_bst.insert(20)
  my_range_bst.insert(14)  
  my_range_bst.insert(18)
  my_range_bst.insert(15)
  my_range_bst.insert(19) 
  my_range_bst.insert(17) 
  my_range_bst.insert(16) 
  my_range_bst.insert(23) 
  my_range_bst.insert(26) 
  my_range_bst.insert(22) 
  my_range_bst.insert(21) 
  my_range_bst.insert(30) 
  my_range_bst.insert(24) 
  my_range_bst.insert(25)
  my_range_bst.print_range(13, 23)

def test_get_next():
  my_bst = BST()
  my_bst.insert(20)
  my_bst.insert(14)  
  my_bst.insert(18)
  my_bst.insert(15)
  my_bst.insert(19) 
  my_bst.insert(17) 
  my_bst.insert(16) 
  my_bst.insert(23) 
  my_bst.insert(26) 
  my_bst.insert(22) 
  my_bst.insert(21) 
  my_bst.insert(30) 
  my_bst.insert(24) 
  my_bst.insert(25) 
  assert_equal(my_bst.get_next(15), 16)
  assert_equal(my_bst.get_next(16), 17)
  assert_equal(my_bst.get_next(19), 20)




