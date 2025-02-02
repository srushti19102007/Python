# import time
# # for loops = execute a block of code a fixed number of times.
# #             you can iterate over a range, string, sequence, etc

# # for x in range(1,11):
# #     print(x)

# # for x in reversed(range(1,11,2)):
# #     print(x)

# # credit_card = "1234-5678-9012"
# # for x in credit_card:
# #     if x == "1":
# #         continue
# #     else:
# #         print(x)

# # t = int(input("Enter time in secands: "))
# # time.sleep(t)
# # print("Time's Up")


# #count down timer program

# # t = int(input("Enter time in secands: "))

# # for x in range(t,0,-1):
# #     secand = x % 60
# #     minutes = int(x / 60) % 60
# #     hours = int(x / 3600)
# #     print(f"{hours:02}:{minutes:02}:{secand:02}")
# #     time.sleep(1)
# # print("Time's Up")


# #nested loop = A loop within anothen loop (outer,inner)
# #              outer loop:
# #                  inner loop:

# for x in range(3):
#     for y in range(1,11):
#         print(y,end=" ")
#     print()

# #rectangle
# rows = int(input("Enter the no of  rows: "))
# columns = int(input("Enter the no of  columns: "))
# symbol = input("Enter a symbol to use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol,end=" ")
#     print()

#collection = single "variable" used to store multiple values
#    List   = [] orderd and changable.duplicates OK
#    Set    = {} unorserd and immutable, but Add/Remove OK, No duplicates
#    Tuple  = () orderd and unchangable. Duplicates OK. Faster


#list []
# fruits = ["apple", "orange", "banana", "coconut"]
    # print(dir(fruits))
    # print(help(fruits))
    # print(len(fruits))
    # print("apple" in fruits)

    # fruits.sort()
    # fruits.reverse()
    # print(fruits.index("orange"))
    # print(fruits.count("banana"))
    # print(fruits.copy())
    # fruits.append("grape")
    # fruits.insert(1,"grape")
    # fruits.remove("orange")
    # print(fruits.pop())
    # fruits.clear()
# print(fruits)
    # for x in fruits:
    #     print(x)

#set []
# fruits = {"apple", "orange", "banana", "coconut"}
    # print(dir(fruits))
    # print(help(fruits))
    # print(len(fruits))
    # print("pineapple" in fruits)
    # fruits.add("pineapple")
    # fruits.remove("apple")
    # fruits.pop()
    # fruits.clear()
# print(fruits)

#tuple()
# fruits = ("apple", "orange", "banana", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# print(fruits)


# list of groceries
# fruits = ["Tomato","mango","watermelon"]
# vegetables = ["potato","carrot","cabbage"]
# meat = ["fish","chicken","turkey"]

# groceries = [fruits,vegetables,meat]
# print(fruits)
# print(groceries[0][0])
# print(groceries)

# 2D list of groceries
groceries = [["Tomato","mango","watermelon"],
             ["potato","carrot","cabbage"],
             ["fish","chicken","turkey"]]
for collection in groceries:
    for item in collection:
        print(item,end =" ")
    print()