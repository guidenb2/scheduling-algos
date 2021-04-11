# Name: Ben Guiden
# Student Number: 19310046
#
# I am aware of and acknowledge the DCU integrity policy and I confirm that all work presented is my own.
#
# As round-robin doesn't run the same as the others, it has its own file for running

# Gets the turnaround time
# Parameters: list of wait times, list of tasks
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
   # Go through the list of tasks
   while i < len(tasks):
      task = tasks[i]   # Hold the current tasks item in the variable task
      if task[2] <= timeQuantum:
         # If the burst time is less than the time quantum, we can finish the task
         timeElapsed += task[2]  # Add the burst time to time elapsed
         pid = int(task[0][1:])  # Holds task name number (leaves out the 'T' or 'P', e.g. T1 would just be saved as 1)
         try:
            # Checks if we have already done a round-robin on this task
            waitTimes[pid - 1] = timeElapsed - tasks[pid - 1][2]  # Edit the wait time of the task
         except:
            # If we have seen this task already
            waitTimes.append(timeElapsed - tasks[pid - 1][2])
      else:
         # If the burst time is greater than the time quantum
         timeElapsed += timeQuantum # We only run up to the time quantum
         if i < length:
            # If we haven't run this task yet
            waitTimes.append(0)
         tasks.append((task[0], task[1], task[2] - timeQuantum))  # Add the task to the list with the burst time modified by subtracting the time quantum for it
      if i < length:
         # Print the task
         print("| {:^10} | {:^10} | {:^10} |".format(task[0], task[1], task[2]))
      i += 1
   turnAroundTimes = getTurnaroundTimes(waitTimes, tasks[:length])   # Call getTurnaroundTimes
   print("+------------+------------+------------+\n| Average Waiting Time: {:<14} |".format(round(sum(waitTimes) / length, 2)))
   print("+------------+------------+------------+\n| Turnaround Time: {:<19} |".format(round(sum(turnAroundTimes) / length, 2)))
   print("+------------+------------+------------+\n")
   return
   