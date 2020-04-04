from numpy import array,zeros
from scipy.linalg import solve
a=array([[1,1,1],[1,7,3],[4,10,-1]],float)
b=array([3,11,13],float)
t=solve(a,b)
print(t)
