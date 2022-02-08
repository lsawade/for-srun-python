#!/bin/bash
#SBATCH -N 1
#SBATCH -n 5
#SBATCH -t 0:5:0
#SBATCH --cpus-per-task=4
#SBATCH --ntasks-per-core=1

python childfor.py

