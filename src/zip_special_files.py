'''
https://developers.google.com/edu/python/exercises/copy-special

Write a program to find files with names is a pattern __something__
Then zip all of them into files.zip 

Is an error occurs while zipping, print the error and exit the program

'''

import re       # regular expression
import os       # listdir, path.abspath
import sys      # argv
import commands # run a shell process

def zip_special_files(from_dir):
  desired_files=[]
  for f in os.listdir(from_dir):
    match = re.search('[a-z]*_{2}[a-z]*_{2}',f)
    if match:
      file_path = os.path.join(from_dir, f)
      file_path = os.path.abspath(file_path)
      desired_files.append(file_path)
   
  cmd = 'zip -j files.zip ' + (' ').join(desired_files) 
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)
  

def main():
 args = sys.argv[1:]
 if len(args) == 0:
   print "must specify an input directory"
   sys.exit(1)
 from_dir = args[0]
 zip_special_files(from_dir) 

if __name__ == "__main__":
  main()


