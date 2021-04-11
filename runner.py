# Name: Ben Guiden
# Student Number: 19310046
#
# I am aware of and acknowledge the DCU integrity policy and I confirm that all work presented is my own.
#

def run(tasks, algo):
   waitTimes = []
   turnAroundTime = []
   print("+--------------------------------------+\n| {:^36} |".format(algo))
   print("+------------+------------+------------+")
   print("| {:^10} | {:^10} | {:^10} |".format("Name", "Priority", "Burst Time"))
   print("+------------+------------+------------+")
   for i in range(0, len(tasks)):
      task = tasks[i]
      if i == 0:
         waitTimes.append(0)
      else:
         waitTimes.append(turnAroundTime[i - 1])
      turnAroundTime.append(waitTimes[i] + task[2])
      print("| {:^10} | {:^10} | {:^10} |".format(task[0], task[1], task[2]))
   print("+------------+------------+------------+\n| Average Waiting Time: {:<14} |".format(round(sum(waitTimes) / len(tasks), 2)))
   print("+------------+------------+------------+\n| Turnaround Time: {:<19} |".format(round(sum(turnAroundTime) / len(tasks), 2)))
   print("+------------+------------+------------+\n")
   return