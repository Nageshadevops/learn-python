"""Assiginment Questions
1) Try For loop with continue
2) Try For loop with continue along with else
3) What happens when an function is expecting 2 arguments and you provide 3 argument & 1 argument"""


# using continue in for loop
"""
for x in range(8):
    if x == 3:
        continue
    print(x)
"""

# for loop with contiue & else
"""
for y in range(8):
    if y==3:
        continue
    print(y)
else :
    print("finished")
    """

# print function with 3 elemets if its expextion only 2
"""
def my_job(fname,lname):
    print(fname,lname  )

my_job("Arjun", "soogurshettar" ,"30")
"""
"""
def my_job(fname,lname):
    print(fname,lname  )

my_job("Arjun")
"""
"""
a=[1,2,3,4]
b=[3,4,5,6]
union =[]
for i in range(len(a)):
    exist = false
    for j in range(len(b)):
    exist = true
        if not exist:
        union +=[a[i]]
for i in range """

#swap values of variables
"""
a=5,3
b=8,4
a,b=b,a
print("a",a)
print("b",b)
"""
#leap year
"""
leap year= 2023
if year % 4 == 0 and year % 100 != 0 :
    print(year,"is leap year")
else:
    print(year,"is not leap year")
"""
#vowels
"""
# Word to analyze""
word = "apple"
vowel_count=0
consonant_count=0

# Define vowels
vowels = ["a","e","i","o","u"]
for i in word:
    if i in vowels:
        print(f"{i} is vowel")
        vowel_count+=1
    else:
         print(f"{i} is consonentl")
         consonant_count+=1
print("vowel",vowel_count)
print("consonent",consonant_count)
"""
"""
Assiginment Questions
1) Try passing the different arguments to a function like tuple sets and dictonaries
2) Try Lambda function take more than 2 arguments and try out 
eg:-a+b+c,a+b-c
"""
# passing tuple as arguments in funtion
"""
def my_job(states):
    for i in states:
        print(i)
states = ("karnataka", "Andra", "tamilnadu")
my_job(states)
"""

# passing set as arguments in funtion
"""
def my_job(states):
    for i in states:
        print(i)
states = {"karnataka","Andra","Tamilnadu"}
my_job(states)"""

#Passing Dictionary as arguments in funtion
"""
def my_job(carmodel):
    for key,value in carmodel.items():
        print(key,value)
car_model = { "brand_name":"Tata", "model":"nexon","fuel":"diesel"}

my_job(car_model)"""

#Try Lambda function take more than 2 arguments and try out
"""
x= lambda a,b,c,d : a*b+c-d
print(x(4,5,6,8))   
"""

"""def my_function(y):
    return 5 * y
print(my_function(3))
print(my_function(5))
print(my_function(9))

x= lambda a,b,c,d : a*b+(c-d)
print(x(4,5,8,9))"""

"""def my_job(carmodel):
    for i,j in carmodel.items():
        print(i,j)
car_model = { "brand_name":"Tata", "model":"nexon","fuel":"diesel"}

my_job(car_model)"""

#degrees to farenhit
"""
degrees=input("enter the degrees")
print("degrees" +"!")
print(type(degrees))
#farenhit=((degrees)*(9/5)+32)
#print(farenhit)

"""
# convert farenhit to
"""
farenhit=input("enter the farenhit")
print("farenhit" +"!")
degree=(int(farenhit)*(5/9)-32)
print(degree)
"""

# palindrome

"""
value= input("enter the value")
print(value)
rever_value= value[::-1]
print(rever_value)

if value == rever_value:
    print("it is a palindrome")
else:
    print("it is not palindrome")
"""
"""
for x in range(10,0,-1):
    print(x)
"""
# even number
"""
x =[]
for x in range(50):
    if x % 2 ==0:
     print(x)
"""
"""
x=6
if x % 2 != 0:
    print("it is a prime number")
else:
    print("it is not a prime number")"""
"""
i = 1
while i < 6:
    pass
"""
"""
def my_job(*args):
    print(min(args))

my_job( 4,5,6,7)
"""

"""
x=[1,1,2,3,3,4,5]

print(set(x))
"""
"""
x=[1,5,3,8,6]

y=sorted(x,reverse=True)
print(y)
"""
"""
x= {"name":"arjun","age":"32","state":"karnataka"}
y= {"name": "prajwal","age":"32","state":"karnataka"}

value1=x.values()
value2=y.values()
for i in value1:
    for j in value2:
        if i == j:
            print(i)
"""
"""
x= 1,2,3,5
least=x[0]
for i in x:
    if (i<least):
        least =i
print(least)
"""
#if largest of 3 number
a=3
b=8
c=6

"""if a > b and a > c :
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else: print("c is largest")
"""
"""
x= [6,5,3,4,6]
y=x[0]
count=0
for i in x:
    if i == y:
        print(i)
        count+=1
print(count)

"""
#revering a string

"""x="apple"
revers_str= x[::-1]
print(revers_str)"""
"""
x = "aeroplane"
reversed_str = ""

for i in range(len(x) - 1, -1,-1):  # Start from the last index and move backward
    reversed_str += x[i]

print(reversed_str)
"""
x ="apple"
y = x[0]
z = str(0)
for i in y -1,-1,-1:
    print(i)