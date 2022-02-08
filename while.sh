#! /bin/bash
#SBATCH -t 0:5:0
#SBATCH --ntasks=5
#SBATCH --cpus-per-task=4
#SBATCH --ntasks-per-core=1

while read a b c

do
    srun -n 1 python code.py $a $b $c > $a-$b-$c.out &
done < parameters.dat
wait
