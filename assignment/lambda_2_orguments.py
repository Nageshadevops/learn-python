"""2) Try Lambda function take more than 2 arguments and try out
eg- a+b+c, a+b-c"""

#Trying lambda function more than two arguments
a=6
b=5
c=8
d=10
sum= a+b
print(sum)
#showing this lamda is a short term work/temprorary function thereis no relation bwt abcd above and below

x=  lambda a,b,c,d : a+b-c*3
print(x(5,6,2,9))


