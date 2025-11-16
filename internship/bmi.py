print("BMI CALCULATOR:")
for i in range(0,4):
    name=input("enter your name:")
    weight=int(input("Enter your weight(in Kgs):"))
    height=float(input("Enter your height(in meters ):"))
    bmi=(weight/(height**2))
    if height > 0 and weight > 0:
        if bmi<18.5:
            print( name ,'ni BMI' ,bmi, 'edhi...sannaga unnav ra ayya....')
        elif bmi>18.5 and bmi<24.9:
            print( name ,'ni BMI' ,bmi, 'edhi...parla baganey dengi thintunav ga .....')
        elif bmi>25 and bmi<29.9:
            print( name ,'ni BMI' ,bmi, ' edhi...Gym ki pora ayya...')
        else:
            print( name ,'ni BMI', bmi ,'edhi...Obesity...')


