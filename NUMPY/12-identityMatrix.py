import numpy as np

a = np.identity(4)
print(a)

b = np.identity(5)
print(b)

c = np.identity(5,dtype="int")
print(c)

d = np.eye(5) #สำหรับต้องการที่ไม่ให้เป็นเมทริกจัตุรัส
print(d)

e = np.eye(3,4)
print(e)

f = np.eye(5,k=1) #ย้านขึ้น 1 
print(f)

g = np.eye(5,k=-1) #ย้ายลง 1 
print(g)