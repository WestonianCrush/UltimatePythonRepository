# ========== 4.3.1 ==========
# list = [1, 2, 3, 4, 5]
# while True:
#     index = int(input("Index: "))
#     if index == -1:
#         break
#     New = int(input("New Value: "))
#     list.pop(index)
#     list.insert(index, New)
#     print(list)
# ========== 4.3.2 ==========
# list = []
# items = int(input("How many items: "))
# while items > 0:
#     word = input(f"Item {items}: ")
#     list.append(word)
#     items -= 1
# print(list)
# ========== 4.3.3 ==========
# list = []
# while True:
#     print("The list is now", list)
#     option = input("A(d)d, (r)emove or e(x)it: ")
#     if option == "x":
#         print("Bye!")
#         break
#     elif option == "d":
#         list.append(len(list)+1)
#     elif option == "r":
#         list.remove(len(list))
# ========== 4.3.4 ==========
list = []
num = 0
while True:
     word = input("Word: ")
     if word in list:
        print("You typed in", num, "different words")
        break
     else: 
        list.append(word)
        num += 1
        print(list)

