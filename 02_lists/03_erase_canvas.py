"""
Problem Statement
Implement an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

The eraser is a rectangle that can be moved around the canvas. When the eraser is moved, it should erase all of the cells it touches. The eraser should be a different color than the cells on the canvas.
"""

# for graphics
import tkinter as tk

# for set the hight and width of the canvas
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# for set the size of the eraser
ERASER_SIZE = 20
CELL_SIZE = 40

# function to erase the cells
def erase_objects(canvas, eraser, cells):
    # Get eraser's current position
    eraser_coords = canvas.coords(eraser)
    ex1, ey1, ex2, ey2 = eraser_coords

    for cell in cells:
        x1, y1, x2, y2 = canvas.coords(cell)
        # Check if the eraser overlaps the cell
        if not (ex2 < x1 or ex1 > x2 or ey2 < y1 or ey1 > y2):
            canvas.itemconfig(cell, fill='white')

# function to move the eraser
def on_mouse_move(event):
    # Move eraser
    canvas.coords(erasers, event.x , event.y , event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    erase_objects(canvas, erasers, grid_cells)

# Create the main window
root = tk.Tk()
root.title("Eraser on Canvas")

# Create a canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()


# Create a grid of cells
grid_cells = []

for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        cell = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue')
        grid_cells.append(cell)


# Create an eraser
erasers = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

# Bind the mouse movement to the on_mouse_move function
canvas.bind("<Motion>", on_mouse_move)

# Start the Tkinter event loop
root.mainloop()
