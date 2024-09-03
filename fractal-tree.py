import tkinter
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
TREE_ROOT_X = WINDOW_WIDTH/2
TREE_ROOT_Y = WINDOW_HEIGHT
TREE_ANGLE = 90
BRANCH_STARTING_LENGTH = 180
BRANCH_ANGLE = 90
BRANCH_THICKNESS = 1
COLOR_STARTING_INDEX = 0
PALETTE_RAINBOW = ['red','orange','yellow','lime','cyan','blue','purple']
PALETTE_SAKURA = ['brown', 'brown', 'brown', 'brown', 'white', 'magenta']
PALETTE_GREEN = ['green']
COLOR_PALETTES = [PALETTE_RAINBOW, PALETTE_SAKURA, PALETTE_GREEN]
SELECTED_COLOR_PALETTE_INDEX = 0
COLOR_PALETTE = PALETTE_RAINBOW
BG_COLOR ='black'
MAX_ITERATIONS = 9
BRANCH_SHORTENING_FACTOR = 0.6


root = tkinter.Tk()
root.title = 'Fractal tree'
mouse_x = 0
mouse_y = 0
myCanvas = tkinter.Canvas(root,bg=BG_COLOR,width=WINDOW_WIDTH, height=WINDOW_HEIGHT)


def draw_branch(canvas, x0, y0,length,color, tree_angle, branch_angle_counter, branch_angle,max_iterations, iterations):
    # Branch starts to be drawn here.
    # We start at x0,y0. 
    # x1,y1 will be the result of calculating the second coordinate using length and angle
    x1 = x0+length*math.cos((tree_angle+branch_angle_counter)*math.pi/180)
    y1 = y0-length*math.sin((tree_angle+branch_angle_counter)*math.pi/180)

    canvas.create_line(x0,y0,x1,y1, fill=COLOR_PALETTE[color % len(COLOR_PALETTE)], width=BRANCH_THICKNESS)
    if iterations < max_iterations:
        draw_branch(canvas, x1, y1, length*BRANCH_SHORTENING_FACTOR, color+1, tree_angle,branch_angle_counter+branch_angle,branch_angle, max_iterations, iterations+1)
        draw_branch(canvas, x1, y1, length*BRANCH_SHORTENING_FACTOR, color+1, tree_angle,branch_angle_counter-branch_angle,branch_angle, max_iterations, iterations+1)

def draw_fractal_tree(canvas, tree_root_x, tree_root_y, starting_branch_length, color, tree_angle, branch_angle, max_iterations):
    myCanvas.delete('all')
    draw_branch(canvas, tree_root_x, tree_root_y, starting_branch_length, color, tree_angle, 0, branch_angle, max_iterations, 0)
    root.after(16, draw_fractal_tree,myCanvas,TREE_ROOT_X, TREE_ROOT_Y, (WINDOW_HEIGHT-mouse_y)/WINDOW_HEIGHT*BRANCH_STARTING_LENGTH, 0,TREE_ANGLE, mouse_x/WINDOW_WIDTH*BRANCH_ANGLE, MAX_ITERATIONS)

def get_mouse_position(event):
    global mouse_x
    global mouse_y
    mouse_x = event.x
    mouse_y = event.y

def increase_max_iterations(event):
    global MAX_ITERATIONS
    if(MAX_ITERATIONS < 20):
        MAX_ITERATIONS += 1

def decrease_max_iterations(event):
    global MAX_ITERATIONS
    if(MAX_ITERATIONS > 0):
        MAX_ITERATIONS -= 1

def next_color_palette(event):
    global COLOR_PALETTE
    global COLOR_PALETTES
    global SELECTED_COLOR_PALETTE_INDEX
    SELECTED_COLOR_PALETTE_INDEX +=1
    COLOR_PALETTE = COLOR_PALETTES[SELECTED_COLOR_PALETTE_INDEX]

def previous_color_palette(event):
    global COLOR_PALETTE
    global COLOR_PALETTES
    global SELECTED_COLOR_PALETTE_INDEX
    SELECTED_COLOR_PALETTE_INDEX -=1
    COLOR_PALETTE = COLOR_PALETTES[SELECTED_COLOR_PALETTE_INDEX]

def increase_shortening_factor(event):
    global BRANCH_SHORTENING_FACTOR
    BRANCH_SHORTENING_FACTOR += 0.1

def decrease_shortening_factor(event):
    global BRANCH_SHORTENING_FACTOR
    BRANCH_SHORTENING_FACTOR -= 0.1

def increase_thickness(event):
    global BRANCH_THICKNESS
    if(BRANCH_THICKNESS < 500):
        BRANCH_THICKNESS += 1

def decrease_thickness(event):
    global BRANCH_THICKNESS
    if(BRANCH_THICKNESS > 0):
        BRANCH_THICKNESS -= 1



myCanvas.pack()
myCanvas.bind('<Motion>', get_mouse_position)
root.bind('<Up>', increase_max_iterations)
root.bind('<Down>', decrease_max_iterations)
root.bind('<Left>', previous_color_palette)
root.bind('<Right>', next_color_palette)
root.bind('w', increase_shortening_factor)
root.bind('s', decrease_shortening_factor)
root.bind('q', increase_thickness)
root.bind('a', decrease_thickness)

draw_fractal_tree(myCanvas, TREE_ROOT_X, TREE_ROOT_Y, BRANCH_STARTING_LENGTH, 0, TREE_ANGLE,BRANCH_ANGLE, MAX_ITERATIONS)
root.mainloop()