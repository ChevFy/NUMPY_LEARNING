import numpy as np

a  =  np.arange(1,11)
print(a)
print(a[2])
print(a[:])
print(a[7:]) #นับตั้งแต่ตัวสุดท้ายถึง 7
print(a[:5]) #นับตั้งแต่ตัวแรกถึงตัวที่ 5
print(a[2:5]) #นับตั้งแต่ตัวที่ 3 ถึง 5
print(a[2:9:2]) # เพิ่ม : มีการกระโดดเสต็ป 2 (กำหนดเขต)
print(a[::2]) # เพิ่ม : มีการกระโดดเสต็ป 2
