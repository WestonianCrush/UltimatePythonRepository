math = input("Enter Expression: ")
num1 = int(math[0])
exp = math[1]
num2 = int(math[2])
if exp == "+":
    print(num1 , "+" , num2 , "=" , num1+num2)
if exp == "-":
    print(num1 , "-" , num2 , "=" , num1-num2)
if exp == "*":
    print(num1 , "*" , num2 , "=" , num1*num2)
if exp == "/":
    print(num1 , "/" , num2 , "=" , num1/num2)