import numpy as np 
a=np.array([[20,30],[30,40]])
b=np.array([[20,30],[30,40]])
print(np.hstack([a,b])) #horizontal concatenation 
print(np.vstack([a,b])) #vertical concatenation 