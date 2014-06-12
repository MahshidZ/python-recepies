'''
https://developers.google.com/edu/python/exercises/copy-special

Write a program to print absolute path of filesnames 
'''


import re
import os
import sys

def find_special_files(dir):
  for f in os.listdir(dir):
    match = re.search('[a-z]*_{2}[a-z]*_{2}',f)
    if match:
      file_path = os.path.join(dir, f)
      print os.path.abspath(file_path)


def main():
  dir = sys.argv[1]
  find_special_files(dir) 


if __name__ == "__main__":
  main()












