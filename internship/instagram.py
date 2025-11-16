'''download instagram data using python
'''
import smtplib
import random
import math
#first we will write down code foretp generation
#all possile digits as inputs
digits="0123456789"
#this will be the output variable ->OTP
OTP=""#this will be updated
#we are trying to get 6digit   number randomlygenerated step by step
for i in range (6):
    #we will update the OTP variable
    OTP+=digits[math.floor((random.random())*10)]#len(digts)=10
    print(OTP)
