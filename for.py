#!/bin/env python
#SBATCH -N 1
#SBATCH -n 5
#SBATCH -t 0:5:0
#SBATCH --cpus-per-task=4
#SBATCH --ntasks-per-core=1


from subprocess import Popen, PIPE

# 'python' for testing and 'srun -n1' for submission
execmethod='python'

# Read parameter file
with open('parameters.dat', 'r') as f:
    paramstr = f.read().split('\n')
    params = [x.split() for x in paramstr]


# Create process list
process_list = []
for _p in params:

    # Creating the full command
    cmd = f"{execmethod} code.py {' '.join(_p)}"

    # Adding it to the process list. Note the .split() Popen doesn't want a single string.
    process_list.append(Popen(cmd.split(), stdout=PIPE, stderr=PIPE, cwd='./'))

# Wait for the processes to finish
for proc in process_list:
    proc.wait()


