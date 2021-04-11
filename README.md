## CA216 CPU Scheduling

All algroithms are run by the program.
The program is run with driver.py. The commandline argument is a test file.
To run: python driver.py FILENAME.txt

Name: Ben Guiden
Student Number: 19310046

I am aware of and acknowledge the DCU integrity policy and I confirm that all work presented is my own.

Link to Youtube video presentation: https://youtu.be/oXzwOZLFPpI

This is the repo for the C starter files.  Read the details below carefully.  Note: the details of the different algorithms required for both the solo and pairs versions of the project are [found in the project spec](https://ca216.computing.dcu.ie/assessments/scheduling-assignment/) Only implement the files for the project-type you are undertaking.

Completing this project will require writing the following C files

schedule_fcfs.c
schedule_sjf.c
schedule_rr.c
schedule_priority.c
schedule_priority_rr.c

The supporting files invoke the appropriate scheduling algorithm. 

For example, to build the FCFS scheduler, enter
```
make fcfs
```
which builds the fcfs executable file.
