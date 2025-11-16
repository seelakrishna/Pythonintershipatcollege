#otp validation
import smtplib #for sending of emails
import random #for generating random data
import math
def rps():
    """***ROCK PAPER SCISSORS***"""
    print("***ROCK PAPER SCISSORS***")
    options=['ROCK','PAPER','SCISSORS']
    #random options took by computer
    M= random.choice(options)
    c=input("Enter your choise IN ROCK PAPER SCISSORS):").upper()#converts the lower case words to uppper case
    if (c=="ROCK"and M=="PAPER") or (c=="PAPER" and M=="SCISSORS") or (c=="SCISSORS"  and M=="ROCK"):
        #for the above condition gets satisfied this block will be executed
        print("you lost...the game")
        print(f"computer choise={M}")
    elif c==M:
         #for the above condition gets satisfied this block will be executed
        print("tie break...")
        print(f"computer choise={M}")
    else:
         #for the above condition gets satisfied this block will be executed
        print("you wonnn....")
        print(f"computer choise={M}")
def bmi():
    """***BMI CALCULATOR***"""
    print("***BMI CALCULATOR***")
    name=input("enter your name:")#name of the person
    weight=int(input("Enter your weight(in Kgs):"))#parameters for BMI
    height=float(input("Enter your height(in meters):"))#parameters for BMI
    #formula for bmin calculation
    bmi=(weight/(height**2))
    if height > 0 and weight > 0:
        if bmi<18.5:
            #if bmi is less than 18.5 this will be printed
            print( name ,'ni BMI' ,bmi, 'koncham  thinnu bro....')
        elif bmi>18.5 and bmi<24.9:
            #if bmi is in between 18.5 and 24.9 this will be printed
            print( name ,'ni BMI' ,bmi, 'very healthy.....')
        elif bmi>25 and bmi<29.9:
            #if bmi is in between 25 and 29.9 this will be printed
            print( name ,'ni BMI' ,bmi, ' better  to workout...')
        else:
            #if bmi is greater than 30 this will be printed
            print( name ,'ni BMI', bmi ,'Obesity...')
def otp():
    '''Code for otp generation1: take all possible digits'''
    digits="0123456789"
    #this will be output vairable ->otp
    OTP = ""#this will be updated
    #we are trying to get 6 digit no. randomly generated step by step
    for i in range(6) :
        OTP += digits[math.floor((random.random())*10)]
        #print(OTP)
        #Now we will send above otp as a message to user
    msg = "Your transaction code is \n"+OTP+"."
    #print(msg)
    #using email automation code
    server = smtplib.SMTP('smtp.gmail.com',587)
    #Now start transaction
    server.starttls() # Transport Layer enables the port connection
    # Make the login
    server.login("podurivatsalya@gmail.com","6349 7311 6672 8424")
    # now we will send the mail
    sender = "podurivatsalya@gmail.com.com"
    receiver = input("Enter mail id for sending otp")
    server.sendmail(sender,receiver,msg)
    #print("Boom mail sent")
    a = input("Enter the OTP received")
    if a == OTP :
        rps()#calling ***ROCK PAPER SCISSORS***
    else :
        bmi()#calling ***BMI CALCULATOR***

otp()#calling otp function

    
