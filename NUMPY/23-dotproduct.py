import numpy as np

a = np.array([[1,2] , [3,4]])
print(a)

b = np.array([[11,12] , [13,14]])
print(b)

c = a.dot(b) 

# [[1*11+2*3 , 1*12+2*14] ,[3*11+4*13, 3*12+4*14]]

print(c)