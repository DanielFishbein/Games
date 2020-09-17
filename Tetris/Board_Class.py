import numpy as np
import random
import sys

#Auther: Daniel Fishbein
#Last edited: 8/23/2020

# This file contains the class board and all its values and
# functions.
class board:
    def __init__(self, h, w):
        # Note: The dead space is not what is seen in the game but rather what
        # is being used in the backround of the hidden matrix.  There must be 
        # this many 0's else python will round the random.random() to the specified
        # number of 0's.
        self.height = h
        self.width = w    
        self.dead_space = "0.0000000000000000"
    
    
    def __del__(self):
        return
        
                            
    
    # Returns the height of the board
    def get_height(self):
        return self.height

    # Returns the width of the board
    def get_width(self):
        return self.width
    
    # Returns the dead space of the hidden board
    def get_dead_space(self):
        return self.dead_space

    # Randomly pick the next piece name
    def next_piece(self):
        next_piece = random.random()
        if next_piece < (1/7):
            return "Long"
        elif next_piece < (2/7):
            return "L-left"
        elif next_piece < (3/7):
            return "L-right"
        elif next_piece < (4/7):
            return "Square"
        elif next_piece < (5/7):
            return "Z-left"
        elif next_piece < (6/7):
            return "Z-right"
        else:
            return "T"
       
    # Function that moves a piece in a specified direction if able 
    # and returns whether or not it could, the shapes new cordinates,
    # and the shape's new center.
    def move_piece(self, center, identity, shape_cordinates, direction, matrix):   

        if direction == "s":
            # Creates a copy of the given board,
            # then parces out the cordinates into height and width
            # along with defing the new height and width that will
            # tested later.  Then it adjusts the center acordingly 
            # depending on the given direction 
            pre_matrix = np.copy(matrix)
            shape_height_cord, shape_width_cord = [shape_cordinates[0],shape_cordinates[1]], [shape_cordinates[2],shape_cordinates[3]]
            new_width_0, new_width_1 = shape_width_cord[0], shape_width_cord[1]
            new_height_0, new_height_1 = shape_height_cord[0]+1, shape_height_cord[1]+1
            new_center = [center[0]+1, center[1]]

            # Searches through the defined height and width of the copied
            # board to find the cordinates of the given piece as well as 
            # creating a list of adjusted cordinates for were the piece will
            # end up.
            new_list_of_cordinates = []
            list_of_cordinates = []
            for y in range(shape_height_cord[0],shape_height_cord[1]):
                for x in range(shape_width_cord[0],shape_width_cord[1]):
                    if pre_matrix[y][x] == str(identity):
                        list_of_cordinates.append([y,x])
                        pre_matrix[y][x] = self.dead_space
                        new_list_of_cordinates.append([y+1,x])

        
        elif direction == "d":
            # Creates a copy of the given board,
            # then parces out the cordinates into height and width
            # along with defing the new height and width that will
            # tested later.  Then it adjusts the center acordingly 
            # depending on the given direction
            pre_matrix = np.copy(matrix)
            shape_height_cord, shape_width_cord = [shape_cordinates[0],shape_cordinates[1]], [shape_cordinates[2],shape_cordinates[3]]
            new_width_0, new_width_1 = shape_width_cord[0]+1, shape_width_cord[1]+1
            new_height_0, new_height_1 = shape_height_cord[0], shape_height_cord[1]
            new_center = [center[0], center[1]+1]

            # Searches through the defined height and width of the copied
            # board to find the cordinates of the given piece as well as 
            # creating a list of adjusted cordinates for were the piece will
            # end up.
            new_list_of_cordinates = []
            list_of_cordinates = []
            for y in range(shape_height_cord[0],shape_height_cord[1]):
                for x in range(shape_width_cord[0],shape_width_cord[1]):
                    if pre_matrix[y][x] == str(identity):
                        list_of_cordinates.append([y,x])
                        pre_matrix[y][x] = self.dead_space
                        new_list_of_cordinates.append([y,x+1])

        
        elif direction == "a":
            # Creates a copy of the given board,
            # then parces out the cordinates into height and width
            # along with defing the new height and width that will
            # tested later.  Then it adjusts the center acordingly 
            # depending on the given direction
            pre_matrix = np.copy(matrix)
            shape_height_cord, shape_width_cord = [shape_cordinates[0],shape_cordinates[1]], [shape_cordinates[2],shape_cordinates[3]]
            new_width_0, new_width_1 = shape_width_cord[0]-1, shape_width_cord[1]-1
            new_height_0, new_height_1 = shape_height_cord[0], shape_height_cord[1]
            new_center = [center[0], center[1]-1]

            # Searches through the defined height and width of the copied
            # board to find the cordinates of the given piece as well as 
            # creating a list of adjusted cordinates for were the piece will
            # end up.
            new_list_of_cordinates = []
            list_of_cordinates = []
            for y in range(shape_height_cord[0],shape_height_cord[1]):
                for x in range(shape_width_cord[0],shape_width_cord[1]):
                    if pre_matrix[y][x] == str(identity):
                        list_of_cordinates.append([y,x])
                        pre_matrix[y][x] = self.dead_space
                        new_list_of_cordinates.append([y,x-1])

        # If none of the specified letters were in direction than 
        # return None, the unaltered cordinates, the unaltered board,
        # and the unaltered center 
        else:
            return None, shape_cordinates, matrix, center

        # Defining the new cordnates of the piece
        new_cordinates = new_height_0, new_height_1, new_width_0, new_width_1

        # A serch through all the values of the given cordinates seaching for 
        # "dead space".  If any of the values in the specified region have anything
        # other than dead space, the test is falied  
        test = True
        for index in range(len(new_list_of_cordinates)):
            if pre_matrix[new_list_of_cordinates[index][0]][new_list_of_cordinates[index][1]] == self.dead_space:
                pass
            else:
                test = False

        # If the test is passed than the piece is added to the copied board in the 
        # new location.  The bool False along with the new cordinates, the altered matrix
        # and the new center are returned
        if test == True:
            for index in range(len(new_list_of_cordinates)):
                pre_matrix[new_list_of_cordinates[index][0]][new_list_of_cordinates[index][1]] = identity
            return False, new_cordinates, pre_matrix, new_center
        
        # If the test is failed than bool True, along with the unaltered 
        # cordinates, board, and center are returned 
        else:
            return True, shape_cordinates, matrix, center

    # A function that takes a board and checks to see if any horizontal
    # lines have been filled.  It then clears those lines and moves the 
    # existing lines above down.  This function returns the altered matrix
    # and whether or not any lines were cleared
    def clear_line(self, matrix):
        line_check  = 0
        did_score = False
        cleared_lines = 0
        # A for loop to check if the matrix is at the bottom yet
        for line in matrix:
            if line[1] == "_":

                # If at the bottom than return the matrix and the bool "did_score"
                # and the number of lines cleared
                return matrix, did_score, cleared_lines
            
            # Resetting the variable "count" to check if the given line is full 
            count = 0
            for value in line:
                if value != self.dead_space:
                    count = count + 1

                    # If the given line is full then set "did_score" to True, and
                    # reset the line with dead space and the edges. Also keeps track
                    # of the number of lines cleared
                    if count == self.width:
                        did_score = True
                        cleared_lines = cleared_lines + 1
                        for value in range(len(line)):
                            if (value == 0) or (value == self.width-1):
                                matrix[line_check][value] = "|"
                                continue
                            matrix[line_check][value] = self.dead_space

                        # A loop to work back up the board. and moving each value above down
                        for shift in range(line_check,-1,-1):
                            for shift_count in range(len(matrix[shift])):
                                if shift == 0:
                                    continue
                                matrix[shift][shift_count] = matrix[shift-1][shift_count]
            
            # A counter to see what the current line is
            line_check = line_check + 1

        # Returning the board and the bool "did_score" and the number of lines cleared.
        # This line is not be nessessary as the function will allways 
        # terminate before the end of the for loop. However, I feel it
        # is good grammer to end functions with a "return" statement.
        return matrix, did_score, cleared_lines


    # A function to check if the given stack size
    # is the size of the board or not.  This function 
    # returns True if the stack is not the size of the board
    # and false if it is the size of the board
    def check_full(self, stack_size):
        if stack_size >= self.height-1:
            return False
        return True


    # A function to measure the current stack and 
    # returns heighest point that is not dead space
    def measure_stack(self,stack):
        highest_point = 0
        step = 0
        
        # Flip the stack to count from the bottom up
        reverse_stack = stack
        reverse_stack = np.flip(reverse_stack)
        
        # If a point has something other than "dead space"
        # than the value of that point is saved.
        for number in reverse_stack:
            if number != self.dead_space:
                highest_point = step
            step = step + 1
        
        # Returns the heighest point 
        return highest_point
    

    # A function that gets a colomn callled a stack from the board
    # and returns that column called a stack
    def get_stack(self,index, matrix):
        stack =  np.array([])
        for i in range(self.height-1):
            stack = np.append(stack,matrix[i,index])
        return stack


    # A function that creates an empty board aside from edges and 
    # a bottom.  This function returns that board 
    def generate_board(self):
        new_board = []
        for i in range(self.height):
            dumb = []

            # For each value of the board the value of "dead space",
            # "|", or "_" if given depending on the height and width position
            for j in range(self.width):
                if (j == 0) or (j == self.width-1):
                    dumb.append("|")
                    continue
                if i == self.height-1:
                    dumb.append("_")
                    continue
                dumb.append(self.dead_space)
            new_board.append(dumb)

        # The board is created as a list of lists and is then converted 
        # into a multi-dimentional numpy array
        new_board = np.array(new_board)

        #Returns the created board
        return new_board


    # A function that insetes a new piece into the board at a given "center" point.
    # This function returns the board, the position of the piece, the bool True or False
    # and the center.
    def insert_piece(self, new_piece, center, matrix):
        
        # Extracting the piece's height and width and then saving values of those baced on thier
        # position to the center
        new_piece_width, new_piece_height = int(len(new_piece[0])), int(len(new_piece))
        middle_left = int(new_piece_width/2)
        middle_right = new_piece_width-middle_left
        middle = center[1]
        
        # A test to see if the given indicies are only dead space
        test = True
        test_area = matrix[center[0]:new_piece_height+center[0], middle-middle_left:middle+middle_right].flatten()
        for i in test_area: 
            if i == self.dead_space:
                pass
            else:
                test = False
        # If the test is passed than the board is filled with the specified piece 
        # at the given cordinates
        if test == True:
            matrix[center[0]:new_piece_height+center[0], middle-middle_left:middle+middle_right] = new_piece
            position = [center[0], new_piece_height+center[0], middle-middle_left, middle+middle_right]
            
            # Returns the altered matrix, the position of the piece the bool True, and the center values
            return matrix, position, True, center
        else:
            position = [center[0], new_piece_height+center[0], middle-middle_left, middle+middle_right]
            
             # Returns the unaltered matrix, the position of the piece the bool False, and the center values
            return matrix, position, False, center


    # A function that prints the board in a more readable fasion of spaces 
    # and intigers
    def print_board(self, pre_matrix):

        # Makes a copy of the given matrix and then replaces all the
        # "dead space" with empty spaces and the really long decmals into
        # readable intigers
        matrix = np.copy(pre_matrix)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                    number = matrix[y][x]
                    if (number != "|") and (number != "_"):
                        if number == self.dead_space:
                            matrix[y][x] = " "
                            continue
                        # The number of 0's that compose of "dead space"
                        # is so great that the value must be converted from 
                        # a string to a float and then an intiger
                        number = int(float(number))
                        matrix[y][x] = number
        print(matrix)
        return

    # A function that prints the "hidden" board that the computer 
    # is working with
    def print_hidden_board(self,matrix):
        print(matrix)
        return
