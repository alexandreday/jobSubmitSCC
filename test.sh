#!bin/bash

for L in 1 10
do

for i in 2  # 1: cont actions; 2: bang-bang
do

        for j in $(seq 1 1 10) # of random realisations
		do
                for k in 2 4 8 #$(seq 2 2 10) # of total ramp times
                do

                echo "#!/bin/bash -login" >> submission.sh
        echo "#$ -P fheating" >> submission.sh #evolve is name of job
        echo "#$ -N jobRL_${L}_${i}_${j}_${k}" >> submission.sh #evolve is name of job
        echo "#$ -l h_rt=12:00:00">> submission.sh #336
        #echo "#$ -pe omp 4">> submission.sh #request more processors
        echo "#$ -m ae" >> submission.sh #a (abort) e(exit)
        #echo "#$-l mem_per_core=4G" >> submission.sh # more memory
        #echo "#$ -M mbukov@bu.edu" >> submission.sh
        echo "#$ -m n" >> submission.sh # disable emails
        echo "source activate py27" >> submission.sh # requires conda env called 'ED' with quspin
        echo "~/.conda/envs/py27/bin/python main_RL.py $i $j $k $L" >> submission.sh

		ksdjfksdjfksdjfk
        #sleep 1.0 #wait for half a second

            done

        done


done
done
~          
