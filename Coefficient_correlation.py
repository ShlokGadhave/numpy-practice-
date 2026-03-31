#-1 is inversly propotional relation 
#1 propotional relation 
#0 is no relation 
import numpy as np 

tobbaco_consumption=[100,300,400,600,900]
death_occur=[20,30,40,50,60]
print(np.corrcoef([tobbaco_consumption,death_occur]))