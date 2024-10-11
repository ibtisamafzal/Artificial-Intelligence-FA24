from collections import deque
import tkinter as tk

# Define the initial maze (2D grid),
maze = [
    ['S', '0', '1', '0', '0', '0'],
    ['0', '1', '0', '1', '1', '0'],
    ['0', '1', '0', '0', '0', '0'],
    ['0', '0', '1', '1', '1', '0'],
    ['1', '0', '0', '0', '0', '0'],
]

# Possible moves: right, down, left, up
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Take the goal coordinates from the user
def get_goal_from_user():
    goal_row = int(input("Enter the goal row: "))
    goal_col = int(input("Enter the goal column: "))
    maze[goal_row][goal_col] = 'G'
    return (goal_row, goal_col)

# BFS to find the shortest path
def bfs(maze):
    rows, cols = len(maze), len(maze[0])
    start = goal = None
    
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S': start = (r, c)
            if maze[r][c] == 'G': goal = (r, c)
    
    queue, visited, parent_map = [start], {start}, {}

    while queue:
        row, col = queue.pop(0)

        if (row, col) == goal:
            path = []
            while (row, col) != start:
                path.append((row, col))
                row, col = parent_map[(row, col)]
            return path[::-1]  # Return reversed path

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and maze[new_row][new_col] != '1':
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
                parent_map[(new_row, new_col)] = (row, col)

    return []  # Return empty path if not found

# Draw the maze and path on the UI
def draw_maze(maze, path):
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            color = 'white' if cell == '0' else 'black' if cell == '1' else 'green' if cell == 'S' else 'red'
            if (r, c) in path and cell not in ['S', 'G']:
                color = 'pink'
            canvas.create_rectangle(c * cell_size, r * cell_size, (c + 1) * cell_size, (r + 1) * cell_size, fill=color)

# Initialize the graphical window
window = tk.Tk()
window.title("Maze Game with BFS")
cell_size = 50
canvas = tk.Canvas(window, width=len(maze[0]) * cell_size, height=len(maze) * cell_size)
canvas.pack()

# Get the goal point from the user
goal = get_goal_from_user()

# Perform BFS and draw the maze
path = bfs(maze)
draw_maze(maze, path)

# Start the Tkinter event loop
window.mainloop()
