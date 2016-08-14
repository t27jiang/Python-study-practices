#!/usr/bin/python -tt

import sys

def main():
  if len(sys.argv) >= 2:
    print 'Hello '+ sys.argv[1]
  else:
    print 'Hello World'


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()