""" Create a program that uses a recursive function to generate a geometric pattern using
Python's turtle graphics. The pattern starts with a regular polygon and recursively
modifies each draw_recursive_edge to create intricate designs.
"""


#Import all functions and classes from the turtle graphics library so they can be used directly.
from turtle import *
#Prompt the user to enter the number of sides of the initial polygon.
sides = int(input("Enter the number of sides: "))
#Prompt the user to enter the length of each side of the polygon.
length = int(input("Enter the side length: "))
#Prompts the user to enter the recursion depth.
depth = int(input("Enter the recursion depth: "))

# Set the turtle drawing speed. The smaller the number, the slower the drawing speed. The number 0 is the fastest.
speed(0)
# Lift the pen so the turtle can move without drawing.
# Move the turtle to the position (-150,150) without drawing.
# Lower the pen so drawing begins.
penup()
goto(-150, 150)
pendown()
def draw_recursive_edge(length, depth):
  if depth == 0:
    forward(length)
  else:
    length /= 3
    draw_recursive_edge(length, depth - 1)
    right(60)
    draw_recursive_edge(length, depth - 1)
    left(120)
    draw_recursive_edge(length, depth - 1)
    right(60)
    draw_recursive_edge(length, depth - 1)
angle = 360 / sides
for _ in range(sides):
  draw_recursive_edge(length, depth)
  right(angle)
done()






