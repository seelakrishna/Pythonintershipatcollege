#task1 :Maka sure your program excuted for 5 times by accepting inviduals #name,height,weight and display BMI

print("BMI CALCULATOR:")
for i in range(5):
    name=input("enter your name:")
    weight=int(input("Enter your weight(in Kgs):"))
    height=float(input("Enter your height(in meters ):"))
    bmi=(weight/(height**2))
    print(f"{name}'s  your weight{weight} , your height {height} and BMI is: {bmi:.2f}")
