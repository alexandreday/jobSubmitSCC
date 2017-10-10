from ezsub import EZSUB
import numpy as np

ezsub = EZSUB( 
    projectName="fheating",
    jobName="QMC", 
    jobNameExtra=[("T","%.2f"),("alpha","%.5f")],
    test=True
    #email = 'agrday@bu.edu'
    #,test=True
)

ezsub.submit(
    command = '~/.conda/envs/py35/bin/python main.py', 
    fixedParameters = [('T',5.5),('E',2.0)], 
    variableParameters = [('alpha',np.arange(0,0.21,0.1))]
)