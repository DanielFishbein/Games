import random
import numpy as np
import os
import time
import sys
import keyboard

from Shape_Class import *
from Board_Class import *

#Auther: Daniel Fishbein
#Last edited: 8/23/2020


# The backbone function of this program 
# and the function that runs the game of 
# Tetris.
def Tetris_function(old_time):

    # Defining the board height, width
    # and initial score.
    height = 25
    width = 13
    score = 0

    # Defining the initial conditions of
    # the game.
    not_dead = True
    next_block = True

    # Change the print statement to always print on one line
    # regardless of how long it is.
    np.set_printoptions(linewidth=np.inf)

    # Creating the object: The_board and generating the matrix
    # on wich the game will be played.
    The_board = board(height,width)
    board_matrix = The_board.generate_board()

    # A loop in wich the game is played.  While this statement
    # is True the game will continue.
    while not_dead == True:
        
        # Wait the desired time.  This makes the game run at a 
        # more consistant pase.
        time.sleep(0.0001)
        
        # A time statement for when the loop passes
        other_time = time.time()

        # Check difference in the two time statements 
        check_time = other_time - old_time

        # The condidtions on wich a new piece is to be made
        if next_block == True:
            
            # Calling the function next_peice() and creating the object: "new_shape"
            next_piece = The_board.next_piece()
            new_shape = shape()

            # Depending on the value of "next_piece" a different peice will be chosen
            # created in the form of new_piece, and its identity will be aducted acordingly.
            if next_piece == "Long":
                new_piece = new_shape.Long_block()
                new_piece_identity = new_shape.get_identity()+1
            elif next_piece == "L-left":
                new_piece = new_shape.L_left_block()
                new_piece_identity = new_shape.get_identity()+2
            elif next_piece == "L-right":
                new_piece = new_shape.L_right_block()
                new_piece_identity = new_shape.get_identity()+3
            elif next_piece == "Square":
                new_piece = new_shape.Square_block()
                new_piece_identity = new_shape.get_identity()+4
            elif next_piece == "Z-left":
                new_piece = new_shape.Z_right_block()
                new_piece_identity = new_shape.get_identity()+5
            elif next_piece == "Z-right":
                new_piece = new_shape.Z_left_block()
                new_piece_identity = new_shape.get_identity()+6
            else:
                new_piece = new_shape.T_block()
                new_piece_identity = new_shape.get_identity()+7
            
            # Now that the piece has been chosen and the identity saved,
            # the object: "new_shape" is deleted to revent memory clutter
            del new_shape
            
            # Defining the center of the new piece
            shape_center = [1, int(The_board.get_width()/2)]

            # Inserting the new piece in the board
            new_board = The_board.insert_piece(new_piece, shape_center, board_matrix)
            
            # Parcing out the pieces of the return statement "insert_piece()"
            board_matrix = new_board[0]
            piece_position = new_board[1]
            landed = new_board[2]
            
            # If the new piece can not be laned than the board is deleted
            # and the program ends.
            if landed == False:
                print("Cant place new piece, you lose")
                del The_board
                sys.exit()

            # Renaming next_piece as it is now the current piece
            # and setting the condition to insert a new piece to False    
            current_piece_name = next_piece
            next_block = False
        
        # Clearing the terminal
        os.system('cls')
        
        # Printing the board in a READABLE fashion and the score.
        The_board.print_board(board_matrix)
        print()
        print("Score: ",score)

        # If you wish to see what the board actualy looks like than uncoment the line below
        #The_board.print_hidden_board(board_matrix)
        
        
        # Used try so that if user pressed other than the given key error will not be shown
        try:  
           
            # If key defined key is pressed is pressed 
            if keyboard.is_pressed('a'):  
                user_input = "a"
            elif keyboard.is_pressed('s'):  
                user_input = "s"
            elif keyboard.is_pressed('d'):
                user_input = "d"
            elif keyboard.is_pressed('w'):
                user_input = "w"

                # The square does not rotate so it is skeipped
                # if the player tries to rotate it.
                if next_piece == "Square":  
                    continue

                # Attempt to rotate the piece if possible
                try:
                    # Create a copy of the board
                    pre_matrix = np.copy(board_matrix)

                    # Parse out the height and width
                    shape_height_cord, shape_width_cord = [piece_position[0],piece_position[1]], [piece_position[2],piece_position[3]]
                    
                    # Create a new piece with the shape of the piece in question
                    pre_rot_piece = np.copy(pre_matrix[shape_height_cord[0]:shape_height_cord[1],shape_width_cord[0]:shape_width_cord[1]])
                    
                    # Rotate the new piece 
                    rot_piece = np.rot90(pre_rot_piece)

                    # Wall is used as a catch all to make sure nothing overlaps
                    wall = False

                    # Inside the defined dimentions of the copied board
                    for y in range(shape_height_cord[0],shape_height_cord[1]):
                        for x in range(shape_width_cord[0],shape_width_cord[1]):
                            
                            # If this is one of the parts of the piece, set it to
                            # "empty_space()".
                            if pre_matrix[y][x] == str(new_piece_identity):
                                pre_matrix[y][x] = The_board.get_dead_space()

                            #if the cordinates are not part of the piece and not "dead_space"
                            if pre_matrix[y][x] != The_board.get_dead_space():
                        
                                    # Wall is set to True and the inner most "try" stament is failed
                                    wall = True
                                    print("You cant do that.")
                                    print("You are either against the wall or agains another piece.")
                                    sys.exit()
                                    
                    # If there is nothing else in the piece position
                    if wall == False:
                        
                        # Insert the rotated piece in the copied matrix
                        rot_matrix = The_board.insert_piece(rot_piece, shape_center, pre_matrix)
                        
                        # Parsing out the pieces of "insert_piece()"
                        board_matrix = rot_matrix[0]
                        piece_position = rot_matrix[1]

                        # Correcting the center of the piece depending on what 
                        # the piece is. 
                        if current_piece_name == "Long":
                            shape_center = rot_matrix[3]

                        elif current_piece_name == "L-left":
                            shape_center = rot_matrix[3]
                            shape_center = [shape_center[0]+1,shape_center[1]]
                        
                        elif current_piece_name == "L-right":
                            shape_center = rot_matrix[3]
                            shape_center = [shape_center[0]+1,shape_center[1]]

                        elif current_piece_name == "Z-left":
                            shape_center = rot_matrix[3]
                            shape_center = [shape_center[0],shape_center[1]]

                        elif current_piece_name == "Z-right":
                            shape_center = rot_matrix[3]
                            shape_center = [shape_center[0],shape_center[1]]

                        else:
                            shape_center = rot_matrix[3]

                    # The old board is maintained
                    else:
                        board_matrix = board_matrix
                
                # If the piece could not be inserted pass
                except:
                    pass
            
            # If the useer does not press any buttons than
            # their input is defaled to ""
            else:
                user_input = ""
        
        # If the user presses anything other than "w", "a", "s", or, "d" print()
        except:
            print("Use -w-a-s-d- to move")
 
        # Depending on what the user inputs  the piece is moved accoringly
        check_move = The_board.move_piece(shape_center, new_piece_identity, piece_position, user_input, board_matrix)
        
        # Parsing out the pieces of "move_shape()" 
        shape_center = check_move[3]
        board_matrix = check_move[2]
        piece_position = check_move[1]

        # Check if 2 time statemnts from above are more than 
        # 2 seconds apart.
        if check_time >= 2:

            # Reset old time 
            old_time = time.time()

            # Move the piece down one
            check_fall = The_board.move_piece(shape_center, new_piece_identity, piece_position, "s", board_matrix)
            
            # Parsing out the pieces of "move_piece()"
            shape_center = check_fall[3]
            board_matrix = check_fall[2]
            piece_position = check_fall[1]
            landed = check_fall[0]

            # Check if the piece has landed 
            if landed == True:

                # Call the funtion "clear_line()" which clears any full lines 
                # and shifts everything on the board down one
                board_clear = The_board.clear_line(board_matrix)

                # Parsing out the pieces of "clear_line()"
                board_matrix = board_clear[0]

                # Updating the score if nessesary
                if board_clear[1] == True:
                    score = score + 100*board_clear[2]

                # Saying that the next block is to be called  
                next_block = True

                # Shifting though each column of the board
                highest_stack = 0
                for index in range(width):
                    if (index == 0) or (index == width-1):
                        continue

                    # Calling the function "get_stack()" which returns the given column
                    stack = The_board.get_stack(index,board_matrix)

                    # Calling the function "measure_stack()" which returns the height of the column
                    stack_height = The_board.measure_stack(stack)

                    # Record the highest stack size
                    if stack_height > highest_stack:
                        highest_stack = stack_height

                    # Call the function "check_full()" to see if the player is dead or not 
                    not_dead = The_board.check_full(highest_stack)

                    # If the player is dead than the the fallowing print statment is shown.
                    if not_dead == False:
                        print("board is full, You lose :(")
    return

if __name__ == "__main__":

    # Telling the player how to move
    print("----Use -w-a-s-d- to move ---")
    
    # Wait 2 seconds
    time.sleep(2)

    # Count down to start
    print("--------------3--------------")
    time.sleep(1)
    print("--------------2--------------")
    time.sleep(1)
    print("--------------1--------------")
    time.sleep(1)
    print("-------------GO!-------------")
    time.sleep(1)
    
    # Calling Tetris_function() 
    old_time = time.time()
    Tetris_function(old_time)

