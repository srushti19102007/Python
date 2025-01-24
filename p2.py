import math
""" #Arithmetic Operator
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

c = a+b
print("The Addition is: ",c)

s = a-b
print("The Subtraction is: ",s)

m = a*b
print("The Multiplication is: ",m)

d = a/b
print("The Division is: ",d)

mo = a%b
print("The Modulud is: ",mo)

e = a**b
print("The exponantial is: ",e)

f = a//b
print("The Floor Division is: ",f) 

# Math Operation
x = 3.14
y = -4
z = 5

#result = round(x)
#result = abs(y)
#result = pow(4,3)
#result = max(x,y,z)
result = min(x,y,z)

print(result)

# math

x=9.3

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)

print(result) """

# Exercise
#exercise1 : Calaculate the circumference,area of a circle

radius=float(input("Enter the radius of the circle: "))
circumference =round( 2 * math.pi * radius )
area=math.pi*pow(radius,2)
print("The circumference of the circle is: ",circumference)
print("The area of the circle is: ",round(area,2))

#exercise2 : Calculate the hypotenius of a right angled triangle

a=float(input("Enter the side A : "))
b=float(input("Enter the side B : "))
c=math.sqrt(pow(a,2)+pow(b,2))
print("The hypotenius of the triangle is: ",round(c))