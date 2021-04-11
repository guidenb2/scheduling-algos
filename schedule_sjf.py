# Name: Ben Guiden
# Student Number: 19310046
#
# I am aware of and acknowledge the DCU integrity policy and I confirm that all work presented is my own.
#

from runner import run

def burst_time(task):
   return task[2] # returns the last item of a tuple

def sjf(tasks):
   nl = sorted(tasks, key=burst_time)  # sort the tasks list on the last item of the tuple
   run(nl, "Shortest Job First") # call the run function
   return
   