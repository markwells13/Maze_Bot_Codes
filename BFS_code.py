from queue import Queue  # Import the Queue class for BFS
#The bfs algorthimn
def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])  # Get the number of rows and columns in the maze
    queue = Queue()  # Create a queue to store paths
    queue.put([start])  # Enqueue a list containing the start position as the first path

    while not queue.empty():  # Continue until there are no more paths to explore
        path = queue.get()  # Dequeue the next path to explore
        x, y = path[-1]     # Get the current position (the last cell in the path)

        if (x, y) == end:   # Check if we've reached the goal
            return path     # Return the successful path

        # Explore the four possible directions: down, right, up, left
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            next_x, next_y = x + dx, y + dy  # Calculate the next position

            # Check if the next position is within bounds
            if 0 <= next_x < rows and 0 <= next_y < cols:
                # Check that the next position is not a wall and not already in the current path, # is stands for a wall
                if maze[next_x][next_y] != '#' and (next_x, next_y) not in path:
                    new_path = list(path)  # Create a new path as a copy of the current path
                    new_path.append((next_x, next_y))  # Add the next position to the new path
                    queue.put(new_path)  # Enqueue the new path for further exploration

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

start = (0, 0)  # Coordinates of the start position 'S'
end = (4, 5)    # Coordinates of the end position 'E'

# Call the bfs function to find the shortest path from the start point to the end.
path = bfs(maze, start, end)

# Print the path as a list of (row, column) tuples
print(path)

