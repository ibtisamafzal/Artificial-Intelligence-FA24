import matplotlib.pyplot as plt

def dfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])] 
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == goal:
            return path

        visited.add((x, y))

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append(((nx, ny), path + [(nx, ny)]))

    return None

# 2D
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)

goal_x = int(input("Enter goal row (0-4): "))
goal_y = int(input("Enter goal column (0-4): "))
goal = (goal_x, goal_y)


path = dfs(maze, start, goal)


if path:
    print("Path found:", path)
else:
    print("No path found.")



def visualize_maze(maze, path):
    plt.figure(figsize=(6, 6))
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 1:
                plt.plot(y, x, "ks", markersize=20)  
            else:
                plt.plot(y, x, "ws", markersize=20)  

  
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, "ro-", markersize=10, label="Path") 
        plt.plot(start[1], start[0], "go", markersize=15, label="Start") 
        plt.plot(goal[1], goal[0], "bo", markersize=15, label="Goal")    

    # Set plot details
    plt.gca().invert_yaxis()
    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.grid(True)
    plt.legend()
    plt.show()

visualize_maze(maze, path)