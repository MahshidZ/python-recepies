'''
https://developers.google.com/edu/python/exercises/copy-special

Write a program to print absolute path of filesnames 
with pattern __something__
'''

import re  # regular expression
import os  # listdir path path.abspath
import sys # argsv exit(1) stderr.write

def find_special_files(dir):
  for f in os.listdir(dir):
    match = re.search('[a-z]*_{2}[a-z]*_{2}',f)
    if match:
      file_path = os.path.join(dir, f)
      print os.path.abspath(file_path)

def main():
  args = sys.argv[1:]
  if len(args) == 0:
    print "must specify an input directory"
    sys.exit(1)
  dir = args[0]
  find_special_files(dir) 


if __name__ == "__main__":
  main()












