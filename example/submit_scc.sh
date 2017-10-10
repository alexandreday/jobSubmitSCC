#!/bin/bash -login
#$ -P biophys
#$ -N SNE_p40_n1200
#$ -l h_rt=02:00:00
#$ -m ae
#$ -m n
~/.conda/envs/py35/bin/python main.py p=40.000 n=1200.000
