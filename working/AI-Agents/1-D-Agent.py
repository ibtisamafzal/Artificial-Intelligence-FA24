# 1D Agent: moves along a line (x-axis)
def move_1D(position, step):
    return position + step

#Current Position
position = 0
print(f"Initial Position: {position}")

# Move the agent by +3 and then -2
position = move_1D(position, 3)
print(f"Position after moving +3: {position}")
position = move_1D(position, -2)
print(f"Position after moving -2: {position}")
