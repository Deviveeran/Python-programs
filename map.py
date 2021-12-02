#reduce()
'''
from functools import *
l=[5,10,35,45,89]
output=reduce(lambda no1,no2:no1+no2,l)
print(output)
'''
'''
from functools import *
output=reduce(lambda no1,no2:no1+no2,range(0,100,5))
print(output)
'''

#function aliasing
'''
def aaa(name):
	print(name)
bbb=aaa
bbb('durga')
aaa('lakshmi')
'''
#map
#applying some functionality in an element present in a sequence
#map(function, iterable)
'''
l=[2,3,4,5,6,7]
m=map(lambda no:no**2,l)
print(list(m))
'''
#inner and outer functions
'''
def outer():
	print("outer")
	def inner():
		print("inner")
	#inner()
	return inner
#outer()
func=outer()
print(func)
'''

#map,reduce,filter
#Filter Here we don't want to use for loop
'''
l=[1,0,2,3,4,5,6]
l2=list(filter(lambda l: l%2==0, l))
print(l2)
'''
#reduce 
# reduce always take two arguments
#if you want to use reduce method fir we should import the functools modules
#sequence of element into single element through specific functions
'''
from functools import * # * or reduce
l=[1,2,3,4,5,6,7]
l2=reduce(lambda a,b:a+b,l)
print(l2)
'''

#map
#Applying some functionality to an element present in a sequence
#it's applying some operations or conditions.
'''
l=[0,1,2,3,4,5,6,7]
l2=list(map(lambda l:l*2,l))
print(l2)
'''
'''
l=list(filter(lambda var:var%2==0,range(0,10)))
print(l)
'''
'''
l=list(map(lambda var:var%2==0,range(0,10)))
print(l)
'''
'''
l=list(filter(lambda var:var*2,range(0,10)))
print(l)
l=list(map(lambda var:var*2,range(0,10)))
print(l)
'''


'''
----REDUCE------
1.reduce is one of the functools method
2.it wil take function and iterable(That function should always have two arguments)
3.It will return a single element from sequence of element using specfic methods.


---- MAP----------
1.It will take one function and iterable(That function have only one argument)
2.It will perform some oerations or conditions in a presented sequence(It will also return boolean values)

-----FILTER-------
1. It's follows some conditions. instead of conditions it's using some operations means it doesn't perform that operations.And it doesn't take boolean values while performing some operations.It will display the assigned values.
2.It have functions and iterable.
3.It will take specific values . 


'''
'''

l=[0,2,4,6,7,3]
l2=list(map(lambda l:l%2==0 ,l))
print(l2)
'''


'''
def add(l):
		return l+2
l=[0,2,4,6,7,3]
l2=list(filter(add,l))
print(l2)
'''








