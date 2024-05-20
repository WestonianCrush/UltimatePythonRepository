due = 50
while True:
    print("Amount due:" , due)
    coin = int(input("Insert Coin: "))
    if coin == 25:
        due -= 25
    elif coin == 10:
        due -= 10
    elif coin == 5:
        due -= 5
    else:
        print("This coin type is not supported")
    if due == 0:
        print("Change owed:" , due)
        break
    if due < 0:
        due = due*-1
        print("Change owed:" , due)
        break

