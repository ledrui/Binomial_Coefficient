# Iliass Tiendrebeogo       Oct. 2014
# Study of three different 
# implementation of the binomial coefficient
#----------------------------------------------------------------------

from math import factorial  # importing factorial from math modules
from time import clock
from memory_profiler import profile
import time

#definition of binomial coefficient generator

# Naive method of computing binomial coefficient (uses factorial)
#@profile
def naive_binom(n,k):
	#checking base cases
	if k < 0 or k > n: 
		return 0
	if k==1 or k == n:
		return 1
        #Output: returning the binomial coefficient of (n,k)
	return factorial(n)//(factorial(k)*factorial(n-k)) ## // stand for integer division

# The multiplicative method which is a more efficient method
#@profile
def mult_binom(n,k):
        #Checking for base cases
	if k < 0 or k > n: 
		return 0
	if k==1 or k == n:
		return 1
	k = min(k, n-k) # take advantage of symmetry
	result = 1
	for i in xrange(k):
		result = result*(n-i)/(i+1) #
	return result #Output: returning the binomial coefficient of (n,k)

# Pascal's triangle method: 
#@profile
def pascal_binom(n,k):

#Checking special cases
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    if k == 0 or n <= 1:
    	return 1
    triangle = [[1], [1, 1]] # Initialization of the array triangle
    if n == 1:
        return triangle[0]
    else:
        for i in xrange(2, n+1):
            triangle.append([1]*i)
            for j in xrange(1,i):
                #Compute the binomial coefficient and store it in the array
                triangle[i][j] = (triangle[i-1][j-1]+triangle[i-1][j]) 
                
            triangle[i].append(1)
        return triangle[n][k] #Output: returning the binomial coefficient of (n,k)


# Recursive version of Pascal's triangle ( high time complexity )

def pascal_binom_recursive(n,k):
        #we use only one array
	b=[0]*(n+1) # initialization of the array b with 0
	b[0]=1
	#we use only one loop 
	for i in xrange(1, n+1):
		b[i]=1
		j=i-1
		while j>0:
			b[j]+=b[j-1]
			j-=1
	return b[k]
## running time testing function
# all tests will be done against the same input n=5000, k=200
def testime(f):
    k = 100 #
    t0 = clock() # Calling the clock() function to set the starting time
    for i in range(1,k): # here the step is 2
        f(1000,k) 
    t1 = clock() # Calling the clock() function to set the ending time
    final_t = t1-t0
    return final_t

print 'naive_binom running time' ,testime(naive_binom), 'Sec'
print 'mult_binom running time' ,testime(mult_binom), 'Sec'
print 'pascal_binom running time' ,testime(pascal_binom), 'Sec'
print 'pascal_binom_recursive running time' ,testime(pascal_binom_recursive), 'Sec'

# Accuracy testing
result1 = 1.0*naive_binom(1000,500)/mult_binom(1000,500)
result2 = 1.0*naive_binom(1000,500)/pascal_binom(1000,500)
result3 = 1.0*mult_binom(1000,500)/pascal_binom(1000,500)
print 'relative error naive_binom/mult_binom', result1
print 'relative error naive_binom/pascal_binom', result2
print 'relative error mult_binom/pascal_binom', result3