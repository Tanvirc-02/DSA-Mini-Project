import random

ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92,80: 99}
snake = {32: 10, 34: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}
pos1 = 0  #position of player one
pos2 = 0  #position of player two

def move(pos):  #function move with argument position
    dice = random.randint(1,6)
    print(f"Dice : {dice}")
    pos = pos + dice
    if pos in snake:
        print("-> ***BITTEN BY SNAKE***")
        pos = snake[pos]
        print(f"Position : {pos}")
    elif pos in ladder:
        print("-> CLIMBED A LADDER!!!")
        pos = ladder[pos]
        print(f"Position : {pos}")
    else:
        print(f"-> Position : {pos}")
    print("\n--------------------------------------\n")
    return pos

while True:
    A = input("PLAYER 1:\nEnter any key to throw dice:")
    pos1 = move(pos1)  #calling move function
    if pos1 >= 100:
        print("**********************************")
        print("PLAYER 1 WINS!!!".center(30," "))
        print("GAME OVER".center(30," "))
        print("**********************************")
        break
    B = input("PLAYER 2:\nEnter any key to throw dice:")
    pos2 = move(pos2)  #calling move function
    if pos2 >= 100:
        print("**********************************")
        print("PLAYER 1 WINS!!!".center(30, " "))
        print("GAME OVER".center(30, " "))
        print("**********************************")
        break
