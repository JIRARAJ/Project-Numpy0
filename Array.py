"""import numpy as np
arr = np.array([[-1, 2, 0, 4],
                [5, -0.5, 7, 6],
                [2.6, 9, 0, 4],
                [8, 9, -7, 0]])
#slicing array
temp = arr[:2, ::2]
print(temp)
r = arr[3::1, 3:1]
print(r)"""

#Basic operations of array
"""import numpy as np
a = np.array([0, 1, 2, 3])
print(a+1)
print(a-2)
print(a*5)#multiply
print(a**2)#squaring each number
a*=2  #modify
print(a)
s = np.array([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [6, 7, 8, 9]])
print(s)
print(s.T)#transpose"""

"""import numpy as np
arr= np.array([[1, 2, 3, 4], [2, 3, 4, 5], [6, 7, 8, 9]])
print(arr.max())
print(arr.max(axis = 1))
print(arr.min())
print(arr.min(axis = 0))
print(arr.sum())
print(arr.sum(axis = 0))
print(arr.sum(axis = 1))
print(arr.cumsum())
print(arr.cumsum(axis = 0))
print(arr.cumsum(axis = 1))"""

#array matrix operation
"""import numpy as np
a = np.array([[1, 2], [4, 5]])
b = np.array([[7, 8], [9, 0]])
print(a+b)
print(a-b)
print(a.dot(b))#matrix multiplication
print((a*2) + (3*b))"""