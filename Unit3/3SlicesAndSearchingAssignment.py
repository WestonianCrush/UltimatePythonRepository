# ========== 3.3.1 ==========
# text = input("Please type in a string: ")
# endpos = 1
# while True:
#     ex = text[0:endpos]
#     endpos += 1
#     print(ex)
#     if len(ex) == len(text):
#         break

# ========== 3.3.2 ==========
# text = input("Please type in a string: ")
# endpos = len(text) - 1
# while True:
#     ex = text[endpos:len(text)]
#     endpos -= 1
#     print (ex)
#     if len(ex) == len(text):
#         break
# ========== 3.3.3 ==========
# text = input("Please type in a string: ")
# if "a" in text:
#     print("A found")
# else:
#     print("A not found")
# if "e" in text:
#     print("E found")
# else:
#     print("E not found")
# if "o" in text:
#     print("O found")
# else:
#     print("O not found")
# ========== 3.3.4 ==========
# word = input("Please type in a word: ")
# char = input("Please type in a character: ")
# if char in word:
#     ex = word.find(char)
#     if ex+3 > len(word):
#         print()
#     else:
#         print(word[ex:ex+3])
        
# ========== 3.3.5 ==========
# word = input("Please type in a word: ")
# char = input("Please type in a character: ")
# while True:
#     if char in word:
#         ex = word.find(char)
#     elif ex+3 > len(word):
#         print()
#     else:
#         print(word)
#         word = word[2:]

# ========== 3.3.6 ==========
string = input("Please type in a string: ")
sub = input("Please type in a substring: ")
position = string.find(sub)
part = string[position+1:]
newpos = part.find(sub)
finalpos = position + newpos + 1
if newpos == -1:
        print("This Substring does not occur twice")
else:
        print("The 2nd occurrence of the substring is at index:" , finalpos )
 

