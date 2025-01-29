import numpy
import numpy as np
w=np.array([-1.5, 1, 1])
(w[0])
(np.float64(-1.5))
w[2]
np.float64(1.0)
x=np.array([[0,0],[0,1],[1,0],[1,1]])
print(f"array({x})")

x2 = np.hstack((np.ones((4,1)) , x))
print(f"array({x2})")

v = np.dot(w,x2[0])
v
np.float64(-1.5)
np.dot(w,x2[1])
np.float64(-0.5)
np.dot(w,x2[2])
np.float64(-0.5)
np.dot(w,x2[3])
np.float64(0.5)
np.dot(w,x2[0]) >=0
np.False_
np.dot(w,x2[0]) >=0
np.False_
np.dot(w,x2[0]) >=0
np.False_
np.dot(w,x2[0]) >=0
np.True_

print (np.dot(w,x2[3].T) >=0)
print (np.dot(w,x2.T) >=0)