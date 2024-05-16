# ========== 4.2.1 ==========
# def greatest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     return c
# print(greatest(3, 4, 1))
# print(greatest(99, -4, 7))
# print(greatest(0, 0, 0))

# ========== 4.2.2 ==========
# def same(word, index1, index2):
#     if index2 > len(word):
#         return False
#     elif word[index1] == word[index2]:
#         return True
#     elif word[index1] != word[index2]:
#         return False
    
# print(same("programmer", 0, 4))
# print(same("programmer", 6, 7))
# print(same("programmer", 0, 12))

# ========== 4.2.3 ==========
sentence = "My name is Sam"
def first(first):
    return sentence[0:2]
def second(second):
    return sentence[3:6]
def final(final):
    return sentence[25:]

print(first(sentence))
print(second(sentence))
print(final(sentence))