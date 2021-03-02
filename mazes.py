# IMPORTS
import Tkinter as tk
# Load the library for sounds 
root = tk.Tk()
canvas = tk.Canvas (root)
# CONSTANTS
global Score
Score = 0

X = -1
Y = -1
Myimage=tk.PhotoImage(file="vun.png")
wall=tk.PhotoImage(file="pic.png")
coin=tk.PhotoImage(file="hah.png")
bg=tk.PhotoImage(file="gan.png")
# canvas.create_image(200,200,image=bg)
# VARIABLES
grid = [[3,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,],
        [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,],
        [1,6,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,],
        [1,0,1,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,],
        [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,6,0,0,0,],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,],
        [0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,],
        [0,0,0,0,0,1,0,0,0,0,0,0,6,1,0,0,0,0,0,0,],
        [1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,],
        [0,0,0,0,0,1,0,0,0,0,0,6,0,0,0,0,1,0,0,0,],
        [0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,]]
# FUNCTION
screen_height = 46*len(grid)+75
screen_width = 46*len(grid[0])
root.geometry(str(screen_width)+"x"+str(screen_height))


time_left = 30

def timer():
    global time_left
    time_left -= 1
    canvas.after(1000, lambda:timer())


def getIndex3():
    global X,Y
    for index in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[index][i] == 3:
                Y =index
                X = i


def arrayToDrawing():
    canvas.delete("all")
    for i in range(len(grid)):
        y1 = 46 * i
        y2 = 46+ y1
        for j in range(len(grid[0])):
            x1 = j*46
            x2 = x1 + 46
            if grid[i][j] == 1:
                canvas.create_image(x1,y1,anchor =tk.NW, image= wall)  
            elif grid[i][j] ==  3:
                canvas.create_image(x1,y1,anchor = tk.NW, image= Myimage) 
            elif grid[i][j] == 5 :
                canvas.create_image(x1, y1, image = bg)
            elif grid[i][j] == 6:
                canvas.create_image(x1, y1,anchor=tk.NW, image = coin) 
            # elif grid[i][j] ==0:
                # canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="white")

# draw a line with white and black squares using the global array




def MoveLeft(event):
    
    global grid,Score
    getIndex3()
    if X >0:
        if grid[Y][X-1] == 0:
            grid[Y][X] = 0
            grid[Y][X-1] = 3
        elif grid[Y][X-1]==6:
            grid[Y][X] = 0
            grid[Y][X-1] = 3
            Score+=1
            str_score.set('Your Score:' + str(Score))
        
    arrayToDrawing()

    
def MoveRight(event):
    
    global grid,Score
    getIndex3()
    if X<len(grid[0]) - 1:
        if grid[Y][X+1] == 0:
            grid[Y][X] = 0
            grid[Y][X+1] = 3
        elif grid[Y][X+1]==6:
            grid[Y][X]=0
            grid[Y][X+1]=3
            Score+=1
            str_score.set('Your Score:' + str(Score))
    arrayToDrawing()

def MoveUp(event):
    global gri,Score
    getIndex3() 
    if Y :
        if  grid[Y-1][X] == 0:
            grid[Y][X] = 0
            grid[Y-1][X] = 3
        elif grid[Y-1][X]==6:
            grid[Y][X] = 0
            grid[Y-1][X] = 3
            Score+=1
            str_score.set('Your Score:' + str(Score))
    arrayToDrawing()
def MoveDown(event):
    global grid,Score
    getIndex3()
    if Y <len(grid)-1 :
        if grid[Y+1][X] == 0:
           grid[Y][X] = 0
           grid[Y+1][X] = 3
        elif grid[Y+1][X] == 6:
            grid[Y][X] = 0
            grid[Y+1][X] = 3
            Score+=1
            str_score.set('Your Score:' + str(Score))
        elif grid[Y+1][X]==5:
            over_lavel = tk.Label(root, text = 'YOU WIN', font = ('Regular script', 35), width = 20, height = 1)
            over_lavel.place(x = 200, y = 500 , bg=None)

    arrayToDrawing()

#LEFT CLICK
root.bind (" <Left> ", MoveLeft) 
#RIGHT CLICK
root.bind ( " <Right> ", MoveRight) 
#UP CLICK
root.bind ( " <Up> ", MoveUp) 
#DOWN CLICK 
root.bind ( " <Down> ", MoveDown)  


str_score = tk.StringVar()
score_label = tk.Label(root, textvariable = str_score, font = ('Regular script', 20), width = 15, height = 1)
str_score.set('Your Score:' + str(Score))
score_label.place(x=300,y=900)

canvas.pack(expand=True, fill="both")
arrayToDrawing()

root.mainloop()

