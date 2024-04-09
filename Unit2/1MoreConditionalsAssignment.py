# print("########## 2.1.1 ##########")
word = input ("please type in a word: ")
print ("There are" , len(word) , "letters in the word" , (word))
print ("Thank you!")
# print("########## 2.1.2 ##########")
num = float(input("Please type in a number: "))
print ("Integer part:" , int(num))
print ("Decimal part:" , float(num) - int(num))
# print("########## 2.1.3 ##########")
age = int(input("How old are you? "))
if age > 17:
    print ("You may vote!")
else:
    print ("You may not vote")
# print("########## 2.1.4 ##########")
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in another number: "))
if num1 > num2:
    print("The grater number was" , num1)
elif num1 < num2:
    print("The greater number was" , num2)
else:
    print("The numbers are equal!")
# print("########## 2.1.5 ##########")
p1n = input("Enter 1st persons name: ")
p1a = int(input("Enter 1st persons age: "))
p2n = input("Enter 2nd persons name: ")
p2a = int(input("Enter 2nd persons age: "))
if p1a > p2a:
    print("The elder is", p1n)
elif p1a < p2a:
    print("The elder is", p2n)
else:
    print(p1n , "and" , p2n , "are the same age")

# print("########## 2.1.6 ##########")
wrd1 = str(input("Please type in the 1st word: "))
wrd2 = str(input("Please type in the 2nd word: "))
if wrd1 < wrd2:
    print(wrd2 , "comes alphabetically last")
elif wrd1 > wrd2:
    print(wrd1 , "comes alphabetically last")
else:
    print("You gave the same word twice")
