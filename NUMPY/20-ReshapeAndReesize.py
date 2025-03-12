import numpy as np

a = np.arange(10)
print(a)

b = a.reshape((2,5)) #เปลี่ยนแปลงไม่ถาวร ต้องมีอะไรไปรับค่า
print(b)

a.resize((2,5)) #เปลี่ยนถาวร
print(a)