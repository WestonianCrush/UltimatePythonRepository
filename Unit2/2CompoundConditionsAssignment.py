# print("########## 2.2.1 ##########")
# age = int(input("What is your age? "))
# if age <= 5 and age >= 1:
#     print("You are too young")
# elif age < 0:
#     print("Enter a valid number")
# else:
#     print("You are" , age , "years old.")
# print("########## 2.2.2 ##########")
# name = input("What is your name? ")
# if name == "Huey" or name == "Dewey" or name == "Louie":
#     print("You could be one of Donald Ducks nephews")
# elif name == "Morty" or name == "Ferdie":
#     print("You could be one of Mickey Mouses nephews")
# else:
#     print("You cant be a nephew of a character I know of")
# print("########## 2.2.3 ##########")
# grade = int(input("Enter your score: "))
# if grade <= 100 and grade >= 90:
#     print("You have an A")
# elif grade <= 89 and grade >= 80:
#     print("You have a B")
# elif grade <= 79 and grade >= 70:
#     print("You have a C")
# elif grade <= 69 and grade >= 60:
#     print("You have a D")
# elif grade <= 59 and grade >= 0:
#     print("You have an F")
# elif grade < 0 or grade > 100:
#     print("Enter a valid percent")
# print("########## 2.2.4 ##########")
# Number = int(input("Enter a number: "))
# if Number % 5 == 0 and Number % 3 == 0:
#     print("BuzzFizz")
# elif Number % 3 == 0:
#     print("Fizz")
# elif Number % 5 == 0:
#     print("Buzz")
# print("########## 2.2.5 ##########")
# year = int(input("Type in a year: "))
# if year % 4 == 0 and year % 100 == 0:
#     print("That is not a leap year")
# elif year % 400 == 0:
#     print("That is a leap year")
# elif year % 4 == 0:
#     print("That is a leap year")
# else:
#     print("That is not a leap year")
# print("########## 2.2.6 ##########")
let1 = input("1st letter: ")
let2 = input("2nd letter: ")
let3 = input("3rd letter: ")
if let1 > let2 and let1 < let3:
    print(let1)
elif let2 < let1 and let2 > let3:
    print(let2)
elif let2 > let1 and let2 < let3:
    print(let2)
elif let1 < let2 and let1 > let3:
    print(let1)
else:
    print(let3)