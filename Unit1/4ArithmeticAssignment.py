print("########## 1.4.1 ##########")
num = input("please type in a number: ")
print (int(num) * 5)

print("########## 1.4.2 ##########")
name = input("What is your name? ")
year = input("What year were you born? ")
print("Hi", name, ", you will be" , (2024 - int(year)), "years old at the end of the year 2024")

print("########## 1.4.3 ##########")
days = input("How many days? ")
print("seconds in that many days:", (int(days) * 24 * 60 * 60))
      
print("########## 1.4.4 ##########")
# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)

print("########## 1.4.5 ##########")
num1 = input("Number 1: ")
num2 = input("Number 2: ")
print("The sum of the numbers:", int(num1) + int(num2))
print("The product of the numbers:", int(num1) * int(num2))

print("########## 1.4.6 ##########")
numb1 = input("Number 1: ")
numb2 = input("Number 2: ")
numb3 = input("Number 3: ")
numb4 = input("Number 4: ")
sum = int(numb1) + int(numb2) + int(numb3) + int(numb4)
print("The sum of the numbers is", sum, "and the mean is", int(sum) / 4)

print("########## 1.4.7 ##########")
caf = input("How many times a week do you eat at the student cafeteria? ")
price = input("The price of a typical student lunch? ")
groc = input("How much money do you spend on groceries in a week? ")
print("Average food expenditure:")
spent = float(caf) * float(price) + float(groc)
print("Daily: $", float(spent) / 7)
print("Weekly: $", float(spent))

print("########## 1.4.8 ##########")
