
    #!/bin/bash -login

    #$ -P fheating
 
    #$ -N QMC0_T=5.50_alpha=0.00000
 
    #$ -l h_rt=02:00:00

    #$ -m ae

    #$ -m n

    
    ~/.conda/envs/py35/bin/python main.py T=5.500 E=2.000 alpha=0.000
    