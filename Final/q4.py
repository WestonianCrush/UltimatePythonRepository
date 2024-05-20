 
def score(word):
    place = 0  
    points = 0  
    while True:      
        if word[place] == "a" or word[place] == "e" or word[place] == "i" or word[place] == "o" or word[place] == "u" or word[place] == "l" or word[place] == "n" or word[place] == "s" or word[place] == "t" or word[place] == "r":
            points += 1
            place += 1
        elif word[place] == "d" or word[place] == "g":
            points += 2
            place += 1
        elif word[place] == "b" or word[place] == "c" or word[place] == "m" or word[place] == "p":
            points += 3
            place += 1
        elif word[place] == "f" or  word[place] == "h" or word[place] == "v" or word[place] == "w" or word[place] == "y":
            points += 4
            place += 1
        elif word[place] == "k":
            points += 5
            place += 1
        elif word[place] == "j" or word[place] == "x":
            points += 8
            place += 1
        elif word[place] == "q" or word[place] == "z":
            points += 10
            place += 1
        if place == len(word):
            print(points)
            break

print(score("hello"))
print(score("world"))
print(score("zebra"))
print(score("xylophone"))