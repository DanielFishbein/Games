import numpy as np
import random

#Auther: Daniel Fishbein
#Last edited: 8/23/2020

class shape:
    def __init__(self):
        #Note: The dead space is not what is seen in the game but rather what
        #is being used in the backround of the hidden matrix.  There must be 
        #this many 0's else python will round the random.random() to the specified
        #number of 0's.
        self.dead_space = "0.0000000000000000"
        self.identity = random.random()
    
    
    def __del__(self):
        return

    #Returns the identity of the piece
    def get_identity(self):
        return self.identity
    
    #The shape of the long block
    def Long_block(self):
        shape = np.array([[self.dead_space,self.identity+1,self.dead_space],
                          [self.dead_space,self.identity+1,self.dead_space],
                          [self.dead_space,self.identity+1,self.dead_space],
                          [self.dead_space,self.identity+1,self.dead_space]])
        return shape

    #The shape of the L left block
    def L_left_block(self):
        shape = np.array([[self.dead_space,self.identity+2,self.dead_space],
                          [self.dead_space,self.identity+2,self.dead_space],
                          [self.identity+2,self.identity+2,self.dead_space]])
        return shape

    #The shape of the L right block
    def L_right_block(self):
        shape = np.array([[self.identity+3,self.dead_space,self.dead_space],
                          [self.identity+3,self.dead_space,self.dead_space],
                          [self.identity+3,self.identity+3,self.dead_space]])
        return shape
        
    #The shape of the square block
    def Square_block(self):
        shape = np.array([[self.identity+4,self.identity+4],
                          [self.identity+4,self.identity+4]])
        return shape

    #The shape of the Z right block
    def Z_right_block(self):
        shape = np.array([[self.dead_space,self.dead_space,self.dead_space],
                          [self.dead_space,self.identity+5,self.identity+5],
                          [self.identity+5,self.identity+5,self.dead_space]])
        return shape

    #The shape of the Z left block
    def Z_left_block(self):
        shape = np.array([[self.dead_space,self.dead_space,self.dead_space],
                          [self.identity+6,self.identity+6,self.dead_space],
                          [self.dead_space,self.identity+6,self.identity+6]])
        return shape

    #The shape of the T block
    def T_block(self):
        shape = np.array([[self.dead_space,self.dead_space,self.dead_space],
                          [self.dead_space,self.identity+7,self.dead_space],
                          [self.identity+7,self.identity+7,self.identity+7]])
        return shape

