# ========== 3.4.1 ==========
# def SevenDwarves():
#     print('bashful\ndoc\ndopey\ngrumpy\nhappy\nsleepy\nsneezy')
# SevenDwarves()
# ========== 3.4.2 ==========
# def firstchar(word):
#     print(word[0:1])
# firstchar('python')
# firstchar('yellow')
# firstchar('tomorrow')
# firstchar('heliotrope')
# firstchar('open')
# firstchar('night')
# ========== 3.4.3 ==========
# def mean(x, y, z):
#     sum = x + y + z
#     print(sum/3)
# mean(5, 3, 1)
# mean(10, 1, 1)
# ========== 3.4.4 ==========
# def printmanytimes(text, times):
#     print(text*times)

# printmanytimes("hi \n", 5)
# printmanytimes("All Pythons, except one, grow up. \n", 3)
# ========== 3.4.5 ==========
# def hashsquare(length):
#     n1 = length
#     while n1 > 0:
#         print("#"*length)
#         n1 -= 1

# hashsquare(3)
# print()
# hashsquare(5)
# ========== 3.4.6 ==========
def chess(length):
    counter = 0
    nlines = length
    while nlines > 0:
        nchars = length
        while nchars > 0:
            if counter % 2 == 0:
                print("1", end="")
                nchars -= 1
            else:
                print("0", end="")
                nchars -= 1
            counter += 1
        nlines -= 1
        if length % 2 == 0:
            counter -= 1
        print()

chess(3)