import turtle
import turtle as t

import turtle

def square(side):
    for i in range(4):
        t.forward(side)
        t.left(90)



def row(w, side):
    for i in range(w):
        square(side)
        t.forward(side)
    t.penup()
    t.left(180)
    t.forward(w * side)
    t.left(180)
    t.pendown()




def grid(l, w, side):
    t.speed(0)
    for i in range(l):
        row(w, side)
        t.penup()
        t.left(90)
        t.forward(side)
        t.right(90)
        t.pendown()
    t.penup()
    t.right(90)
    t.forward(l * side)
    t.left(90)
    t.pendown()

def connect_four():
    connect_four = turtle.Screen()
    t.penup()
    t.goto(-350,300)
    t.pendown()
    t.speed(0)
    t.color("blue")
    t.width(5)

    t.goto(350,300)
    t.goto(350,200)

    t.goto(-350,200)
    t.goto(-350,100)

    t.goto(350,100)
    t.goto(350,0)

    t.goto(-350,0)
    t.goto(-350,-100)

    t.goto(350,-100)
    t.goto(350,-200)

    t.goto(-350,-200)
    t.goto(-350,-300)
    t.goto(350,-300)

    t.goto(350,300)
    t.goto(250,300)

    t.goto(250,-300)
    t.goto(150,-300)

    t.goto(150,300)
    t.goto(50,300)

    t.goto(50,-300)
    t.goto(-50,-300)

    t.goto(-50,300)
    t.goto(-150,300)

    t.goto(-150,-300)
    t.goto(-250,-300)

    t.goto(-250,300)
    t.goto(-350,300)
    t.goto(-350,-300)

    move = 30 * [0]
    c = 7
    r = 6
    board = [[9] * c for i in range(r)]

    
    print(board)

    player = 1
    col = 0
    game_on = True
    row = 0

    while (game_on):
        col = int(input("What column?"))
        for r in range (0,5):
            if board[r][col-1] == 9:
                board[r][col-1] = player
                row = r
                break
        if player == 1:
            t.color("red")
        else:
            t.color("yellow")
        t.penup()
        t.goto((col-4)*100,((row-3)*100))
        t.pendown()
        t.circle(50)
        for w in range(0,6):
            for y in range(0,4):
                if board[w][y] == board[w][y+1] == board[w][y+2] == board[w][y+3] and board[w][y] != 9:
                    if player == 1:
                        print("Player 1 wins!")
                    else:
                        print("Player 2 wins!")
                    game_on = False
        for w in range(0,3):
            for y in range(0,7):
                if board[w][y] == board[w+1][y] == board[w+2][y] == board[w+3][y] and board[w][y] != 9:
                    if player == 1:
                        print("Player 1 wins!")
                    else:
                        print("Player 2 wins!")
                    game_on = False
        for w in range(0,3):
            for y in range(0,4):
                if board[w][y] == board[w+1][y+1] == board[w+2][y+2] == board[w+3][y+3] and board[w][y] != 9:
                    if player == 1:
                        print("Player 1 wins!")
                    else:
                        print("Player 2 wins!")
                    game_on = False
        player = not(player)


