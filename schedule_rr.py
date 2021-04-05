def getTurnaroundTimes(waitTimes, tasks):
   TATs = []
   for i in range(0, len(waitTimes)):
      TATs.append(waitTimes[i] + tasks[i][2])
   return TATs

def round_robin(tasks):
   waitTimes = []
   turnAroundTimes = []
   timeQuantum = 10
   timeElapsed = 0
   length = len(tasks)
   i = 0
   print("+--------------------------------------+\n| {:^36} |".format("Round-Robin"))
   print("+------------+------------+------------+")
   print("| {:^10} | {:^10} | {:^10} |".format("Name", "Priority", "Burst Time"))
   print("+------------+------------+------------+")
   while i < len(tasks):
      task = tasks[i]
      if task[2] <= timeQuantum:
         timeElapsed += task[2]
         pid = int(task[0][1:])
         try:
            waitTimes[pid - 1] = timeElapsed - tasks[pid - 1][2]
         except:
            waitTimes.append(timeElapsed - tasks[pid - 1][2])
      else:
         timeElapsed += timeQuantum
         if i < length:
            waitTimes.append(0)
         tasks.append((task[0], task[1], task[2] - timeQuantum))
      if i < length:
         print("| {:^10} | {:^10} | {:^10} |".format(task[0], task[1], task[2]))
      i += 1
   turnAroundTimes = getTurnaroundTimes(waitTimes, tasks[:length])
   print("+------------+------------+------------+\n| Average Waiting Time: {:<14} |".format(round(sum(waitTimes) / length, 2)))
   print("+------------+------------+------------+\n| Turnaround Time: {:<19} |".format(round(sum(turnAroundTimes) / length, 2)))
   print("+------------+------------+------------+\n")
   return
   