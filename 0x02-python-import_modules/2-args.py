#!/usr/bin/python#
if __name__ == "__main__":
 from sys import argv
 lenofArg = (len(argv)

 if lenArg == 1:
  print("0 arguments.")
 elif lenofArg == 2:
  print("{} arguments:".format(lenofArg - 1)
 else:
  print("{} argguments:".format(lenofArg - 1)
 for index, var in enumerate(argv):
  if index == 0:
 continue
  print("{}: {}".format(index, var))
