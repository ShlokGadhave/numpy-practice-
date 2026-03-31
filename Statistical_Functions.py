import numpy as np 
import statistics as stats
baked_food=[100,200,200,300,400,500,600]
a=np.array(baked_food)

print(np.mean(baked_food))
print(np.median(baked_food)) #central value after sorting 
print(stats.mode(baked_food)) #number of time the value occurs 
print(np.std(baked_food))
print(np.var(baked_food))

