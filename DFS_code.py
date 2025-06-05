# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 14:33:31 2025

@author: marka
"""

#Depth-First-Search Algorithm:
def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])  #Gathers the size of the maze(rows and columns)
    stack = [ [start] ]  # Initialize the stack with the starting position as a path

    while stack:  
        path = stack.pop()  #Takes the last path added (LIFO behavior of DFS)
        x, y = path[-1]     #Gathers the current position's cell

        if (x, y) == end:   # If the current position is the goal
            return path     # Return the path as the solution

        #checks the four possible directions: down, right, up, left
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            next_x, next_y = x + dx, y + dy  # Compute the next cell's coordinates

            #The if loops checks to make sure the cell is within maze bounds and isn't a wall
            if 0 <= next_x < rows and 0 <= next_y < cols:
                if maze[next_x][next_y] != '#' and (next_x, next_y) not in path:
                    # Create a new path with the next cell added
                    new_path = list(path)
                    new_path.append((next_x, next_y))
                    stack.append(new_path)  #Adds the new path to the stack.

# Example maze where:
# 'S' is the Start, 'E' is the End, '#' are walls, and ' ' are open paths
maze = [
      #It goes by (row,column), the rows are numbered row 0 to row 5.
      #The columns are numbered from 0 to 5 also.
    ['S', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', ' '],
    ['#', ' ', ' ', ' ', ' ', ' '],
    ['#', '#', '#', ' ', '#', 'E'],
    ['#', '#', ' ', '#', ' ', '#'],
    [' ', '#', '#', '#', '#', '#']
]

start = (0, 0)  # Coordinates of the starting cell 'S'
end = (4, 5)    # Coordinates of the ending cell 'E'

#Calls the DFS function to find the path.
path = dfs(maze, start, end)

#Prints the path to the user screen.
print(path)
