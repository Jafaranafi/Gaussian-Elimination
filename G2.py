from numpy import array,zeros
#Note that this code is for Newton method for two variable
a=array([[1,-2],[1,0]],float)
b=array([1/4,0],float)
n=len(b)
x=zeros(n,float)
#print (a,b)
#Elimination
for k in range(n-1):
	for i in range(k+1,n):
		if a[i,k]==0:continue
		factor=a[k,k]/a[i,k]
		print (factor)
		for j in range(k,n):
			print(factor)
			a[i,j]=a[k,j]-a[i,j]*factor
			#print (a)
		b[i]=b[k]-b[i]*factor
#print (a)
#print (b)
#Back-substitution
x[n-1]=b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
	sum_gauss=0
	for j in range(i+1,n):
		sum_gauss+=a[i,j]*x[j]
	x[i]=(b[i]-sum_gauss)/a[i,i]
print (x)   
