name = input("Enter your Name : ")
weight = float(input("Enter your Weight in Kilograms : "))
height = float(input("Enter your Height in Meters : "))
BMI = weight / (height * height)
print("Your BMI is : " , BMI)

if BMI>0:
    if BMI<18.5:
        print(name,', you are Underweight')
    elif BMI<=24.9:
        print(name,', you are Normal Weight!')
    elif BMI<=29.9:
        print(name,', you are Overweight')
    elif BMI<=34.9:
        print(name,', you are Obese')
    elif (BMI<=39.9):
        print(name,", you are severely obese.")
    else:
        print(name,", you are morbidly obese.")
else:
    print("Enter valid input")