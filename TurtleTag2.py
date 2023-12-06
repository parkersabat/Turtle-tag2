from turtle import *
import pdb

win = Screen()
runner = Turtle()
tagger = Turtle()
runner.color("Blue")
tagger.color("Red")

currentPlayer = 0

win.listen()


def Up():
    global currentPlayer
    if currentPlayer == 0:
        return

    tagger.setheading(90)
    tagger.forward(20)
    currentPlayer = 0


def Down():
    global currentPlayer

    if currentPlayer == 0:
        return

    tagger.setheading(270)
    tagger.forward(20)
    currentPlayer = 0


def Left():
    global currentPlayer

    if currentPlayer == 0:
        return

    tagger.setheading(180)
    tagger.forward(20)
    currentPlayer = 0


def Right():
    global currentPlayer

    if currentPlayer == 0:
        return

    tagger.setheading(0)
    tagger.forward(20)
    currentPlayer = 0


def Runnerup():
    global currentPlayer

    if currentPlayer == 1:
        return

    runner.setheading(90)
    runner.forward(20)
    currentPlayer = 1


def Runnerdown():
    global currentPlayer

    if currentPlayer == 1:
        return

    runner.setheading(270)
    runner.forward(20)
    currentPlayer = 1


def Runnerleft():
    global currentPlayer

    if currentPlayer == 1:
        return

    runner.setheading(180)
    runner.forward(20)
    currentPlayer = 1


def Runnerright():
    global currentPlayer

    if currentPlayer == 1:
        return

    runner.setheading(0)
    runner.forward(20)
    currentPlayer = 1


print(
    """
Runner moves with wasd
Tagger moves with ijkl"""
)

win.onkey(Runnerup, "w")
win.onkey(Runnerdown, "s")
win.onkey(Runnerleft, "a")
win.onkey(Runnerright, "d")
win.onkey(Up, "i")
win.onkey(Down, "k")
win.onkey(Left, "j")
win.onkey(Right, "l")

win.mainloop()
