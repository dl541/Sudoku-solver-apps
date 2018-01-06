# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 05:13:43 2017

@author: user
"""
import numpy as np
import time
width = 9
length = 9
grid_length = 3
grid_width = 3

#sudoku = np.array([[None,1,3,None],[2,None,None,None],[None,None,None,3],[None,2,1,None]])
def solve(sudoku):
    sudoku = np.array(sudoku)
    def solver(sudoku):
        #print (sudoku)

        empty_space = [(i,j) for i in range(length) for j in range(width) if sudoku[i][j]==None]
        
        if empty_space==[]:
            return sudoku
        
        else:
            x_pos = empty_space[0][0] #find the first empty cell
            y_pos = empty_space[0][1]
            
            possible_num = possible_candidates(x_pos,y_pos,sudoku) #find the possible numbers in the cell
            
            if possible_num ==[]:
                return None
            else:
                for num in possible_num:
                    sudoku[x_pos][y_pos] = num #try one of the nums
                    ans = solver(sudoku)
                    if type(ans)==np.ndarray:   
                        return ans
                    
                sudoku[x_pos][y_pos] = None     #No possible ans, trace back to the last node
                return None
                
    time1 = time.time()              
    ans = solver(sudoku)
    time2 = time.time()
    return time2-time1, ans
                

    
    


def possible_candidates(x_pos,y_pos,sudoku):
    
    
    #check row candidates
    row_candidates = set(list(range(1,width+1)))
    current_row = set(sudoku[x_pos])
    row_candidates = row_candidates-current_row

    #check column candidates
    column_candidates = set(list(range(1,length+1)))
    current_column = set(sudoku.transpose()[y_pos])
    column_candidates = column_candidates-current_column
    
    #print (row_candidates)
    #print (column_candidates)

    #check grid candidates
    grid_candidates = set(list(range(1,width+1)))
    
    grid_x,grid_y = x_pos-x_pos%grid_width,y_pos-y_pos%grid_length    
    grid = sudoku[grid_x:grid_x+grid_width, grid_y:grid_y+grid_length]    
    current_grid = set(grid.flatten())
    
    grid_candidates = grid_candidates - current_grid
    
    #print (grid_candidates)

        
    
    return grid_candidates & column_candidates & row_candidates
    
    

    

        
            
        
    
                