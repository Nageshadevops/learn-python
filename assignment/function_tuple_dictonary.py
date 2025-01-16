"""Assiginment Questions
1) Try passing the different arguments to a function like tuple sets and dictonaries
"""


"""#passing tuple as argument in function
def my_func(fruits):
    for i in fruits:
        print(i)
fruits = ("banana", "orange", "apple")
my_func(fruits)"""


"""#passing set as argument in function
def my_func(fruits):
    for i in fruits:
       print(i)
fruits = {"banana","orange", "apple"}
my_func(fruits)"""

"""#passing dict as argument in function
def my_func(building):
    for key,values in building.items():
        print(key,values)
building = {"house_type":"villa", "house_floors":"2", "house_rooms":"three"}
my_func(building)"""



#passing dict as argument in function
def my_func(building):
    for key,values in building.items():
        print(key,values)
building = {"house_type":"villa", "house_floors":"2", "house_rooms":"three"}
my_func(building)