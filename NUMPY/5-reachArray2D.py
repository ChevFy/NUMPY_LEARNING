import numpy as np

a = np.array([[1,2],[3,4],[5,6]])

# array( [[1,2] ,
#         [3,4] ,
#         [5,6]])
#


print(a[1][1])
print(a[0][1])
print(a[2][0])

a[2][1] = 500

print(a)

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(b[-1][-2])