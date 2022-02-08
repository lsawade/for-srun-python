# Running srun commands in parallel

This is a python version of https://github.com/luet/while-loop-srun

It does the same thing three different ways:


[1] `sbatch` script with `bash` loop to run `code.py`
    ```bash
    sbatch while.sh
    ```
[2] `sbatch` script that calls a `python` script that handles
    submission within a for loop
    ```bash
    sbatch parent.sh
    ```
[3] `sbatch` script entirely based on python.
    ```bash
    sbatch for.py
    ```
    
All three have their place and do the same thing, and handle srun the same
way but their exectution and setup differs.

Note that each submission file contains the statement:
```bash
#SBATCH --cpus-per-task=4
#SBATCH --ntasks-per-core=1
```
This is unique to Traverse and can be removed for the Intel clusters on the Princeton clusters.
SLURM seems to have issue with non-explicit submission of tasks with the 4 hardware thread setup
that the POWER9 CPU has. Removing `--ntasks-per-core=1` does work, but is slower in subsequent
submission. Removing `#SBATCH --cpus-per-task=4` does not work.