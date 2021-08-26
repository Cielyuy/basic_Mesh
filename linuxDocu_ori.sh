#!/bin/bash
#SBATCH -J test1
#SBATCH -p cpu
#SBATCH -N 1
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH -t 1-15:00:00




module load ansys/fluent

hostlist= echo `env |grep RMS_HOSTLIST|awk -F "=" '{print $2}'` | tr "," "\n" > hostlist



