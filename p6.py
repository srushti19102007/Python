# format specifiers = {value:flags} format a value based on 
#                      what flags are inserted

# price1 = 30.1456
# price2 = -94.66
# price3 = 5477.89

# print(f"Price1 is: {price1:10}")  # leaves 10 spaces to the left
# print(f"Price2 is: {price2:,}")
# print(f"Price3 is: {price3:+10}")  #assigns {+/-} sign

# print(f"Price1 is: {price1:<10}")  # no to left
# print(f"Price2 is: {price2:>10}")  #no to right
# print(f"Price3 is: {price3:^10}")  #no to center

# print(f"Price1 is: {price1:.2f}")  # 2 = no of digit after decimal, f = float datatype
# print(f"Price2 is: {price2:+.2f}") #assigns {+/-} sign
# print(f"Price3 is: {price3:+,.2f}")  #assigns {+/-} sign, gives proper(,)

# while loop = execute some code WHILE some condition remains true

# WAP to print even number using while loop and logical operator
# num = int(input("Enter a number: "))
# while not num%2 != 0:
#     print("The number is Even ")
#     num = int(input("Enter another number: "))
# print("The number is Odd.")

# # WAP to quit when u want
# food = input("Enter your favourite food: ")
# while not food == "q":
#     print("Your favourite food is: ",food)
#     food = input("Enter your favourite food press (q) to quit: ")
# print("You have quited successfully.. :)")


#command intrest calculation

principal = 0
rate = 0
time = 0

while principal <= 0 :
   principal = float(input("Enter the principal amount: "))
   if principal <= 0:
       print("Principal can't be less than 0")

while rate <= 5 :
   rate = float(input("Enter the rate of intrest: "))
   if rate <= 0:
       print("rate of intrest can't be less than 0")

# while time <= 0 :
#    time = float(input("Enter the time in years: "))
#    if time <= 0:
#        print("time can't be less than or equal to 0")
#OR
while True :
   time = float(input("Enter the time in years: "))
   if time <= 0:
       print("time can't be less than or equal to 0")
   else :
        break

final_a = principal*(1+rate/100)**time
print(f"The final/total amount after {time} year's is: ${final_a:.2f}")