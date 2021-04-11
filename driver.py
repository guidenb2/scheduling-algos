# Name: Ben Guiden
# Student Number: 19310046
#
# I am aware of and acknowledge the DCU integrity policy and I confirm that all work presented is my own.
#

import sys
from schedule_fcfs import fcsf
from schedule_sjf import sjf
from schedule_priority import priority
from schedule_rr import round_robin

def reader(file):
   tasks = []
   try:
      with open(file, "r") as fd:
         lines = fd.readlines()
      for line in lines:
         tokens = line.split(",")
         tasks.append((tokens[0].strip(), int(tokens[1].strip()), int(tokens[2].strip())))
   except:
      sys.exit("The file {} does not exist".format(file))
   return tasks

def main():
   file = sys.argv[1]
   tasks = reader(file)
   fcsf(tasks)
   sjf(tasks)
   priority(tasks)
   round_robin(tasks)

if __name__ == "__main__":
   main()
