import numpy as np

class EZSUB:
    """Python 3 script for easily submitting jobs on the SCC !
    """

    def __init__(self, projectName, jobName, jobNameExtra= None, wallTime=(2,0,0), email = None):
        self.projectName = projectName
        self.jobName = jobName
        self.wallTime = "{:02d}:{:02d}:{:02d}".format(wallTime)
        self.email = email    
        self.jobNameExtra = jobNameExtra

    def submit(self, command, fixedParameters, variableParameters):
        bashScript = template()
        bashScript = bashScript.replace('*projectName*', self.projectName)
        
        if self.jobNameExtra is None:
            bashScript = bashScript.replace('*jobName*', self.jobName)
        else:
            print("kjsfdk")
        
        f = open('submit_scc.sh','w')
        f.write(
        

def template():
    tmp = """
    #!/bin/bash -login\n
    #$ -P *projectName*\n 
    #$ -N *jobName*\n 
    #$ -l h_rt=*wallTime*\n
    #$ -m ae\n
    #$ -m n\n
    """
    #$ -pe omp 4 submission.sh \n
    #$ -l mem_per_core=4G# more memory \n
    #$ -M mbukov@bu.edu \n

    source activate py27
~/.conda/envs/py27/bin/python main_RL.py 2 1 2 1
#!/bin/bash -login
#$ -P fheating
#$ -N jobRL_1_2_1_4
#$ -l h_rt=12:00:00
#$ -m ae
#$ -m n
#$ -pe omp 4 submission.sh #request more processors
#$ -l mem_per_core=4G# more memory
#$ -M mbukov@bu.edu



    