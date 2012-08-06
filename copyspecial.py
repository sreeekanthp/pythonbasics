#!/usr/bin/python

import sys
import re
import os
import shutil
import commands

def absolute_path(dirname):
  result = []
  paths = os.listdir(dirname)
  for filename in paths:
    match = re.search(r'__(\w+)__', filename)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, filename)))
  return result


def cpy(paths, dirctory):
  if not os.path.exists(directory):
    os.mkdir(directory)
  for path in paths:
    filename = os.path.basename(path)
    shutil.copy(path, os.path.join(directory, filename))

def zipto(paths, zfile):
  cmd = 'zip -j ' + zfile + ' ' + ' '.join(paths)
  print "Command I'm going to do:" + cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    cpy(paths, todir)
  elif tozip:
    zipto(paths, tozip)
  else:
    print '\n'.join(paths)

  
if __name__ == "__main__":
  main()
