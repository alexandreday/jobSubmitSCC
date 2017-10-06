.. first documentation master file, created by
   sphinx-quickstart on Fri Oct  6 15:19:16 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Example of use
=================

.. highlight:: python

**The header:** 
::
	from ezsub import EZSUB
	import numpy as np

**Submit a single job:**
::

    # define macro parameters
    so_easy = EZSUB( 
                    projectName="fheating",
                    jobName="MC"
                    )
    # submit job with parameters T=2.26 and J=1.0
    so_easy.submit(
                    command = '~/.conda/envs/py35/bin/python main.py', # main.py is the python script you want to submit
                    fixedParameters = [('T',2.26), ('J',1.0)]
                    )
                    
**Submit a multiple jobs:**
::
    # submit job with parameters T=[1.0,2.0,3.0,4.0] and J=1.0
    so_easy.submit(
                    command = '~/.conda/envs/py35/bin/python main.py', 
                    fixedParameters = [('J',1.0)],
                    variableParameters = [('T', np.arange(1.0,4.01,1.0))]
                    )

**Submit multiple jobs, and have clear job name identifiers:**
::
    # define macro parameters and job identifier syntax
    so_easy = EZSUB( 
                    projectName="fheating",
                    jobName="MC",
                    jobNameExtra=[("T","%.2f"),("J","%.1f")] 
                    # jobNameExtra specifies the format of the param. to track in the job name
                    )
     # submit job with parameters T=[1.0,2.0,3.0,4.0] and J=1.0
    so_easy.submit(
                    command = '~/.conda/envs/py35/bin/python main.py', 
                    fixedParameters = [('T',2.26), ('J',1.0)]
                    )


Documentation
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. automodule:: ezsub
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
