#!/usr/bin/python
import turtle

def draw_square(box):
     for i in range(1,5):
         box.forward(100)
         box.right(90)

def draw_art():    
    window = turtle.Screen()
    window.bgcolor("orange")

    #create a square
    brad = turtle.Turtle()
    draw_square(brad)

    #create circle
    beth = turtle.Turtle()
    beth.color("blue")
    beth.circle(100)

    
    

    window.exitonclick()

draw_art()
