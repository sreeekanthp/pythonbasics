#!/usr/bin/python -tt

import random
import sys

def mimic_dict(filename):
  f = open(filename, 'r')
  t = f.read()
  f.close()
  words = t.split()
  first = ''
  mimic = {}
  for word in words:
    if not first in mimic:
      mimic[first] = [word]
    else:
      mimic[first].append(word)
    first = word
  return mimic

def print_mimic(mimic, word):
  for i in range(200):
    print word,
    j = mimic.get(word)
    if not j:
      j = mimic['']
    word = random.choice(j)

def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
