#  concession stand program usig dictionary

menu =  {
        "chips":10.00,
        "soup":20.00,
        "icecream":40.20,
        "burger":50.00,
        "fries":15.24,
        "soda":30.45,
        "bhail":20.25
        }

cart = []
total = 0

# print("\nMenu:")
# for item in menu:
#     print(f"{item:10} : {menu.get(item):.2f}")  

# OR

print("---------Menu---------")
for key,value in menu.items():
    print(f"{key:10} : {value:.2f}")
print("----------------------")
print()

while True:
    food = input("Add item to the cart, press(q to quit): ").lower()
    if food == 'q':
        break
    elif food in menu:
        cart.append(food)
        total += menu.get(food)

print("\n---------Your Cart---------")
for item in cart:
    print(item,end=" ")
print("\n----------------------")
print(f"Total: ${total:.2f}")

