import numpy as np
import os, time, itertools

def template():
    return """
    #!/bin/bash -login\n
    #$ -P *projectName*\n 
    #$ -N *jobName*\n 
    #$ -l h_rt=*wallTime*\n
    #$ -m ae\n
    #$ -m n\n
    #$ -M *email*\n
    *command*
    """

class EZSUB:
    """Python 3 script for easily submitting jobs on the SCC !
    """

    def __init__(self, projectName, jobName, jobNameExtra= None, wallTime=(2,0,0), email = None, jobNumber = True):
        self.projectName = projectName
        self.jobName = jobName
        self.wallTime = "{:02d}:{:02d}:{:02d}".format(*wallTime)
        self.email = email    
        self.jobNameExtra = dict(jobNameExtra)
        self.jobNumber = jobNumber

    def submit(self, command, fixedParameters = None, variableParameters = None):
        """
        Parameters
        ------------
        fixedParameters: list of tuples = (string, float or int)
            specifies the fixed parameters passed to the command line.
            For instance, if parameter T takes values 2.26 and J takes values 1.0, this is specified as:
                [("T",2.26),("J",1.0)]
            This will be translated to:
                "T=2.26 J=1.0" on the commmand line.
        
        variableParameters: list of tuples = (string, iterable)
            specifies the variable parameters passed to the command line.
            For instance, if parameter T takes values [1.0, 2.0, 2.26, 3.0] and J takes values [1.0, 1.1, 1.2], this is specified as:
                [("T",[1.0, 2.0, 2.26, 3.0]),("J",np.arange(1.0, 1.21, 0.1))]
            This will trigger a loop over the parameters, giving the command line the following series of parameters:
                "T=1.0 J=1.0" 
                "T=1.0 J=1.1"
                "T=1.0 J=1.2"
                "T=2.0 J=1.0"
                ...

            Some notes: 
                - maximum precision on float parameters is 3 decimal places
                - format of specified parameters is always parameter=parameter_value, with parameter a string and parameter_value a numeric type
        """

        bashScript = template() # template format for scc qsub ...
        bashScript = bashScript.replace('*projectName*', self.projectName)
        bashScript = bashScript.replace('*wallTime*', self.wallTime)

        if self.email is not None:
            bashScript = bashScript.replace('*email*', self.email)
        else:
            bashScript = bashScript.replace("#$ -M *email*\n","")
            
        main_cmd = command
        jobNameList_dict = []
        
        if self.jobNameExtra is None:
            bashScript = bashScript.replace('*jobName*', self.jobName)
        else:
            jobName_str = ""
            if fixedParameters is not None:
                for fP in fixedParameters:
                    if fP[0] in self.jobNameExtra.keys():
                        jobName_str += (fP[0]+"="+self.jobNameExtra[fP[0]]%fP[1]+"_")

        cmdVar_list = []
        cmdVar_jobName_extra_list = []

        if variableParameters is not None:
            vParNames = [v[0] for v in variableParameters]
            vParIterables = [v[1] for v in variableParameters]
            n_varPar = len(vParNames)
    
            for values in list(itertools.product(*vParIterables)):
                tmp_name_to_value = dict(zip(vParNames, values))
                cmdVar_list.append(" ".join([vParNames[i]+"="+"%.3f"%vPV for i, vPV in enumerate(values)]))
                if self.jobNameExtra is not None:
                    for vPN in vParNames:
                        tmp = jobName_str
                        if vPN in self.jobNameExtra.keys():
                            tmp += (vPN+"="+self.jobNameExtra[vPN]%tmp_name_to_value[vPN]+"_")
                
                    cmdVar_jobName_extra_list.append(tmp[:-1])
        
        if fixedParameters is not None:
            cmdFix = " ".join([vFN+"="+"%.3f"%vFV for vFN, vFV in fixedParameters])
            main_cmd = main_cmd + " " + cmdFix
   
        ################ -> Submitting job here --> ###########

        if variableParameters is not None:
            for i, cmdVar in enumerate(cmdVar_list):

                full_cmd = main_cmd + " " + cmdVar
                f = open('submit_scc.sh', 'w')
                print(full_cmd)

                fullScript = bashScript
                tmp_jobName = self.jobName
                if self.jobNumber is True:
                    tmp_jobName += "%i"%i

                if self.jobNameExtra is not None:
                    fullScript = bashScript.replace('*jobName*', tmp_jobName + "_" + cmdVar_jobName_extra_list[i])
        
                fullScript = fullScript.replace("*command*", full_cmd)
                #print(fullScript)
                f.write(fullScript)
                os.system('qsub submit_scc.sh')
                os.system('rm submit_scc.sh')
                f.close()
                time.sleep(0.05)
        else:
            full_cmd = main_cmd
            f = open('submit_scc.sh', 'w')
            print(full_cmd)
            fullScript = bashScript
            tmp_jobName = self.jobName
            if self.jobNumber is True:
                tmp_jobName += "%i"%0

            if self.jobNameExtra is not None:
                fullScript = bashScript.replace('*jobName*', tmp_jobName)
        
            fullScript = fullScript.replace("*command*", full_cmd)
            #print(fullScript)
            
            f.write(fullScript)
            os.system('qsub submit_scc.sh')
            os.system('rm submit_scc.sh')
            f.close()
            time.sleep(0.05)


    #$ -pe omp 4 submission.sh \n
    #$ -l mem_per_core=4G# more memory \n
    #$ -M mbukov@bu.edu \n

#    source activate py27
#~/.conda/envs/py27/bin/python main_RL.py 2 1 2 1
#!/bin/bash -login
#$ -P fheating
#$ -N jobRL_1_2_1_4
#$ -l h_rt=12:00:00
#$ -m ae
#$ -m n
#$ -pe omp 4 submission.sh #request more processors
#$ -l mem_per_core=4G# more memory
#$ -M mbukov@bu.edu



    