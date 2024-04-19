# # ========== 2.3.1 ==========
# while True:
#     print("Hi")
#     msg = input("Shall we continue? ")
#     if msg == "no":
#         print("Okay Then")
#         break

# # ========== 2.3.2 ==========
# while True:
#     num = int(input("Please type in a number: "))
#     if num < 0:
#         print("invalid Number")  
#     elif num == 0:
#         print("Exiting...")
#         break
#     elif num > 0:
#         from math import sqrt
#         print(sqrt(num))

# # ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#     print(number)
#     number = number - 1
#     if number == 0:
#      break
# print("Now!")

# ========== 2.3.4 ==========
# while True:
#     pass1 = input("Password: ")
#     pass2 = input("Confirm Password: ")
#     if pass1 == pass2: 
#         print("Account Created!")
#         break
#     print("They do not match! ")

# ========== 2.3.5 ==========
# Attempts = 0
# while True:
#     Pin = 4321
#     userpin = int(input("PIN: "))
#     if Pin != userpin:
#         success = False
#         Attempts += 1
#         print("Wrong")
#     elif Pin == userpin:
#         success = True
#         break
# if Attempts < 1:
#     print("Correct! It only took you a single attempt!")
# else:
#     print("Correct! It only took you", (Attempts), "Attempts!")
# ========== 2.3.6 ==========
# year = int(input("Year: "))
# rem = 0
# while True: 
#     rem = year % 4
#     leapyear = (year - rem + 4)
#     print("the next leap year is", (leapyear) )
#     break

# ========== 2.3.7 ==========
# story = ""
# while True:
#     word = input("Please type in a word: ")
#     if word == "end":
#         print(story)
#         break
#     else:
#         story = story + " " + word
# ========== 2.3.8 ==========
# story = ""
# rwrd = ""
# while True:
#     word = input("Please type in a word: ")
#     if word == "end":
#         print(story)
#         break
#     elif rwrd == word:
#         print(story)
#         break
#     else:
#         word != "end"
#         rwrd = word
#         story += rwrd + " "
# ========== 2.3.9 ==========
print("Please type in integer numbers. Type 0 to end. ")
totnum = 0
sumnum = 0
mean = 0
pos = 0
neg = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        print("Numbers typed in:" , totnum)
        print("Sum:", sumnum)
        print("Mean:", mean)
        print("Positive:", pos)
        print("Negative:", neg)
    else:
        totnum += 1
        sumnum += number
        mean = sumnum/totnum
        if number > 0:
            pos += 1
        else:
            neg += 1


