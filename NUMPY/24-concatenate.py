import numpy as np

a = np.array([3,4,2,6])
b = np.array([8,6,5,10])

c = np.concatenate((a,b))
print(c)

k  = np.append(a,100)
print(k)

h = np.array([[1,2],[3,4]])
print(h)
print(np.append(h,[[10],[20]] ,axis =1))