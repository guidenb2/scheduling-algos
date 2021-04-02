def run(tasks, algo):
   waitTimes = []
   print("+--------------------------------------+\n| {:^36} |".format(algo))
   print("+------------+------------+------------+")
   print("| {:^10} | {:^10} | {:^10} |".format("Name", "Priority", "Burst Time"))
   print("+------------+------------+------------+")
   print("| {:^10} | {:^10} | {:^10} |".format(tasks[0][0], tasks[0][1], tasks[0][2]))
   waitTimes.append(0)
   for i in range(1, len(tasks)):
      task = tasks[i]
      waitTimes.append(waitTimes[i - 1] + tasks[i - 1][2])
      print("| {:^10} | {:^10} | {:^10} |".format(task[0], task[1], task[2]))
   print("+------------+------------+------------+\n| Average Waiting Time: {:<14} |".format(sum(waitTimes) / len(tasks)))
   print("+------------+------------+------------+\n")
   return