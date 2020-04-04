from numpy import array,zeros
from scipy.linalg import solve
a=array([[1,2,-1],[2,1,-2],[-3,1,1]],float)
b=array([3,3,-6],float)
t=solve(a,b)
print(t)
