# Description
Python package for easily sending jobs on the scc. Facilitates looping over parameters and avoids dealing directly with cumbersome bash syntax !

# Installing
I suggest you install the code using ```pip``` from an [Anaconda](https://conda.io/docs/user-guide/tasks/manage-environments.html) Python 3 environment. From that environment run the following commands:
```
git clone https://github.com/alexandreday/jobSubmitSCC.git
cd jobSubmitSCC/
pip install .
```
That's it ! You can import the ```ezsub.EZSUB()``` class and submit your jobs really easily. Check out the example file for more info on the format of the command or just try running it.

# Documentation
To generate the documentation go to ```doc/``` and use ```make html```. The produced html file will be in the ```_build``` directory.
