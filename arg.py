"""
def my_function(arg1, arg2):
    print(arg1, arg2)

# Call with 3 arguments
my_function(1, 2, 3)
#TypeError: my_function() takes 2 positional arguments but 3 were given
"""
def my_function(arg1, arg2):
    print(arg1, arg2)

# Call with 1 argument
my_function(1)
#TypeError: my_function() missing 1 required positional argument: 'arg2'