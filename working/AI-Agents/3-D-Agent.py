# 3D Agent: moves in space (x, y, z)
def move_3D(position, step_x, step_y, step_z):
    return (position[0] + step_x, position[1] + step_y, position[2] + step_z)

# Current Position
position = (0, 0, 0)
print(f"Initial Position: {position}")

# Move the agent by (+1, +2, +3) and then (-2, -1, +1)
position = move_3D(position, 1, 2, 3)
print(f"Position after moving (+1, +2, +3): {position}")
position = move_3D(position, -2, -1, 1)
print(f"Position after moving (-2, -1, +1): {position}")