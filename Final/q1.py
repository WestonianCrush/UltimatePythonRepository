fname = input("Please type in your first name: ")
lname = input("Please type in your last name: ")
gpa = float(input("Please type in your gpa: "))
hybrid = lname[0]
sch = ""
amt = ""
if hybrid == "A" or hybrid == "B" or hybrid == "C" or hybrid == "D" or hybrid == "E" or hybrid == "F" or hybrid == "G" or hybrid == "H" or hybrid == "I" or hybrid == "J" or hybrid == "K":
    sch = "Monday & Thursday" 
else:
    sch = "Tuesday & Friday"
if gpa > 3.86:
    amt = "$16000"
elif gpa < 3.85 and gpa > 3.7:
    amt = "$12000"
elif gpa < 3.69 and gpa > 3.49:
    amt = "$8000"
elif gpa < 4.98 and gpa > 3.25:
    amt = "$4000"
else:
    amt = "$0"
print("Hello," , fname , "You should report to school on" , sch , "You are eligible for a scholarship of", amt)