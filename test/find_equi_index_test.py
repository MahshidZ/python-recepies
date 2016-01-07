from nose.tools import *
from find_equilibrium_index import *

def test_simple_arr():
    arr = [1, 2, 1]
    assert_equal(find_equi_index(arr), 1)

def test_empty_arr():
    arr = []
    assert_equal(find_equi_index(arr), -1)