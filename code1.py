# IMPORTS
import tkinter as tk
# Load the library for sounds 
root = tk.Tk()

# CONSTANTS
root.geometry("800x800")
X = -1
Y = -1
image=PhotoImage(file="vun.png")
# VARIABLES
grid = [[3,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,],
        [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,],
        [0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,],
        [0,0,1,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,],
        [0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,6,0,0,0,],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,],
        [0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,],
        [1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,],
        [0,0,0,0,0,1,0,0,0,0,0,6,0,0,0,0,1,0,0,0,],
        [0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
        [0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,]]
# FUNCTION
def getIndex3():
    global X,Y
    for index in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[index][i] == 3:
                Y =index
                X = i


def arrayToDrawing():
    for i in range(len(grid)):
        y1 = 40 * i
        y2 = 40+ y1
        for j in range(len(grid[0])):
            x1 = j*40
            x2 = x1 + 40
            if grid[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill = "black")  
            elif grid[i][j] ==  3 :
                canvas.create_oval(x1, y1, x2, y2, fill = "red") 
            elif grid[i][j] == 5 :
                canvas.create_rectangle(x1, y1, x2, y2, fill = "green")
            elif grid[i][j] == 6:
                canvas.create_oval(x1, y1, x2, y2, fill = "blue") 

# draw a line with white and black squares using the global array
def MoveLeft(event):
    global grid
    getIndex3()
    if X and grid[Y][X-1] == 0:
        grid[Y][X] = 0
        grid[Y][X-1] = 3
   
    arrayToDrawing()

    
def MoveRight(event):
    global grid
    getIndex3()
    if X<len(grid[0]) - 1 and grid[Y][X+1] == 0:
        grid[Y][X] = 0
        grid[Y][X+1] = 3
    
    arrayToDrawing()
def MoveUp(event):
    global grid 
    getIndex3() 
    if Y and grid[Y-1][X] == 0:
            grid[Y][X] = 0
            grid[Y-1][X] = 3
    
    arrayToDrawing()
def MoveDown(event):
    global grid
    getIndex3()
    if Y <len(grid)-1 and grid[Y+1][X] == 0:
        grid[Y][X] = 0
        grid[Y+1][X] = 3
    arrayToDrawing()

#LEFT CLICK
root.bind (" <Left> ", MoveLeft) 
#RIGHT CLICK
root.bind ( " <Right> ", MoveRight) 
#UP CLICK
root.bind ( " <Up> ", MoveUp) 
#DOWN CLICK 
root.bind ( " <Down> ", MoveDown)  



canvas = tk.Canvas (root)

canvas.pack(expand=True, fill="both")
arrayToDrawing()

root.mainloop()

