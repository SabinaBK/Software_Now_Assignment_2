from turtle import *
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))
speed(0)
penup()
goto(-150,150)
pendown()
def egde(length, depth):
  if depth == 0:
    forward(length)
  else:
    length/=3
    egde(length, depth-1)
    right(60)
    egde(length, depth-1)
    left(120)
    egde(length, depth-1)
    right(60)
    egde(length, depth-1)
angle = 360/sides
for _ in range(sides):
  egde(length, depth)
  right(angle)

Screen.exitonclick()
