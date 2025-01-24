"""#This is my first python program
#printing a statement
print("fish")
print("It's really good")

#variable = A contaier for a value (string,float,integer, boolean)
#           A variable behaves as if it was the value ot contain
#           A variable should have no space and should'nt start with numbers
a="Bro"
print(f"Hello {a}")
b=2
c=3
print(f"Addition is: {b+c}")

student = True
if student:
    print("You are a student")
else:
    print("You are not a student")

#Typecasting = The process of converting a variable feom one data type to anotheer 
#               str(),int(),float(),bool()

age = 20
name = "Srushti"
gpa = int(3.2)
is_student = True

print(type(age))
print(type(is_student))

print(gpa)
age = str(age) 
age += "1"
print(age)

name = bool(name)
print(name)

#input = A function that prompts the user to enter date return the data in a string

n = int(input("What is yor age?: "))
print("Your age is : ",n)
n=n+1
print(n) 

# Exercise 1 Rectangle Area Calc

length = int(input("Enetr the the length of a rectangle : "))
breadth = int(input("Enter the breadth of the rectangle : "))
area = length*breadth
print(f"The are of the rectangle is : {area}") 

#Exercise 2 shopping cart program
item = input("What iytem u wan to buy : ")
price = float(input("What is the price : "))
quantity = int(input("How many : "))
total=price*quantity
print("The toal price for yur item is : ",total)
print("The toal price for yur item is :  ${total}")  """

# madlibs game 
# word game where you create a story
# By filling in blankss with random words

adjective1 = input("Enter an adjective (DESCRIPTION): ")
noun1 = input("Enter a noun(person, place, thing): ")
adjective2=input("Enter an adjective (Description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3=input("Enter an adjective (Description): ")

print(f"Today I Went to a {adjective1} zoo.")
print(f"In a exhibit, I Saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")