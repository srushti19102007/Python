#All the string fuctioins 
#print(help(str))


# String Functions
#name = input("Enter a name: ")
#ph = input("Enter Phone no: ")

#result = len(name)    # Prints the lengeth of the name
#result = name.find(" ")    # Finds space or a given chrechter in the entered string
#result = name.rfind("s")    # Finds space or a given chrechter in the entered string in reverse order
#result = name.capitalize()    # makes the first letter capital
#result = name.upper()    # makes all the charecters in the string upper cased
#result = name.lower()    # makes all the charecters in the string lower cased
#result = name.isdigit()    # checks if all the charecter in the string are numbers/digit
#result = name.isalpha()    # checks if all the charecter in the string are alphabets
#result = ph.count("-")    # counts spaces /character/alphabet given in parenthices ()
#result = ph.replace("-"," ")    # replaces the given symbol/charecter with given charecter/space

#print(result)


# Validate user input excercise
# 1. username is no more than 12 charecters
# 2. username must not contain sapaces
# 3. username must not contain digits

# 1. 
# username = input("Enter a name: ")
# if len(username) < 12:
#     print("Your name is: ",username)
# elif len(username) > 12:
#     print("The name should'nt be greater than 12 charecters")
# else:
#     print("Invalid Input... :)")

# 2.
# username = input("Enter a name: ")

# if username.find(" ") == -1:
#     print("Your name is: ",username)
# else:
#     print("The name should'nt contain space")

# 3.
username = input("Enter a name: ")

if username.isalpha():  #if username.isdigit() == "-1":
    print("Your name is: ",username)
else:
    print("The name should'nt contain digits")