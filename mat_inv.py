import numpy as np

a=np.array(([1,3,3],[1,4,3],[1,3,4]))
print(a)

a_inv=np.linalg.inv(a)
print(a_inv)

a_trps=a.transpose()
print(a_trps)

p1=np.linalg.inv(a_trps.dot(a)).dot(a_trps).dot(a)


print(p1)
