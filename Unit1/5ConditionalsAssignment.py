
# print("########## 1.5.1 ##########")
# name = int(input("Please type in a number: "))
# if name == 1984:
#     print("Orwell")

# print("########## 1.5.2 ##########")
# num = int(input("Please type in a number: "))
# if num < 0:
#     print(num*-1)
# else:
#     print(num)

# print("########## 1.5.3 ##########")
# customer = input("Please type in your name: ")
# if customer == "Jerry":
#     print("Next Please!")
# else:
#     por = int(input("How many portions of soup? "))
#     print("The total cost is", por*5.90)
#     print("Next Please!")

# print("########## 1.5.4 ##########")
# number = int(input("Type in a number: "))
# if number < 1000:
#     print("This number is smaller than 1000")
# if number < 100:
#     print("This number is smaller than 100")
# if number < 10:
#     print("This number is smaller than 10")
# print("Thank You!")

# print("########## 1.5.5 ##########")
# num1 = int(input("Number 1: "))
# num2 = int(input("Number 2: "))
# op = input("Operation: ")
# if op == "add":
#     print(num1 , "+" , num2 , "=" , num1+num2)
# if op == "subtract":
#     print(num1 , "-" , num2 , "=" , num1-num2)
# if op == "multiply":
#     print(num1 , "*" , num2 , "=" , num1*num2)

# print("########## 1.5.6 ##########")
# tempf = int(input("Type in a temperature (F): "))
# tempc = (tempf - 32) / 1.8
# print(tempf , "degrees Farenheit equals" , tempc , "degrees Celsius")
# if tempc < 0:
#     print("Brr! It's cold in here!")

# print("########## 1.5.7 ##########")
# wage = float(input("Hourly wage: "))
# hours = float(input("Hours worked: "))
# day = input("Day of the week: ")
# sun = (hours*wage)*2
# if day == "sunday":
#     print("Daily wages:" , "$" , sun)
# else:
#     print("Daily wages:" , "$" , wage*hours)

# print("########## 1.5.8 ##########")
# # Fix the program
# points = int(input("How many points are on your card? "))
# if points < 100:
#     points *= 1.1
#     print("Your bonus is 10 %")

# else:
#     points *= 1.15
#     print("Your bonus is 15 %")

# print("You now have", points, "points")

print("########## 1.5.9 ##########")
print("What is the weather forecast for tomorrow?")
tem = int(input("Temperature: "))
rain = input("Will it rain? (yes/no): ")
if tem > 20:
    print("Wear jeans and a T-shirt")
if tem <= 20:
    print("Wear jeans and a T-shirt")
    print("I recommend a sweater as well")
if tem <= 10:
    print("Take a jacket with you")
if tem <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
