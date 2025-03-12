import numpy as np
a  = np.array([1,2,4,5,8])
print(np.append(a,40))
print(np.insert(a,1,100))

b = np.array([[1,2],[3,4]])
print(b)
print( np.insert(b,1,[10,20],axis=0))