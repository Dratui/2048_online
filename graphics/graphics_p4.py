from tkinter import *
from board import Board

## Graphical values

TILES_FG_COLOR = {None:"#ffffff", 0:"#ff0000", 1:"#ffff00"}

TILES_FONT = ("Verdana", 20, "bold")

## Code starts here

def initialization():
    # Creates the window
    window = Tk()
    return window
    
def update_display():
    # Size of the grid. Should be choosen by the user thanks to another function
    grid_size = (Board.height,Board.wwidth)
    
    # Single grid. Should be created by the init function
    game_grid = Board.get_grid()
    
    # Lists of canvas and buttons
    list_canvas = [[None for j in range(grid_size[1])] for i in range(grid_size[0])]
    list_buttons = [None for j in range(grid_size[1])]
    
    # Display function, called at the beginning and then at every change
    def display():
        
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                case = Canvas(window, bg = "#ffffff", height = 50, width = 50)
                case.grid_propagate(0)
                case.grid(column = y, row = x)
                text = Label(case, text = 'O', fg = TILES_FG_COLOR[game_grid[x][y]], bg = "#ffffff", font = TILES_FONT)
                text.place(x=25, y=25, anchor="center")
        for y in range(grid_size[1]) :
            button = Button(window, text = "Ici", height = 3, width = 6, command = lambda arg = y : click(arg))
            button.grid_propagate(0)
            button.grid(column = y, row = 0)
            list_buttons[y] = button
            
    # Update function
    def click(i):
        Board.input = str(i+1)
    
        display()
        window.update()
    
        
    display()
    window.mainloop()
    
def close_window(window):
    # Closes the window
    window.destroy
