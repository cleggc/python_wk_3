import numpy as np

##arr = np.array([1,2,3,5,6])
##
##print(arr)

##new_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
##
##print(new_matrix)
##print(np.__version__)
##print(type(new_matrix))
##
##
##
##
##arr = np.array(42)
##
##print(arr)

#-----------------------------------------------------------------------

##a = np.array(42)
##b = np.array([1, 2, 3, 4, 5])
##c = np.array([[1, 2, 3], [4, 5, 6]])
##d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

##print(a.ndim)
##print(b.ndim)
##print(c.ndim)
##print(d.ndim)

##print(a)
##print(b)
##print(c)
##print(d)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)