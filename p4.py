""" #Square root of a number
no = float(input("Enter a number: "))
print("The number is: ",no)
print("The square root of the number: ",no*no)

# Surface volume and area of a cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = 3.14 * radius ** 2 * height
surface_area = 2 * 3.14 * radius * (radius + height)

print(f"Volume of the cylinder: {volume:}")
print(f"Surface area of the cylinder: {surface_area}") 

# Logical Operators = Evaluate multiple condition (or,and,not)
#                     or = at least one condition must be true
#                     and = both condition must be true 
#                     not = invert the condition (not false, not true)

# Out Door event using or operator

temp = int(input("Enter a temprature in celcius: "))
rain = input("Is it raining?? (Yes/No): ")

if temp >36 or temp<0 or rain == "Yes":
    print("It is not a good day for an out door event")
else:
    print("It is a good day for an out door event") 

# Check if the weather outside is hot, warm, cold using and, not operator

temp=int(input("Enter a temprature in celcius: "))
sunny = input("Is The weather Hot?? (Yes/No): ")

if temp>=36 and sunny == "Yes":
    print("It is Hot outside.")
elif temp<0 and sunny == "No":
    print("It is Cold outside.")
elif temp>28 and temp<0 and sunny =="Yes":
    print("It is warm outside.")
elif temp>=36 and not sunny == "Yes":
    print("It is Hot outside.")
elif temp<0 and not sunny == "No":
    print("It is Cold outside.")
elif temp>28 and not temp<0 and not sunny =="Yes":
    print("It is warm outside.")
else:
    print("Invalid Input") """

# Conditional Operator = A one-line shortcut for the if-else statement 
#                        (ternary Operator)print or assign of 2 values based o a condition 
#                        x if condition else y

# Check if the no is even odd using conditional/ternary Operator
num = int(input("Enter a number: "))
result = "Even" if num%2 == 0 else "Odd"
print("The given number is : ",result)
