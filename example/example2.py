from ezsub import EZSUB
import numpy as np

ezsub = EZSUB(
    projectName="biophys",
    jobName="SNE",
    wallTime=(2,0,0),
    jobNameExtra=[("p","%i"),("n","%i")]
	,test=True
    #email = 'agrday@bu.edu'
    )

ezsub.submit(
    command = '~/.conda/envs/py35/bin/python main.py',
    #fixedParameters = [('T',5.5),('E',2.0)],
    variableParameters = [('p',[20,40]),('n',[1000,1200])]
)
