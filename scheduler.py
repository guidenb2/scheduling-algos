import sys
from schedule_fcfs import fcsf
from schedule_sjf import sjf
from schedule_priority import priority

def reader(file):
   tasks = []
   try:
      with open(file, "r") as fd:
         lines = fd.readlines()
      for line in lines:
         tokens = line.split(",")
         tasks.append((tokens[0].strip(), int(tokens[1].strip()), int(tokens[2].strip())))
   except:
      print("The file {} does not exist".format(file))
   return tasks

def main():
   file = sys.argv[1]
   tasks = reader(file)
   fcsf(tasks)
   sjf(tasks)
   priority(tasks)

if __name__ == "__main__":
   main()
