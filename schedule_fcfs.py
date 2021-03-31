def fcsf(tasks):
   waitTimes = []
   i = 0
   print("Name Priority Burst Time")
   print("{}\t{}\t{}".format(tasks[0][0], tasks[0][1], tasks[0][2]))
   waitTimes.append(0)
   for i in range(1, len(tasks)):
      task = tasks[i]
      waitTimes.append(waitTimes[i - 1] + tasks[i - 1][2])
      print("{}\t{}\t{}".format(task[0], task[1], task[2]))
   print("Average waiting time: {}".format(sum(waitTimes) / len(tasks)))