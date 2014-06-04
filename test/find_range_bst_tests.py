from nose.tools import *
from basic_bst import *
from find_range_bst import *

def test_range_count():
  my_bst = BST()
  my_bst.insert(3)
  my_bst.insert(5)  
  my_bst.insert(4)
  my_bst.insert(2) 
  range_finder1 = RangeFinderInOrderStrategy(my_bst, 2, 4)
  count = range_finder1.count_range()
  assert_equal(count, 3)
  range_finder2 = RangeFinderCompareStrategy(my_bst, 2, 4)
  count = range_finder2.count_range()
  assert_equal(count, 3)
  range_finder3 = RangeFinderGetNextStrategy(my_bst, 2, 4)
  count = range_finder3.count_range()
  assert_equal(count, 3)

def test_print_range():
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
  range_finder1 = RangeFinderInOrderStrategy(my_bst, 13, 23)
  range_finder1.print_range()
  range_finder2 = RangeFinderCompareStrategy(my_bst, 13, 23)
  range_finder2.print_range()
  range_finder3 = RangeFinderGetNextStrategy(my_bst, 13, 23)
  range_finder3.print_range()

