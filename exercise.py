#shpping cart progream

# foods =[]
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input("Enter the price of {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("--------YOR CART -------")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total+=price

# print()
# print("Your Total is: $", total) 


# 2D Tuples no_keypad
# no = ((1,2,3),
#       (4,5,6),
#       (7,8,9),
#       ("*",0,"#"))

# for row in no:
#     for item in row:
#         print(item, end=" ")
#     print()


# quiz game
questions = ("1. What is the capital of Australia?",
            "2. Which planet is known as the 'Red Planet'?",
            "3. Who invented the telephone?",
            "4. What is the smallest ocean in the world?",
            "5. Which gas is most abundant in the Earth's atmosphere?")

options = (("A) Sydney","B) Melbourne","C) Canberra","D) Brisbane"),
            ("A) Earth","B) Mars","C) Jupiter","D) Venus"),
            ("A) Thomas Edison","B) Alexander Graham Bell","C) Nikola Tesla","D) James Watt"),
            ("A) Indian Ocean","B) Arctic Ocean","C) Atlantic Ocean","D) Pacific Ocean"),
            ("A) Oxygen","B) Carbon Dioxide","C) Nitrogen","D) Hydrogen:"))

answers = ("C","B","B","B","C")
guesses = []
score = 0
quest_no = 0

for question in questions:
    print("------------------------------------")
    print(question)
    for option in options[quest_no]:
        print(option)

    guess = input("Enter your choice(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[quest_no]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"{answers[quest_no]} is the correct answer")
    quest_no += 1


print("------------------------------------")
print("               RESULT               ")
print("------------------------------------")

print("Answer= ",end="")
for answer in answers:
    print(answer,end = " ")

print()
print("Guesses= ",end="")
for guess in guesses:
    print(guess,end = " ")

print()
# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        while True:
            try:
                price = float(input(f"Enter the price of {food}: $"))
                break
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        foods.append(food)
        prices.append(price)

print("\n--------YOUR CART-------")

for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")

total = sum(prices)
print(f"\nYour Total is: ${total:.2f}")


# 2D Tuples no_keypad
no = ((1, 2, 3),
      (4, 5, 6),
      (7, 8, 9),
      ("*", 0, "#"))

for row in no:
    for item in row:
        print(item, end=" ")
    print()


# Quiz Game
questions = ("1. What is the capital of Australia?",
             "2. Which planet is known as the 'Red Planet'?",
             "3. Who invented the telephone?",
             "4. What is the smallest ocean in the world?",
             "5. Which gas is most abundant in the Earth's atmosphere?")

options = (("A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"),
          ("A) Earth", "B) Mars", "C) Jupiter", "D) Venus"),
          ("A) Thomas Edison", "B) Alexander Graham Bell", "C) Nikola Tesla", "D) James Watt"),
          ("A) Indian Ocean", "B) Arctic Ocean", "C) Atlantic Ocean", "D) Pacific Ocean"),
          ("A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"))

answers = ("C", "B", "B", "B", "C")
guesses = []
score = 0
quest_no = 0

for question in questions:
    print("\n------------------------------------")
    print(question)
    for option in options[quest_no]:
        print(option)

    while True:
        guess = input("Enter your choice(A, B, C, D): ").upper()
        if guess in ["A", "B", "C", "D"]:
            guesses.append(guess)
            break
        else:
            print("Invalid choice. Please enter A, B, C, or D.")

    if guess == answers[quest_no]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"{answers[quest_no]} is the correct answer")
    quest_no += 1

print("\n------------------------------------")
print("               RESULT               ")
print("------------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

print()
print("------------------------------------")
score = score / len(questions) * 100
print(f"\nYour score is: {score:.2f}%")
