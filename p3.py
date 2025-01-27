""" # Write a code to check if the user is eligible to drive or not , 
# using if condition

age = int(input("Enter the age: "))
if age >= 18:
    print("You are now eligible to drive... :)")

# Write a code to check if the number is even or odd , 
# using else-if condition and elif  condition

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even...")
elif num% 2 != 0:
    print("The number is odd...")
else:
    print("Invalid input...") 

# Python Calculator

operator = input("Enter a operator (+,-,*,/): ")
num1 = float(input("Enter a for 1st number: "))
num2 = float(input("Enter a for 2nd number: "))

if operator == "+":
    print("The result of 1st and 2nd number is: ",round(num1+num2,3))
elif operator == "-":
    print("The result of 1st and 2nd number is: ",round(num1-num2,3))
elif operator == "*":
    print("The result of 1st and 2nd number is: ",round(num1*num2,3))
elif operator == "/":
    print("The result of 1st and 2nd number is: ",round(num1/num2,3))
else:
    print(f"{operator} is an Invalid operator... :)") 

# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit kilogram or pound?? (K or L): ")

if unit == "K":
    print("The weight converted in kilogram is: ",round(weight*2.205,3))
elif unit == "L":
    print("The weight converted in pound is: ",round(weight/2.205,3))
else:
    print("Invalid input... :)") """

# Temprature converter

temp = float(input("Enter a tempature: "))
unit = input("Enter a Unit in celcius or fahrenheit (C/F): ")

if unit == "C":
    print("The temprature in celcius is: ",round((temp*9)/5+32,3))
elif unit == "F":
    print("The temprature in fahrenheit is: ",round((temp-32)*5/9,3))
else:
    print("Invalid input... :)")