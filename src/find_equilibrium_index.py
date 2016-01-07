'''
https://codility.com/c/run/demoQAUFYG-QZR

Write a program to return one equilibrium index. If not found, return -1.

Equilibrium index is an index where sum of all the elements in its right is equal to
sum of all the elements in its left. Assume that in the begining, sum is zero. Also we can
have negative or positive integers in any range.

The solution time and space should be O(n)

'''

def find_equi_index(Arr):
    arr_sum = sum(Arr)
    sum_so_far = 0
    for i in range(0, len(Arr)):
        if (arr_sum - Arr[i])%2 == 0 and (arr_sum - Arr[i]) / 2  == sum_so_far:
            return i
        sum_so_far += Arr[i]
    return -1

def main():
  args = sys.argv[1:]
  if len(args) == 0:
    print "must specify an input array"
    sys.exit(1)
  arr = args[0]
  find_equi_index(arr) 


if __name__ == "__main__":
  main()


