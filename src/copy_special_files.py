'''
https://developers.google.com/edu/python/exercises/copy-special

Write a program to find filenames with pattern __something__ 
in an input directiry and copy them into another directory
if to_dir does not exits, create it

Usage: python copy_special_files from_dir to_dir
'''

import re   #regular expression
import os   # listdir, path.abspath
import sys  # argv
import shutil  # copy from to

def copy_special_files(from_dir, to_dir):
  for f in os.listdir(from_dir):
    match = re.search('[a-z]*_{2}[a-z]*_{2}',f)
    if match:
      file_path = os.path.join(from_dir, f)
      file_path = os.path.abspath(file_path)
      shutil.copy(file_path, to_dir)


def main():
 args = sys.argv[1:]
 if len(args) == 0:
   print "Must specify two input arguments"
   sys.exit(1)

 from_dir = args[0]
 to_dir = args[1]

 if not os.path.exists(to_dir):
   os.mkdir(to_dir)

 copy_special_files(from_dir, to_dir) 


if __name__ == "__main__":
  main()












