#-----Task Description-----------------------------------------------#
#
#  NOT CONNECT-4
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "play_game".  You are required to
#  complete this function so that when the program is run it fills
#  a grid with various rectangular tokens, using data stored in a
#  list to determine which tokens to place and where.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *

# Define constant values for setting up the drawing canvas
cell_size = 100 # pixels (default is 100)
num_columns = 7 # cells (default is 7)
num_rows = 6 # cells (default is 6)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the board
y_margin = cell_size // 2 # pixels, the size of the margin below/above the board
canvas_height = num_rows * cell_size + y_margin * 2
canvas_width = num_columns * cell_size + x_margin * 2

# Validity checks on board size
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert num_columns >= 7, 'Board must be at least 7 columns wide'
assert num_rows >= 6, 'Board must be at least 6 rows high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_legend_spaces = True, # show text for legend
                          mark_axes = True, # show labels on axes
                          bg_colour = 'light grey', # background colour
                          line_colour = 'slate grey'): # line colour for board
    
    # Set up the drawing canvas with enough space for the board and
    # legend
    setup(canvas_width, canvas_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the board
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the board
    left_edge = -(num_columns * cell_size) // 2 
    bottom_edge = -(num_rows * cell_size) // 2

    # Draw the horizontal grid lines
    setheading(0) # face east
    for line_no in range(0, num_rows + 1):
        penup()
        goto(left_edge, bottom_edge + line_no * cell_size)
        pendown()
        forward(num_columns * cell_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for line_no in range(0, num_columns + 1):
        penup()
        goto(left_edge + line_no * cell_size, bottom_edge)
        pendown()
        forward(num_rows * cell_size)

    # Mark the centre of the board (coordinate [0, 0])
    penup()
    home()
    dot(10)

    # Optionally label the axes
    if mark_axes:

        # Define the font and position for the labels
        small_font = ('Arial', (18 * cell_size) // 100, 'normal')
        y_offset = (27 * cell_size) // 100 # pixels

        # Draw each of the labels on the x axis
        penup()
        for x_label in range(0, num_columns):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('a')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, num_rows):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

    # Optionally mark the spaces for drawing the legend
    if mark_legend_spaces:
        # Font for marking the legend's position
        big_font = ('Arial', (24 * cell_size) // 100, 'normal')
        # Left side
        goto(-(num_columns * cell_size) // 2 - 80, -25)
        write('Grub\n \nKnight', align = 'right', font = big_font)    
        # Right side
        goto((num_columns * cell_size) // 2 + 80, -25)
        write('Myla\n \nHornet', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "play_game" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_game" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the "random_game" function.
#
# Each of the data sets is a list of instructions, each specifying
# in which column to drop a particular type of game token.  The
# general form of each instruction is
#
#     [column, token_type]
#
# where the columns range from 'a' to 'g' and the token types
# range from 1 to 4.
#
# Note that the fixed patterns below all assume the board has its
# default dimensions of 7x6 cells.
#

# The following data sets each draw just one token type once
fixed_game_a0 = [['a', 1]]
fixed_game_a1 = [['b', 2]]
fixed_game_a2 = [['c', 3]]
fixed_game_a3 = [['d', 4]]

# The following data sets each draw just one type
# of token multiple times
fixed_game_a4 = [['c', 1], ['f', 1], ['g', 1], ['c', 1]] 
fixed_game_a5 = [['d', 2], ['d', 2], ['a', 2], ['c', 2]] 
fixed_game_a6 = [['c', 3], ['f', 3], ['g', 3], ['c', 3]] 
fixed_game_a7 = [['f', 4], ['f', 4], ['c', 4], ['c', 4]]

# The following small data sets each draw all four kinds
# of token
fixed_game_a8 = [['e', 3], ['e', 4], ['f', 3], ['e', 1],
                 ['c', 2], ['g', 4]]
fixed_game_a9 = [['g', 3], ['d', 4], ['b', 3], ['e', 1],
                 ['f', 2], ['g', 4], ['c', 2], ['g', 4]]
fixed_game_a10 = [['f', 3], ['d', 1], ['c', 3], ['c', 4],
                  ['e', 2], ['b', 1], ['b', 3]]
fixed_game_a11 = [['e', 3], ['c', 3], ['d', 3], ['c', 2],
                  ['c', 3], ['d', 4], ['a', 4], ['f', 1]]
fixed_game_a12 = [['f', 1], ['b', 4], ['f', 1], ['f', 4],
                  ['e', 2], ['a', 3], ['c', 3], ['b', 2],
                  ['a', 2]]
fixed_game_a13 = [['b', 3], ['f', 4], ['d', 4], ['b', 1],
                  ['b', 4], ['f', 4], ['b', 2], ['c', 4],
                  ['d', 3], ['a', 1], ['g', 3]]
fixed_game_a14 = [['c', 1], ['c', 4], ['g', 2], ['d', 4],
                  ['d', 1], ['f', 3], ['f', 4], ['f', 1],
                  ['g', 2], ['c', 2]]
fixed_game_a15 = [['d', 3], ['d', 4], ['a', 1], ['c', 2],
                 ['g', 3], ['d', 3], ['g', 1], ['a', 2],
                 ['a', 2], ['f', 4], ['a', 3], ['c', 2]]

# The following large data sets are each a typical game
# as generated by the "play_game" function.  (They are
# divided into five groups whose significance will be
# revealed in Part B of the assignment.)
fixed_game_b0_0 = [['d', 4], ['e', 1], ['f', 1], ['d', 1],
                   ['e', 2], ['c', 3], ['a', 2], ['e', 4],
                   ['g', 1], ['d', 4], ['a', 2], ['f', 2]]
fixed_game_b0_1 = [['f', 3], ['a', 2], ['d', 2], ['f', 4],
                   ['b', 2], ['a', 2], ['f', 3], ['f', 3],
                   ['e', 1], ['b', 2], ['e', 1], ['c', 1],
                   ['a', 3], ['d', 3], ['f', 1], ['f', 4],
                   ['b', 4], ['b', 1], ['c', 4], ['d', 1],
                   ['a', 3], ['e', 1], ['b', 2], ['c', 3],
                   ['d', 3], ['c', 2], ['c', 1], ['a', 2],
                   ['d', 4], ['b', 4], ['g', 2]]
fixed_game_b0_2 = [['d', 3], ['d', 4], ['a', 4], ['g', 3],
                   ['d', 2], ['g', 2], ['f', 1], ['b', 2],
                   ['a', 1], ['a', 3], ['a', 4], ['c', 3],
                   ['f', 3], ['b', 2], ['c', 3], ['a', 4],
                   ['g', 1]]

fixed_game_b1_0 = [['e', 3], ['a', 4], ['c', 2], ['f', 1],
                   ['a', 1], ['c', 4], ['g', 3], ['d', 1],
                   ['f', 3], ['d', 1], ['f', 1], ['g', 1],
                   ['e', 3], ['f', 3], ['f', 3], ['e', 4],
                   ['b', 2], ['a', 2], ['g', 1], ['d', 1],
                   ['a', 1], ['a', 1]]
fixed_game_b1_1 = [['f', 3], ['g', 1], ['g', 2], ['b', 1],
                   ['c', 2], ['c', 2], ['f', 3], ['g', 3],
                   ['b', 4], ['g', 4], ['d', 4], ['b', 1],
                   ['e', 3], ['e', 3], ['a', 2], ['c', 1],
                   ['f', 4], ['f', 3], ['e', 3], ['a', 2],
                   ['f', 4], ['g', 1], ['f', 4], ['a', 1]]
fixed_game_b1_2 = [['d', 2], ['f', 1], ['f', 1], ['c', 1],
                   ['c', 4], ['c', 4], ['d', 1], ['d', 4],
                   ['b', 2], ['d', 4], ['b', 1], ['d', 3],
                   ['d', 1], ['a', 1], ['f', 2], ['c', 2],
                   ['c', 4], ['c', 1], ['g', 1], ['g', 1],
                   ['g', 4], ['g', 2], ['a', 1], ['g', 1],
                   ['f', 2], ['e', 4], ['b', 1], ['e', 3],
                   ['b', 4], ['a', 4], ['b', 1], ['a', 4],
                   ['f', 2], ['g', 2], ['a', 1], ['f', 4],
                   ['e', 1], ['b', 4], ['a', 4], ['e', 2],
                   ['e', 3], ['e', 1]]

fixed_game_b2_0 = [['g', 2], ['d', 2], ['f', 2], ['f', 2],
                   ['b', 2], ['e', 1], ['d', 1], ['d', 3],
                   ['e', 1], ['e', 1], ['b', 1], ['b', 1],
                   ['d', 3], ['f', 3], ['d', 3]]
fixed_game_b2_1 = [['c', 2], ['g', 3], ['e', 4], ['g', 2],
                   ['a', 2], ['f', 2], ['f', 2], ['c', 1],
                   ['d', 2], ['b', 3], ['f', 2], ['d', 4],
                   ['b', 4], ['e', 2], ['g', 3], ['b', 4],
                   ['a', 1], ['g', 3], ['f', 1], ['e', 4],
                   ['d', 3], ['a', 1], ['a', 1], ['d', 2],
                   ['g', 3], ['d', 2], ['c', 4], ['f', 2],
                   ['g', 1], ['e', 4], ['f', 3], ['e', 3],
                   ['e', 3], ['b', 1], ['d', 2], ['c', 1],
                   ['c', 3]]
fixed_game_b2_2 = [['e', 2], ['b', 2], ['e', 2], ['g', 2],
                   ['f', 3], ['e', 3], ['e', 2], ['g', 2],
                   ['d', 2], ['e', 2], ['a', 1], ['c', 2],
                   ['e', 2], ['a', 3], ['f', 1], ['a', 3],
                   ['d', 2], ['g', 3], ['b', 4], ['b', 2],
                   ['f', 2], ['g', 4], ['d', 3], ['f', 1],
                   ['d', 3], ['a', 1], ['a', 4], ['g', 1],
                   ['f', 3], ['b', 3], ['c', 4], ['a', 3],
                   ['g', 2], ['c', 1], ['f', 3], ['b', 2],
                   ['b', 4], ['c', 3], ['d', 4], ['c', 4],
                   ['d', 1], ['c', 1]]

fixed_game_b3_0 = [['b', 2], ['d', 4], ['g', 2], ['e', 3],
                   ['d', 3], ['f', 4], ['g', 3], ['a', 3],
                   ['g', 2], ['d', 4], ['g', 4], ['f', 4],
                   ['a', 4], ['a', 4], ['f', 2], ['b', 1]]
fixed_game_b3_1 = [['d', 2], ['b', 2], ['e', 4], ['e', 3],
                   ['d', 3], ['c', 2], ['e', 3], ['b', 4],
                   ['b', 4], ['d', 4], ['f', 1], ['c', 2],
                   ['a', 1], ['e', 3], ['b', 4], ['f', 3],
                   ['c', 3], ['b', 3], ['c', 2], ['b', 2],
                   ['d', 3], ['e', 4], ['f', 2], ['g', 3],
                   ['g', 4], ['e', 2], ['c', 1], ['d', 3],
                   ['d', 1], ['f', 3], ['g', 3], ['f', 3],
                   ['c', 3], ['g', 4], ['g', 3], ['g', 3]]
fixed_game_b3_2 = [['a', 2], ['c', 1], ['f', 2], ['d', 2],
                   ['a', 3], ['c', 2], ['b', 3], ['e', 3],
                   ['e', 3], ['f', 4], ['a', 1], ['a', 2],
                   ['b', 1], ['c', 3], ['a', 2], ['c', 2],
                   ['g', 3], ['g', 3], ['d', 3], ['b', 2],
                   ['c', 4], ['g', 3], ['f', 3], ['a', 3],
                   ['f', 2], ['f', 1], ['d', 4], ['d', 4],
                   ['g', 2], ['e', 3], ['e', 4], ['f', 3],
                   ['d', 3], ['e', 4], ['g', 4], ['c', 3],
                   ['d', 1], ['e', 2], ['b', 2], ['b', 1],
                   ['g', 1]]

fixed_game_b4_0 = [['g', 3], ['f', 3], ['e', 4], ['a', 4],
                   ['a', 4], ['c', 4], ['e', 3], ['e', 4],
                   ['a', 4], ['a', 2], ['a', 2], ['c', 4],
                   ['f', 4], ['d', 4], ['c', 4], ['f', 3],
                   ['e', 1], ['b', 2], ['c', 2], ['a', 3],
                   ['g', 4], ['d', 3], ['f', 1], ['f', 2],
                   ['e', 2], ['d', 1], ['c', 4]]
fixed_game_b4_1 = [['a', 3], ['d', 4], ['g', 4], ['b', 3],
                   ['e', 1], ['b', 4], ['e', 3], ['f', 1],
                   ['f', 4], ['b', 4], ['d', 2], ['e', 4],
                   ['g', 4], ['d', 2], ['c', 3], ['b', 2],
                   ['f', 4], ['d', 2], ['b', 2], ['e', 4],
                   ['c', 3], ['d', 2], ['a', 1], ['e', 1],
                   ['d', 2], ['g', 1], ['g', 3]]
fixed_game_b4_2 = [['c', 1], ['c', 4], ['d', 1], ['c', 2],
                   ['d', 3], ['d', 4], ['g', 3], ['e', 1],
                   ['g', 4], ['c', 3], ['f', 1], ['b', 4],
                   ['a', 3], ['c', 4], ['e', 2], ['e', 3],
                   ['b', 3], ['d', 1], ['c', 3], ['f', 4],
                   ['e', 1], ['g', 4], ['b', 4], ['g', 3],
                   ['b', 4], ['b', 3], ['b', 3], ['g', 3],
                   ['e', 3], ['f', 1], ['e', 1], ['a', 1],
                   ['a', 4], ['a', 1], ['f', 4], ['f', 2],
                   ['f', 3], ['d', 1], ['d', 3], ['a', 3],
                   ['a', 1], ['g', 2]]

# If you want to create your own test data sets put them here,
# otherwise call function random_game to obtain data sets.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.

# The following function creates a random data set describing a
# game to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "play_game"
# function during marking.  For convenience during code development
# and marking this function also prints each move in the game to the
# shell window.  NB: Your code should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# To maximise the amount of "randomness" the function makes no attempt
# to give each of the four "players" the same number of turns.  (We
# assume some other random mechanism, such as rolling a die, determines
# who gets to drop a token into the board at each turn.)  However the
# function has been designed so that it will never attempt to overfill
# a column of the board.  Also, the function will not necessarily
# generate enough moves to fill every cell in the board.
#
def random_game():
    # Welcoming message
    print('Welcome to the game!')
    print('Here are the randomly-generated moves:')
    # Initialise the list of moves
    game = []
    # Keep track of free spaces
    vacant = [["I'm free!"] * num_rows] * num_columns
    # Decide how many tokens to insert
    num_tokens = randint(0, num_rows * num_columns * 1.5)
    # Drop random tokens into the board, provided they won't
    # overfill a column
    for move in range(num_tokens):
        # Choose a random column and token type
        column_num = randint(0, num_columns - 1)
        column = chr(column_num + ord('a'))
        token = randint(1, 4)
        # Add the move, provided it won't overfill the board
        if vacant[column_num] != []:
            # Display the move
            print([column, token])
            # Remember it
            game.append([column, token])
            vacant[column_num] = vacant[column_num][1:]
    # Print a final message and return the completed game
    print('Game over!')
    if len(game) == 0:
        print('Zero moves were generated')
    elif len(game) == 1:
        print('Only one move was generated')
    else:
        print('There were', len(game), 'moves generated')
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "play_game" function.
#

# Draw tokens on the board as per the provided data set

#start drawing from the bottom left of each grid square
def goto_home():
    goto(-350, -300)

#grid array
slot_array = [0,0,0,0,0,0,0]
winner = [0,0,0,0,0,0,0]
    

#takes a letter from a to g and returns an int (a = 0, b = 1 ...)
def locate_slot_number(a_to_g):
    a_to_g = a_to_g.lower()
    #I originally had 97 here just know that ord("a") == int(97)
    slot_no = ord(a_to_g) - ord("a")
    return slot_no

#takes a number from 1 to 4 and draws the token
def draw_token(token_number):
    if token_number == 1:
        token_1()
    if token_number == 2:
        token_2()
    if token_number == 3:
        token_3()
    if token_number == 4:
        token_4()

# moves the turtle to the right until it reaches the correct column
# and moves up if theres already a token in the column
def find_slot(slot_number):
    goto_home()
    setheading(0)
    forward(slot_number * 100)
    setheading(90)
    forward(100 * slot_array[slot_number])
    slot_array[slot_number] += 1

def determine_winner(column_number, token_type):
    winner[column_number] = token_type

    #for loop to detect winner
    number_of_top_tokens = [0,0,0,0]
    for win in range(7):
        if (winner[win] == 1):
            number_of_top_tokens[0] += 1
        if (winner[win] == 2):
            number_of_top_tokens[1] += 1
        if (winner[win] == 3):
            number_of_top_tokens[2] += 1
        if (winner[win] == 4):
            number_of_top_tokens[3] += 1

        if number_of_top_tokens[0] == 4:
            return 1
        if number_of_top_tokens[1] == 4:
            return 2
        if number_of_top_tokens[2] == 4:
            return 3
        if number_of_top_tokens[3] == 4:
            return 4
    
        
            
    
        
    
    
 

def background_color(background):
    #goto bottom left of grid square
    fillcolor(background)
    begin_fill()
    setheading(0)
    for square in range(4):
        forward(100)
        left(90)
    end_fill()

def myla():
##    setheading(0)
##    up()
##    forward(-250/5)
##    setheading(270)
##    forward(250/5)
##    down()
    setheading(0)
    fillcolor("plum")
    begin_fill()
    for loop in range(4):
        forward(500/5)
        left(90)
    end_fill()
    color("grey")
    for loop in range(4):
        forward(500/5)
        left(90)
    color("black")
    up()
    forward(250/5)
    setheading(90)
    
    forward(80/5)
    setheading(0)

    fillcolor("steel blue")
    down()
    circle(150/5, 60)
    setheading(-270)
    circle(300/5, 46)

    begin_fill()

    circle(300/5, -46)


    setheading(60)
    circle(150/5, -60)
    down()

    setheading(0)
    circle(150/5, -60)

    setheading(270)
    circle(300/5, -45)
    setheading(0)
    forward(40/5)
    forward(-40/5)
    end_fill()

    up()
    setheading(90)
    forward(20/5)
    down()




    fillcolor("light cyan")
    begin_fill()
    setheading(270)
    circle(40/5)
    end_fill()

    up()
    setheading(90)
    forward(4/5)
    setheading(0)
    forward(15/5)
    down()
    color("White")
    fillcolor("White")
    begin_fill()
    setheading(180)
    circle(25/5, -90)
    setheading(270)
    circle(25/5, -90)

    setheading(135)
    circle(20/5, 85)
    setheading(135)
    circle(20/5, 85)
    end_fill()

    up()
    setheading(45)
    forward(20/5)
    setheading(0)
    forward(15/5)
    dot(10/5)
    setheading(0)
    forward(15/5)
    setheading(270)
    forward(40/5)
    dot(10/5)
    setheading(180)
    forward(30/5)
    dot(10/5)

    setheading(0)
    forward(15/5)
    setheading(270)
    forward(20/5)
    down()
    color("Black")
    forward(25/5)
    up()
    forward(30/5)

    setheading(0)
    forward(98/5)
    down()

    fillcolor("white")
    begin_fill()
    setheading(145)
    circle(175/5, 65)
    setheading(28)
    forward(20/5)
    setheading(267)
    circle(75/5, 180)


    end_fill()
    width(4/5)
    setheading(180)
    up()
    forward(25/5)
    setheading(270)
    forward(10/5)
    down()
    setheading(90)
    circle(17/5, -180)
    setheading(180)
    up()
    forward(31/5)
    down()
    setheading(90)
    circle(17/5, -180)
    up()
    setheading(180)
    forward(26/5)
    down()
    setheading(90)
    forward(15/5)
    width(3/5)
    fillcolor("light blue")
    begin_fill()
    up()
    setheading(267)
    circle(75/5, 180)
    down()
    setheading(280)
    forward(100/5)
    setheading(35)
    circle(160/5, -72)
    setheading(79)
    forward(105/5)
    end_fill()

    setheading(259)
    forward(105/5)
    begin_fill()
    setheading(260)
    circle(150/5, 25)
    setheading(315)
    circle(130/5, 93)
    setheading(81)
    circle(150/5, 22)
    end_fill()
    setheading(35)
    circle(160/5, -72)
    up()
    setheading(260)
    circle(150/5, 25)
    down()
    begin_fill()
    setheading(280)
    forward(30/5)
    setheading(325)
    up()
    circle(150/5, 72)
    down()
    setheading(80)
    forward(30/5)

    setheading(35)
    circle(160/5, -72)

    end_fill()
    #pickaxe
    fillcolor("white")
    begin_fill()

    setheading(180)
    forward(20/5)
    setheading(0)
    circle(6/5, -180)
    setheading(0)
    forward(200/5)
    setheading(0)
    circle(20/5, 150)
    setheading(180)
    circle(55/5, -170)
    setheading(30)
    circle(33/5, 130)
    setheading(180)
    forward(200/5)

    end_fill()
    up()
    setheading(90)
    forward(60/5)
    setheading(0)
    forward(4/5)
    down()
    setheading(290)
    width(7/4)
    forward(65/5)
    up()
    setheading(0)
    forward(140/5)
    setheading(70)
    down()
    forward(62/5)
    up()
    setheading(270)
    forward(110/5)
    setheading(180)
    forward(30/5)
    setheading(265)
    down()
    width(9/6)
    forward(40/5)
    up()
    setheading(180)
    forward(110/5)
    down()
    setheading(95)
    forward(40/5)

    penup()
    color("Black")
    width(1)

def grub():
    color("grey")
##  fillcolor("plum")
    fillcolor("white")
    #0,0
    width(1)
    pendown()
    setheading(0)
    begin_fill()
    for lopo in range(4):
        forward(100)
        left(90)
    end_fill()
    color("Black")
    fillcolor("medium sea green")
##    penup()
##    forward(-250/5)
##    setheading(270)
##    forward(250/5)

    ##speed("normal")
    up()
    setheading(0)
    forward(60)
    setheading(90)
    forward(50)
    down()
    setheading(30)
    circle(80/5, 190)


    begin_fill()

    setheading(40 + 180)
    circle(80/5, -200)
    setheading(15)
    circle(80/5, 10)

    setheading(120)
    circle(45/5, -90)
    setheading(20)
    forward(10/5)
    setheading(130)
    circle(30/5, -90)
    setheading(45)
    forward(10/5)
    setheading(225)
    circle(15/5, -180)
    setheading(250)
    circle(20/5, -180)
    speed("normal")


    setheading(60)
    circle(80/5, -65)
    up()
    setheading(90)
    forward(8/5)
    down()
    setheading(70)
    circle(50/5, -25)

    ##dot(10, "red")

    setheading(340)
    circle(60/5, -65)
    setheading(105)
    forward(20/5)

    setheading(10)
    up()

    forward(20/5)
    setheading(270)
    forward(5/5)

    down()
    setheading(10)
    circle(50/5, -50)

    setheading(250)
    circle(50/5, -30)

    setheading(290)
    circle(80/5, -30)
    up()
    setheading(0)
    forward(20/5)
    setheading(270)
    forward(5/5)
    setheading(0)
    down()

    circle(50/5, -40)
    setheading(240)
    circle(50/5, -25)
    setheading(90)
    circle(20/5, 90)
    ##dot(10, "red")
    setheading(0)
    circle(20/5, 90)
    setheading(60)
    circle(50/5, 40)



    setheading(90)
    forward(10/5)
    setheading(90)
    circle(30/5, 90)
    setheading(180)
    forward(10/5)
    setheading(48)
    forward(40/5)

    end_fill()
    up()
    setheading(315)
    forward(100/5)
    setheading(90)
    forward(10/5)
    dot(50/5)

    setheading(180)
    forward(83/5)
    setheading(270)
    forward(62/5)
    setheading(0)
    down()

    fillcolor("linen")
    begin_fill()

    setheading(0)
    circle(20/5, 90)
    setheading(60)
    circle(50/5, 40)
    setheading(90)
    forward(10/5)
    setheading(90)
    circle(30/5, 90)
    setheading(180)
    forward(10/5)


    setheading(180)
    circle(47/5, 180)
    setheading(0)
    forward(13/5)

    end_fill()
    setheading(180)
    forward(10/5)
    setheading(315)
    circle(75/5, -55)
    setheading(230)
    circle(40/5, 130)

    fillcolor("pale green")
    begin_fill()

    setheading(180)
    forward(20/5)
    setheading(250)
    forward(15/5)
    setheading(160)
    forward(30/5)
    setheading(240)
    circle(25/5, 110)
    setheading(250)
    forward(8/5)

    setheading(250)
    circle(90/5, 40)
    setheading(215)
    circle(50/5, 40)
    setheading(315)
    circle(30/5, 53)

    setheading(305)
    circle(70/5, 77)
    up()
    setheading(320)
    forward(20/5)
    setheading(0)
    forward(5/5)
    # wow
    setheading(340)
    circle(60/5, -65)
    setheading(105)
    forward(20/5)

    setheading(10)
    up()

    forward(20/5)
    setheading(270)
    forward(6/5)

    down()
    setheading(10)
    circle(50/5, -50)

    setheading(250)
    circle(50/5, -30)

    setheading(290)
    circle(80/5, -30)
    up()
    setheading(0)
    forward(20/5)
    setheading(270)
    forward(5/5)
    setheading(0)
    down()

    circle(50/5, -40)
    setheading(240)
    circle(50/5, -25)
    setheading(90)
    circle(20/5, 90)


    end_fill()

    up()
    setheading(270)
    forward(173/5)
    down()

    begin_fill()
    setheading(215)
    forward(15/5)
    setheading(115)
    forward(20/5)
    end_fill()
    width(1)
    up()
    
def hollow_knight():
    #draw background box
    fillcolor("steel blue")
    begin_fill()
    setheading(0)
    for square in range(4):
        forward(100)
        left(90)
    end_fill()
    pendown()
    color("grey")
    for square in range(4):
        forward(100)
        left(90)
    penup()
    color("Black")
    forward(50)
    setheading(90)
    forward(50)

        
    knight_home = pos()



    setheading(180)
    forward(70/5)

    pendown()
    setheading(270)
    penup()
    forward(80/5)
    pendown()

    begin_fill()

    penup()
    setheading(0)
    forward(27/5)
    pendown()
    forward(73/5)

    circle(100/5, 90)
    setheading(90)
    forward(75/5)

    #horn top right
    setheading(30)
    circle(80/5, 160)

    width(0.7)

    setheading(160)
    circle(100/5, -20)

    setheading(180)
    circle(80/5, 14)

    setheading(175)
    circle(55/5 , -145)

    #horn top right done
    width(1)
    setheading(180)
    forward(220/5)
    penup()
    forward(20/5)
    setheading(270)
    forward(25/5)
    pendown()

    #horn top left

    setheading(-30)
    circle(80/5, -160)


    setheading(-160)
    circle(100/5, 20)

    setheading(-180)
    circle(80/5, -14)

    setheading(-175)
    circle(55/5 , 146)
    #horn top left done

    width(1)
    penup()
    setheading(180)
    forward(20/5)
    setheading(270)
    forward(25/5)
    pendown()

    setheading(270)
    forward(78/5)
    setheading(270)
    circle(100/5, 81)

    fillcolor("white smoke")
    end_fill()

    width(1)

    #legs
    penup()
    goto(knight_home)
    fillcolor("Black")
    setheading(0)
    forward(8)
    setheading(270)
    forward(50)
    begin_fill()
    setheading(180)
    forward(20)
    setheading(90)
    forward(30)
    setheading(0)
    forward(20)
    setheading(270)
    forward(30)
    end_fill()

    setheading(180)
    forward(8)

    fillcolor("steel blue")

    setheading(180)
    forward(5)
    begin_fill()
    setheading(90)
    forward(3)
    setheading(270)
    circle(3, -180)
    setheading(270)
    forward(3)
    setheading(0)
    forward(5)

    end_fill()




    goto(knight_home)
    setheading(0)
    forward(70/5)
    dot(75/5)
    goto(knight_home)
    setheading(180)
    forward(70/5)
    dot(75/5)
    goto(knight_home)
    pendown()


    penup()
    setheading(90)
    forward(127/5.2)
    setheading(270)
    forward(26/5)

    pendown()

    fillcolor("white")
    begin_fill()

    color("white")
    setheading(0)
    circle(280/5, 20)
    circle(280/5, -40)


    setheading(0)
    forward(195/5)
    setheading(225)
    forward(5/5)
    end_fill()

    penup()
    goto(knight_home)
    setheading(270)
    forward(80/5)
    setheading(0)
    forward(-50/5)
    # -55.00,-80.00
    pendown()
    color("black")
    fillcolor("slate grey")

    begin_fill()
    setheading(230)
    circle(200/5, 50)


    speed("normal")
    setheading(28)
    circle(270/5, 25)

    setheading(300)
    circle(50, 25)

    setheading(70)
    circle(40, 50)
    setheading(180)
    forward(22)

    setheading(300)
    forward(20)
    setheading(300 + 180)
    forward(20)


    end_fill()

    fillcolor("gray")
    begin_fill()
    setheading(225)
    forward(15/5)
    setheading(135)
    forward(50/5)
    setheading(225)
    forward(20/5)
    setheading(135)
    forward(-50/5)
    setheading(225)
    forward(25/5)
    setheading(315)
    forward(20/5)


    end_fill()



    
    penup()
    color("Black")

def hornet():
    color("grey")
    width(1)
    setheading(0)
    up()
##    forward(-250/5)
##    setheading(270)
##    forward(250/5)
    down()
    setheading(0)
    fillcolor("light green")
    begin_fill()
    for loop in range(4):
        forward(500/5)
        left(90)
    end_fill()
    for loop in range(4):
        forward(500/5)
        left(90)


    color("black")
    up()
    setheading(0)
    forward(400/5)
    setheading(90)
    forward(250/5)
    down()
    fillcolor("grey")
    begin_fill()
    setheading(210)
    forward(300/5)
    setheading(28)
    forward(300/5)
    end_fill()
    up()
    setheading(180)
    forward(10/5)
    down()
    begin_fill()
    setheading(300)
    circle(10/5)
    end_fill()
    up()
    setheading(35)
    forward(10/5)
    dot(8/5, "black")

    setheading(270)
    forward(253/5)
    setheading(180)
    forward(403/5)

    down()

    up()
    setheading(0)
    forward(250/5)
    setheading(90)
    up()
    forward(250/5)
    setheading(0)
    width(3/5)
    down()
    fillcolor("firebrick")
    begin_fill()

    setheading(135)
    forward(20/5)
    setheading(0)
    forward(50/5)
    setheading(225)
    forward(20/5)
    end_fill()
    up()
    setheading(45)
    forward(20/5)
    setheading(180)
    forward(45/5)
    down()
    setheading(315)
    fillcolor("white")
    begin_fill()
    circle(30/5, -45)

    setheading(270)
    circle(150/5, -70)

    setheading(225)
    circle(200/5, 30)

    setheading(270)
    circle(6/5, 150)
    setheading(55)
    forward(110/5)

    setheading(91)
    circle(200/5, -52)
    end_fill()
    up()
    setheading(90)
    forward(15/5)
    setheading(180)
    forward(15/5)
    down()



    fillcolor("black")
    begin_fill()

    setheading(235)
    circle(6/5, 180)


    setheading(55)
    forward(10/5)


    setheading(45)
    circle(3/5, 140)

    setheading(188)
    circle(30/5, 30)

    end_fill()

    #second eye
    up()
    setheading(180)
    forward(15/5)
    setheading(270)
    forward(5/5)
    down()

    begin_fill()
    setheading(120)
    circle(3/5, -180)
    setheading(120)
    forward(10/5)
    setheading(300)
    circle(3/5, -180)
    setheading(300)
    forward(10/5)
    end_fill()
    up()
    setheading(270)
    forward(25/5)
    down()

    fillcolor("firebrick")
    begin_fill()
    setheading(240)
    forward(80/5)
    setheading(315)
    circle(70/5, 90)
    setheading(117)
    forward(80/5)
    end_fill()

    up()
    setheading(270)
    forward(87/5)
    down()
    setheading(95)
    forward(80/5)
    up()
    setheading(180)
    forward(10/5)
    setheading(260)
    down()
    forward(80/5)
    setheading(270)
    up()
    forward(5/5)
    down()
    fillcolor("black")
    begin_fill()
    setheading(270)
    forward(50/5)
    circle(2/5, 180)
    setheading(90)
    forward(49/5)
    end_fill()

    setheading(0)
    up()
    forward(15/5)
    down()
    begin_fill()
    setheading(280)
    forward(50/5)
    circle(2/5, 180)
    setheading(100)
    forward(49/5)
    end_fill()

    color("black")
    pendown()
    up()

    
    

#replace background_color with each different drawing
def token_1():
    grub()  
def token_2():
    hollow_knight() 
def token_3():
    myla()
def token_4():
    hornet()


def example_tokens():
    up()
    home()
    setheading(180)
    forward(535)
    setheading(90)
    forward(100)
    down()
    token_1()
    up()
    home()
    setheading(180)
    forward(540)
    setheading(270)
    forward(140)
    down()
    token_2()
    up()
    home()
    setheading(0)
    forward(420)
    setheading(90)
    forward(100)
    down()
    token_3()
    up()
    home()
    setheading(0)
    forward(420)
    setheading(270)
    forward(140)
    down()
    token_4()
    


    up()

def sad_face():
    up()
    home()
    setheading(180)
    forward(30)
    width(4)
    setheading(270)
    color("black")
    down()
    circle(30)
    up()
    setheading(0)
    forward(20)
    dot(10)
    forward(20)
    dot(10)
    setheading(270)
    forward(40)
    setheading(90)
    forward(20)
    down()
    circle(10, 180)
    up()

def celebration(winner_number):
    home()
    setheading(180)
    forward(100)
    setheading(270)
    forward(100)
    setheading(0)
    fillcolor("yellow")
    begin_fill()
    for loop in range(4):
        forward(200)
        left(90)
    end_fill()
    
    color("black")
    for loop in range(4):
        forward(200)
        left(90)
    
    home()
    setheading(270)
    forward(50)
    setheading(180)
    forward(50)
    if (winner_number == 0):
        sad_face()
    else:
        draw_token(winner_number)
    
    setheading(270)
    forward(50)
    setheading(0)
    forward(30)
    if (winner_number == 1):
        write('Token 1: grub Wins!', move=False, align="center", font=("Arial", 12, "normal"))
    if (winner_number == 2):
        write('Token 2: Knight Wins!', move=False, align="center", font=("Arial", 12, "normal"))
    if (winner_number == 3):
        write('Token 3: Myla Wins!', move=False, align="center", font=("Arial", 12, "normal"))
    if (winner_number == 4):
        setheading(180)
        forward(20)
        write('Token 4: Hornet Wins!', move=False, align="center", font=("Arial", 12, "normal"))

    if (winner_number == 0):
        setheading(180)
        up()
        forward(20)
        write('Its a draw! Nobody wins!', move=False, align="center", font=("Arial", 12, "normal"))
        

def play_game(game_info):
    thingy = None
    example_tokens()
    game_length = len(game_info)
    for loop in range(game_length):
        goto_home()
        #move turtle to the right
        #needs number from 0-6
        find_slot(locate_slot_number(game_info[loop][0]))

        #draws the token (1 2 3 or 4)
        draw_token(game_info[loop - 1][1])

        #determine a winner if any
        thingy = determine_winner(locate_slot_number(game_info[loop][0]), game_info[loop - 1][1])
        if (thingy != None):
            celebration(thingy)
            return
    if (thingy == None):
        print("no winner")
        celebration(0)

    

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to label the axes and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** theme and its tokens
title('Hollow Knight not_connect_4 featuring the Grub, the Knight, Myla the miner bug and Hornet :D')

### Call the student's function to play the game
### ***** While developing your program you can call the "play_game"
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument.  Your "play_game" function must work for any data
### ***** set that can be returned by the "random_game" function.
#play_game(fixed_game_a0) # <-- use this for code development only
play_game(random_game()) # <-- this will be used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
