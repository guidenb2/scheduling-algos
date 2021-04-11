# Name: Ben Guiden
# Student Number: 19310046
#
# I am aware of and acknowledge the DCU integrity policy and I confirm that all work presented is my own.
#

from runner import run

def priority_number(task):
   return task[1]

def priority(tasks):
   nl = sorted(tasks, key=priority_number)
   run(nl, "Priority")
   return
   