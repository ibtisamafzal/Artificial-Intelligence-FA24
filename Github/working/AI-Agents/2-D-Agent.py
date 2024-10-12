# 2D Agent: moves on a plane (x, y)
def move_2D(position, step_x, step_y):
    return (position[0] + step_x, position[1] + step_y)

# Current Position
position = (0, 0)
print(f"Initial Position: {position}")

# Move the agent by (+2, +3) and then (-1, -2)
position = move_2D(position, 2, 3)
print(f"Position after moving (+2, +3): {position}")
position = move_2D(position, -1, -2)
print(f"Position after moving (-1, -2): {position}")
