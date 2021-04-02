from runner import run

def priority_number(task):
   return task[1]

def priority(tasks):
   nl = sorted(tasks, key=priority_number)
   run(nl, "Priority")
   return
   