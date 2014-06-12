'''
https://developers.google.com/edu/python/exercises/copy-special

Write a program to print absolute path of filesnames 
'''


import re
import os
import sys
import shutil

def copy_special_files(from_dir, to_dir):
  for f in os.listdir(from_dir):
    match = re.search('[a-z]*_{2}[a-z]*_{2}',f)
    if match:
      file_path = os.path.join(from_dir, f)
      file_path = os.path.abspath(file_path)
      shutil.copy(file_path, to_dir)


def main():
 from_dir = sys.argv[1]
 to_dir = sys.argv[2]
 if not os.path.exists(to_dir):
   os.mkdir(to_dir)
 copy_special_files(from_dir, to_dir) 


if __name__ == "__main__":
  main()












