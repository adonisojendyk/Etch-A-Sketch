print("Hello World!")

import os
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Etch A Sketch")

player = turtle.Turtle()
player.color("black")
player.shape("square")
player.pensize(5)

playerspeed = 15

def move_left():
    x = player.xcor()
    x -= playerspeed
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    player.sety(y)

def color_green():
    player.color("green")

def color_pink():
    player.color("pink")

def color_black():
    player.color("black")

def color_yellow():
    player.color("yellow")

def color_orange():
    player.color("orange")

def color_red():
    player.color("red")

def color_purple():
    player.color("purple")

def color_white():
    player.color("white")

def color_blue():
    player.color("blue")

def bkcolor_black():
    wn.bgcolor("black")

def bkcolor_white():
    wn.bgcolor("white")

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(color_green, "g")
turtle.onkey(color_pink, "p")
turtle.onkey(color_black, "b")
turtle.onkey(color_yellow, "y")
turtle.onkey(color_orange, "o")
turtle.onkey(color_red, "r")
turtle.onkey(color_purple, "u")
turtle.onkey(color_white, "w")
turtle.onkey(color_blue, "e")
turtle.onkey(bkcolor_black, "space")
turtle.onkey(bkcolor_white, "h")
