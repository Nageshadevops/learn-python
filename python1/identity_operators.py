"""
#Using is
x = [1, 2, 3]
y = x
z= [1, 2, 3]
print(x is y)
#output: True
print(x is z)
#output: False
"""

"""
x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)
#output: true
"""

#Combining Identity Operators
a = 10
b = 10
c = [10]
print(a is b)
#output: true
print(a is not c)
#output: true