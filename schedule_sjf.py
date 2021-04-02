from runner import run

def burst_time(task):
   return task[2]

def sjf(tasks):
   nl = sorted(tasks, key=burst_time)
   run(nl, "Shortest Job First")
   return
   