
import turtle

def draw_recursive_edge(t, length, depth): # to draw one edge with recursion

    if depth == 0:
        t.forward(length)
    else:
        segment = length / 3

        # Segment 1
        draw_recursive_edge(t, segment, depth - 1)
        
        t.right(60)  # turn inward
        
        # Segment 2 down into indentation
        draw_recursive_edge(t, segment, depth - 1)
        
        t.left(120)  # turns outward to come back up
        
        # Segment 3 up out of indentation
        draw_recursive_edge(t, segment, depth - 1)
        
        t.right(60)
        
        # Segment 4
        draw_recursive_edge(t, segment, depth - 1)