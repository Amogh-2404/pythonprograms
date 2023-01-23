import turtle
from turtle import Screen,Turtle
import time

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
#range function is not pure python and comes from the C language and does not let us pass the values to the functions using names.
    for seg_num in range(len(segments)-1,0,-1):  #We are trying to go backwards in the list using the range function.
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)






screen.exitonclick()