# ========== 4.1.1 ==========
def line(num, string):
    if string == "":
        string = "*"
    letter = string[0]
    print(letter*num)

# line(7, "%")
# line(10, "LOL")
# line(3, "")
# ========== 4.1.2 ==========
# def box(height):
#     times = height
#     while times > 0:
#         line(10, "#")
#         times -= 1

# box(5)
# print()
# box(2)
# ========== 4.1.3 ==========
# def hash(length):
#     times = length
#     while times > 0:
#         line(length, "#")
#         times -= 1

# hash(5)
# print()
# hash(2)
# ========== 4.1.4 ==========
# def square(num, char):
#     index = num
#     while index > 0:
#         line(num, char)
#         index -= 1

# square(5, "*")
# print()
# square(3, "o")
# ========== 4.1.5 ==========
# def triangle(size):
#     long = 1
#     while long < size+1:
#         line(long, "#")
#         long += 1

# triangle(6)
# print()
# triangle(3)
# ========== 4.1.6 ==========
# def shape(num1, char1, num2, char2):
#     index = num2
#     long = 1
#     while long < num1+1:
#         line(long, char1)
#         long += 1
#     while index > 0:
#         line(num1, char2)
#         index -=1

# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")
# ========== 4.1.7 ==========
def spruce(num):   
    print("A spruce!")
    