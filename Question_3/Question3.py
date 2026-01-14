"""
Create a program that uses a recursive function to generate a geometric pattern using
Python's turtle graphics. The pattern starts with a regular polygon and recursively
modifies each draw_recursive_edge to create intricate designs.


Pattern Generation Rules:

For each edge of the shape:
1. 2. 3. 4. Divide the edge into three equal segments
Replace the middle segment with two sides of an equilateral triangle pointing
inward (creating an indentation)
This transforms one straight edge into four smaller edges, each 1/3 the length of
the original edge
Apply this same process recursively to each of the four new edges based on the
specified depth.

"""


#Import all functions and classes from the turtle graphics library so they can be used directly.
import turtle


def draw_recursive_edge(t,length, depth):
  
  if depth == 0:
    t.forward(length)
  else:
    segment= length / 3 #hfh

    draw_recursive_edge(t,segment, depth - 1) #Segment 1
    
    t.right(60) #turn inward
    
    #Segment 2 down into indentation 
    draw_recursive_edge(t,segment, depth - 1)
    
    t.left(120) # turns outward to come back up
    
    #segment 3 up out of indentation
    draw_recursive_edge(t,segment, depth - 1)
    t.right(60)
    
    #Segment 4
    draw_recursive_edge(t,segment, depth - 1)
    
def main ():
  # setting up screen
  screen = turtle.Screen() #Create a screen object
  screen.title("Recursive Geometric Pattern") # Set the title of the window
  screen.bgcolor("white") # Set background color to white

#Settig up Turtle
  pen = turtle.Turtle()
  pen.speed(0) # Set the fastest drawing speed
  pen.color("black") # Set pen color to black
  pen.pensize(1) 
  
  #Get user inputs for sides, length, and depth
  try:
    sides = int(input("Enter the number of sides:"))
    length = float(input("Enter the side length:"))
    depth = int(input("Enter the recursion depth:"))
  except ValueError:
    print("Invalid input. Please enter numeric values.")
    return
  
  #Center the drawing shape position
  pen.penup()
  pen.goto(-length / 2, length / 2) # Move to starting position
  pen.pendown() 
  
  #Draw the recursive polygon
  angle = 360 / sides 
  for _ in range(sides): # For each side of the polygon
    draw_recursive_edge(pen,length, depth)
    pen.right(angle) # Turn the turtle to the right to form the polygon.


  pen.hideturtle()
    #Complete the drawing and wait for user to close the windowcreen.mainloop()
  screen.mainloop()
  
if __name__ == "__main__": #Run the main function if this script is executed directly
  main()








