# Name: Ben Guiden
# Student Number: 19310046
#
# I am aware of and acknowledge the DCU integrity policy and I confirm that all work presented is my own.
#
# This is the file used to gather input
#

import sys
# Import algorithms
from schedule_fcfs import fcsf
from schedule_sjf import sjf
from schedule_priority import priority
from schedule_rr import round_robin

# Used to add file input into a list
# Parameter: a file name
def reader(file):
   tasks = []
   # Check if file exits
   try:
      # If the file exists
      with open(file, "r") as fd:
         lines = fd.readlines()  # store file contents in lines
      # Iterate through lines => each line is contained in the string 'line'
      for line in lines:
         tokens = line.split(",")   # Split the line string on commas and hold the list in tokens
         tasks.append((tokens[0].strip(), int(tokens[1].strip()), int(tokens[2].strip())))   # Add each item in tokens to the list tasks. The items in tasks are tuples. Each tuple holds the task name, priority and CPU burst time
   except:
      # If the file doesn't exist
      sys.exit("The file {} does not exist".format(file))   # Display message and exit
   # returns the list of tasks
   return tasks

def main():
   file = sys.argv[1]   # File name will be on command line 
   tasks = reader(file) # Stores the return of the reader function in tasks
   fcsf(tasks) # call first come first serve
   sjf(tasks)  # call shortest job first
   priority(tasks)   # call priority
   round_robin(tasks)   # call round-robin scheduling

if __name__ == "__main__":
   main()
