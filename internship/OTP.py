'''download instagram data using python
'''
'''import smtplib
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
    #print(OTP)
#now we will swnd above otp as a message to user
    msg ="Your Transaction code is "+OTP+","
    server=smtplib.SMTP('smtp.gmail.com',587)
    #now we start the connection
    server.login("seelakrishna7@gmail.com","fsfs fdsdf dfs fsdf sdf")
    #we will send mail
    sender="seelakrishna7@gmail.com"
    reciever=input("enter the mail id for sending OTP")
    server.sendmail(sender,reciever,msg)
   # print("Boooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooom mail sent")
   #we will valide the otp
 a=input("enter a opt recieved")
   if a==OTP:
       print("transaction was succesfull")
   else:
       print("failed enter the Otp again")
#we have to communicate
       profile_name=input("enter the ig profile name ")
       #we will download the data
       m.download_profile(profile_name)
    #m.login(user.passwd)
    #if ypu want only profile picture from public profile
       m.download_profile(profile_name.profile_pic_only=True)
#now let us understnad some simple functions on time and datetime modules
import time
#first let us get the epoch time
epoch = time.time()#returns epoch time considering from 1970  jan 1st
#print(each)
#lert us get current time
  b=time.localtime(epoch)
  print(b)
  print(type(b))
  #from the above structure let us get only date
d=b.tm_mday
m=b.tm-hour
m=b.tm_min
print(f'Time now is {h}:{m}')
#in the similar way we have ctime()
f=time.ctime()
#print(f)
#print(type(f)) #returns  string format
#datetime module is a collection of date,time,datetime and timedelta methods
import datetime
#print(dir(datetime))
from datetime import datetime
a=datetime.now()
#print(a)
#print(type(a))

from datetime import *
#we want to get only date separately
b=date.today()
print(b)
#if you want to create a date object
c=date(2024,4,26)
print(c)
print(type(c))'''
from datetime import *

#if we want to return only timme
#d=datetime.time()
#print(d)
#formatting datetime-->strftime() (String Format converts datetimme into string
'''
%d-->day of the month%b-->short from the month  name %B-->Full name of month %y--->2digit year,%Y-->4digit year ,%a-->short form
'''
#take your desired date format
b=date.today()
f=b.strftime("Today is %A and this is %B and this is of  %j date of the year")
print(f)

#task-->Accept 3 inputs from the user as day ,month ,year  convert to date format #then given the name,day number of the year and #
#8106429771 
