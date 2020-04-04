from numpy import array,zeros
from scipy.linalg import solve
a=array([[1,-2],[1,0]],float)
b=array([1/4,0],float)
t=solve(a,b)
print(t)
