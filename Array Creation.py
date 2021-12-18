"""import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ndim)
print(type(arr))
print(arr.size)
print(arr.dtype)
print(arr.shape)"""

#creating array from list with dtype
"""import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]], dtype = "float")
print(a)
a = np.array([[1, 2, 3], [4, 5, 6]], dtype = "int")
print(a)
a = np.array([[1, 2, 3], [4, 5, 6]], dtype = "complex")
print(a)"""

#creating array from tuple
"""import numpy as np
b = np.array((1, 3, 2))
print(b)"""

#creating 3by 4 array
"""import numpy as np
s = np.zeros((3, 4))
print(s)"""

#creating constant value array of complex type
import numpy as np
c = np.full((3, 3), 5, dtype = "complex")
print(c)