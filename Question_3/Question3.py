""" Create a program that uses a recursive function to generate a geometric pattern using
Python's turtle graphics. The pattern starts with a regular polygon and recursively
modifies each draw_recursive_edge to create intricate designs.
"""


#Import all functions and classes from the turtle graphics library so they can be used directly.
import turtle


def draw_recursive_edge(t,length, depth):
  
  if depth == 0:
    t.forward(length)
  else:
    segment= length / 3

    draw_recursive_edge(t,segment, depth - 1)
    t.right(60)
    draw_recursive_edge(t,segment, depth - 1)
    t.left(120)
    draw_recursive_edge(t,segment, depth - 1)
    t.right(60)
    draw_recursive_edge(t,segment, depth - 1)
    
def main ():
  # setting up screen
  screen = turtle.Screen()
  screen.title("Recursive Geometric Pattern")
  screen.bgcolor("white")

#Settig up Trurtle
  pen = turtle.Turtle()
  pen.speed(0)
  pen.color("black")
  pen.pensize(1)
  
  #User inputs
  try:
    sides = int(input("Enter the number of sides:"))
    length = float(input("Enter the side length:"))
    depth = int(input("Enter the recursion depth:"))
  except ValueError:
    print("Invalid input. Please enter numeric values.")
    return
  
  #Center the drawing shape position
  pen.penup()
  pen.goto(-length / 2, length / 2)
  pen.pendown()
  
  #Draw the recursive polygon
  angle = 360 / sides
  for _ in range(sides):
    draw_recursive_edge(pen,length, depth)
    pen.right(angle) # Turn the turtle to the right to form the polygon.


  pen.hideturtle()
    #Complete the drawing and wait for user to close the windowcreen.mainloop()
  screen.mainloop()
  
if __name__ == "__main__":
  main()







