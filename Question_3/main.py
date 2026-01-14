"""
Group: DAN/EXT 14
Main program to draw recursive geometric patterns using turtle graphics.
"""
import turtle
from turtleREC import draw_recursive_edge
from config import (
    SCREEN_TITLE, SCREEN_BGCOLOR, PEN_COLOR, PEN_SIZE, PEN_SPEED,
    MIN_SIDES, MAX_SIDES, MIN_LENGTH, MAX_LENGTH, MIN_DEPTH, MAX_DEPTH
)

def get_user_input(): #getting user input for side,length, and depth
   
    try:
        sides = int(input("Enter the number of sides (0-10): "))
        length = float(input("Enter the side length (50-500):"))
        depth = int(input("Enter the recursion depth (0-8): "))
        
        # To validate the user input ranges
        if not (MIN_SIDES <= sides <= MAX_SIDES):
            print("Error: Sides must be between {MIN_SIDES} and {MAX_SIDES}")
            return None
        if not (MIN_LENGTH <= length <= MAX_LENGTH):
            print("Error: Length must be between {MIN_LENGTH} and {MAX_LENGTH}")
            return None
        if not (MIN_DEPTH <= depth <= MAX_DEPTH):
            print("Error: Depth must be between {MIN_DEPTH} and {MAX_DEPTH}")
            return None
        
        return sides, length, depth
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None

#To initialize and configure the turtle screen
def setup_screen():
   
    screen = turtle.Screen()
    screen.title(SCREEN_TITLE)
    screen.bgcolor(SCREEN_BGCOLOR)
    return screen

def setup_turtle(): #To initialize and configure the turtle pen
   
    pen = turtle.Turtle()
    pen.speed(PEN_SPEED)
    pen.color(PEN_COLOR)
    pen.pensize(PEN_SIZE)
    return pen

# To draw the recursive geometric pattern
def draw_pattern(pen, sides, length, depth):
  
    # Center the drawing
    pen.penup()
    pen.goto(-length / 2, length / 2)
    pen.pendown()
    
    # To draw the polygon
    angle = 360 / sides
    for _ in range(sides):
        draw_recursive_edge(pen, length, depth)
        pen.right(angle)
# To run the main program
def main():

    print("=== Recursive Geometric Pattern Generator ===\n")
    
    # To setup screen and turtle pen
    screen = setup_screen()
    pen = setup_turtle()
    
    # To get user input
    user_input = get_user_input()
    if user_input is None:
        print("Program terminated due to invalid input.")
        return
    
    sides, length, depth = user_input
    
    # To draw pattern
    print(f"\nDrawing {sides}-sided pattern with depth {depth}...")
    draw_pattern(pen, sides, length, depth)
    
    pen.hideturtle()
    print("Drawing complete! Close the window to exit.")
    screen.mainloop()

if __name__ == "__main__":
    main()