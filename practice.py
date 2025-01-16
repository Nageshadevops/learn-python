"""#which is the largest number
a = 3
b = 4
c = 5
if a > b and a > c :
    print("a is greater")
elif b > a and b > c:
    print ("b is greater")
else: print ("c is greater")"""


"""
a =265
b =555
if a > b:
    print ("a is greater")
else: print ("b is greater")
"""

"""
a = 1, 2, 3
b = 4
if b in a:
    print("b is in a")
else: print("b not in a")
"""

"""
a = 1, 2, 32
c = 5, 8, 9
b = c
if a is b:
    print ("a is b")
elif c is b:
    print("c is b")
else: print ("c is not a")
"""

"""
#leap year
year = input("enter the year")
year=int(year)
if year % 4 == 0 and year % 100 != 0:
    print("year is leap year")
else: print ("not a leap year")
"""

"""
#swap values
a = 1
b = 2
a,b = b,a #values are interchanging
print(a)
print(b)
"""

"""
#List find the least number
x = 5, 2, 3, 4, -1
y = x[0] #index
for i in x:
    if i < y:
        y = i
print(y)
"""

"""
i < y:
5 < 5
2 < 5
3 < 5
-1 < 5 
"""

"""
#remove the duplicate value from the list
x = ["apple", "banana", "orange", "apple"]
print(set(x))
"""

#To find the same value in different dict
"""
a = {"apple":1 , "banana":2}
b = {"apple":4 , "banana":2}
val1 = a.values() # extract the value in a
val2 = b.values() # extract the value in b
for i in val1:    #
    for z in val2:
        if i == z:
            print(i)
"""


#To find the same value in different dict
"""
a = {"apple":1 , "banana":2}
b = {"apple":4 , "banana":2}
val1 = a.values()
val2 = b.values()
for i,z in zip(val1, val2): # Use zip() to iterate through both value sets
        if i == z:
            print(i)
"""

"""# set of number how many times a word is repeated
x = ["van", "car", "bus", "car"]
y = []
count=0
for i in range(len(x)):
    if i == y:
        print(i)
        count+=1"""

"""
#repeated values in the list, it will display
x= [5,2,4,5,5]
y=x[0]
count=0
for i in x:
    if i == y:
        print(i)
        count+=1
print(count)
"""

#reverse a string
x = "fruits"
reverse_string= x[::-1]
print(reverse_string)






