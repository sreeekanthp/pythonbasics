#!/usr/bin/python

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  fp = open(filename,'rU')
  text = fp.read()
  namelist = []
  year_find = re.search(r'Popularity\sin\s(\d\d\d\d)',text)
  if not year_found:
     print 'Could not find the year\n'
  year = year_find.group(1)
  namelist.append(year)
  
  name_order = {}
  rank_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  for rank_name in rank_names:
    (rank,bname,gname) = rank_name
    if bname not in name_order:
      name_order[bname] = rank
    if gname not in name_order:
      name_order[gname] = rank
    
  sorted_name_order = sorted(rank_order.keys())
  for name in sorted_name_order:
    namelist.append(name + " " + name_order[name])
  return namelist

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
    namelist = extract_names(filename)
    text = '\n'.join(names)
    if summary:
      f = open(filename + '.summary', 'w')
      f.write(text + '\n')
      f.close()
    else:
      print text

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
