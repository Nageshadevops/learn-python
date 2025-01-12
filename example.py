# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4 # x is of type integer
x = "Sally" # x is now of type string
print(x)


#You can get the data type of a variable with the type () function.
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John" #is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

#Many Values to Multiple Variables**
x, y, z = "Orange", "Banana", "cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)



