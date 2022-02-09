#!/bin/env python

from subprocess import Popen, PIPE, STDOUT

# 'python' for testing and 'srun -n1' for submission
execmethod='srun -n1'

# Read parameter file
with open('parameters.dat', 'r') as f:
    paramstr = f.read().strip().split('\n')
    params = [x.split() for x in paramstr]

    # There is a new line at the end of the file.

# Create process list and output file list
outfile_list = []
process_list = []

for _p in params:

    # Creating the full command
    cmd = f"{execmethod} code.py {' '.join(_p)}"

    # Outputfile
    filename = f"{_p[0]}-{_p[1]}-{_p[2]}.out"
    f = open(filename, 'w')
    outfile_list.append(f)
    
    # Adding it to the process list. Note the .split() Popen doesn't want a single string.
    # Also the stderr is sent to PIPE because f/stdout is sent to file. PIPE could be
    # replaced by an error log.
    process_list.append(Popen(cmd.split(), stdout=f, stderr=None, cwd='./'))

# Wait for the processes to finish
for _proc, _f in zip(process_list, outfile_list):
    _proc.wait()
    _f.close()
    


