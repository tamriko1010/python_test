#библиотека NumPy
import numpy as np
#сумма всех элементов в массиве
a = np.random.random((2,3))
print(a)
print(a.sum())

#произведение элементов массивов
print('*' * 30)
a = np.array([[1,1], [0,1]])
b = np.array([[2,0],[3,4]])
print(a * b)