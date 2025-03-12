import numpy as np

x = np.array([[1,2,3] , [4,5,6] , [7,8,9]])

#x[start,end,step,col]

print(x[:,:])
print(x[1:,1:])
print(x[2:,2:])
print(x[2:,1:])
print(x[:,2:])
print(x[1:,:])
print(x[:2,:])
print(x[:2,2:])
print(x[1:2,1:2])
print(x[1:2,1:2])
print(x[::2,:])
print(x[1:2,:])
print(x[::,::2])
print(x[::,1:2])
