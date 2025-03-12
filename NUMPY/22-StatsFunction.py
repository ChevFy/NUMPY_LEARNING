import numpy as np

a = np.array([10,5,4,6,99,100,50,30])

print(a.sum())
print(a.prod())
print(a.mean())
print(a.max())
print(a.min())
print(a.argmax()) #แสดงตำแหน่ง
print(a.argmin()) #แสดงตำแหน่ง

b = np.array([[10,20,30] , [40,50,90] , [80,100,5]])
print(b)

print(np.min(b,axis=1))
print(np.min(b,axis=0))

print(np.max(b,axis=1))
print(np.max(b,axis=0))