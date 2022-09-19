#Lambda functions 

#normal function but the problem is that its only a single line expression which will more than likely not be used again 
#so whats the point of making it a defined function.
def cube(a):
    return a*a*a


result = cube(6)

print(result)

#a single use un-named function/ anonymous function is better to use. It is also know as a lamda function
#lambda
f = lambda a,b : a+b 

result = f(4,6)

print(result)




def myfunc(n):

   return lambda a : a + n

c = myfunc(5)

print(c(7))