def snakes_and_ladders():
    import random
    snakes_and_ladders = turtle.Screen
    
    t.speed(0)
    
    grid(10,10,40)
    one = turtle.Turtle()
    one.shape("turtle")
    one.color("red")
    one.penup()
    one.goto(20,10)
    one_value = 1
    
    two = turtle.Turtle()
    two.shape("turtle")
    two.color("blue")
    two.penup()
    two.goto(20,30)
    two_value = 1
    dice = 0
    
    game_on = True
    while game_on == True:
        roll = input("Player 1, press enter to roll the die.")
        if roll == "":
            dice = random.randint(1,6)
            print(dice)
            one_value += dice
            
        if one_value > 100:
            one_value = one_value - dice
            
        if one_value <= 10:
            one.goto(20+40*(one_value-1),10)
        elif one_value <= 20:
            one.goto(400-(20+40*(one_value-11)),50)
        elif one_value <= 30:
            one.goto(20+40*(one_value-21),90)
        elif one_value <= 40:
            one.goto(400-(20+40*(one_value-31)),130)
        elif one_value <= 50:
            one.goto(20+40*(one_value-41),170)
        elif one_value <= 60:
            one.goto(400-(20+40*(one_value-51)),210)
        elif one_value <= 70:
            one.goto(20+40*(one_value-61),250)
        elif one_value <= 80:
            one.goto(400-(20+40*(one_value-71)),290)
        elif one_value <= 90:
            one.goto(20+40*(one_value-81),330)
        elif one_value <= 100:
            one.goto(400-(20+40*(one_value-91)),370)

        if one_value == 2:
            one_value = 38
            print("You climbed up a ladder!")
        if one_value == 4:
            one_value = 14
            print("You climbed up a ladder!")
        if one_value == 9:
            one_value = 31
            print("You climbed up a ladder!")
        if one_value == 21:
            one_value = 42
            print("You climbed up a ladder!")
        if one_value == 28:
            one_value = 84
            print("You climbed up a ladder!")
        if one_value == 51:
            one_value = 67
            print("You climbed up a ladder!")
        if one_value == 71:
            one_value = 91
            print("You climbed up a ladder!")
        if one_value == 80:
            one_value = 100
            print("You climbed up a ladder!")
        if one_value == 17:
            one_value = 7
            print("you fell down a snake!")
        if one_value == 54:
            one_value = 34
            print("you fell down a snake!")
        if one_value == 62:
            one_value = 19
            print("you fell down a snake!")
        if one_value == 64:
            one_value = 60
            print("you fell down a snake!")
        if one_value == 87:
            one_value = 24
            print("you fell down a snake!")
        if one_value == 93:
            one_value = 73
            print("you fell down a snake!")
        if one_value == 95:
            one_value = 75
            print("you fell down a snake!")
        if one_value == 98:
            one_value = 79
            print("you fell down a snake!")
        if one_value == 100:
            print("Player 1 wins!")
            game_on = False
            break

        roll = input("Player 2, press enter to roll the die.")
        if roll == "":
            dice = random.randint(1,6)
            print(dice)
            two_value += dice
            
        if two_value > 100:
            two_value = two_value - dice
            
        if two_value <= 10:
            two.goto(20+40*(two_value-1),30)
        elif two_value <= 20:
            two.goto(400-(20+40*(two_value-11)),70)
        elif two_value <= 30:
            two.goto(20+40*(two_value-21),110)
        elif two_value <= 40:
            two.goto(400-(20+40*(two_value-31)),150)
        elif two_value <= 50:
            two.goto(20+40*(two_value-41),190)
        elif two_value <= 60:
            two.goto(400-(20+40*(two_value-51)),230)
        elif two_value <= 70:
            two.goto(20+40*(two_value-61),270)
        elif two_value <= 80:
            two.goto(400-(20+40*(two_value-71)),310)
        elif two_value <= 90:
            two.goto(20+40*(two_value-81),350)
        elif two_value <= 100:
            two.goto(400-(20+40*(two_value-91)),390)

        if two_value == 2:
            two_value = 38
            print("You climbed up a ladder!")
        if two_value == 4:
            two_value = 14
            print("You climbed up a ladder!")
        if two_value == 9:
            two_value = 31
            print("You climbed up a ladder!")
        if two_value == 21:
            two_value = 42
            print("You climbed up a ladder!")
        if one_value == 28:
            two_value = 84
            print("You climbed up a ladder!")
        if two_value == 51:
            two_value = 67
            print("You climbed up a ladder!")
        if two_value == 71:
            two_value = 91
            print("You climbed up a ladder!")
        if two_value == 80:
            two_value = 100
            print("You climbed up a ladder!")
        if two_value == 17:
            two_value = 7
            print("you fell down a snake!")
        if two_value == 54:
            two_value = 34
            print("you fell down a snake!")
        if two_value == 62:
            two_value - 19
            print("you fell down a snake!")
        if two_value == 64:
            two_value = 60
            print("you fell down a snake!")
        if two_value == 87:
            two_value = 24
            print("you fell down a snake!")
        if two_value == 93:
            two_value = 73
            print("you fell down a snake!")
        if two_value == 95:
            two_value = 75
            print("you fell down a snake!")
        if one_value == 98:
            two_value = 79
            print("you fell down a snake!")
        if two_value == 100:
            print("Player 2 wins!")
            game_on = False
            break
        
ex = 0
wy = 0

def get_coor(x, y):
    ex = x
    wy = y
    if player == True:
            t.penup()
            t.goto(ex//100*100+50, wy//100*100+15)
            t.pendown()
            t.circle(35)
            
    else:
        t.penup
        t.goto(ex//100*100+20, wy//100*100+20)
        t.pendown()
        t.goto(ex//100*100+80, wy//100*100+80)
        t.penup
        t.goto(ex//100*100+20, wy//100*100+80)
        t.pendown()
        t.goto(ex//100*100+80, wy//100*100+20)
    
def tic_tac_toe():
    
    game_on = True
    c = 3
    r = 3
    board = [[9] * c for i in range(r)]
    move = 9
    coor = [0,0]
    player = 1
    
    tic = turtle.Screen()
    grid(3,3,100)

    while game_on == True:
        turtle.onscreenclick(get_coor)
        
        



            

game = input("Choose what game you want to play, Connect Four, Snakes and Ladders, Tic-tac-toe")

if game == ("Connect Four"):
    connect_four()
if game == ("Snakes and Ladders"):
    snakes_and_ladders()    
if game == ("Tic-tac-toe"):
    tic_tac_toe()
