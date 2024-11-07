graph_structure = {
    'A': [('B', 4), ('C', 3)],
    'B': [('F', 5)],
    'C': [('E', 10), ('D', 7)],
    'D': [('E', 2)],
    'E': [('G', 5)],
    'F': [('G', 16)]
}

heuristic_values = {
    'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0
}

# A* search function
def a_star(start_node, end_node):
    to_explore = [(heuristic_values[start_node], 0, start_node, [start_node])]
    
    while to_explore:
        to_explore.sort()
        f_score, g_score, current_node, current_path = to_explore.pop(0)
        
        if current_node == end_node:
            return current_path, g_score
        
        # Check neighboring nodes
        for neighbor, travel_cost in graph_structure.get(current_node, []):
            new_g_score = g_score + travel_cost
            new_f_score = new_g_score + heuristic_values[neighbor]
            
            to_explore.append((new_f_score, new_g_score, neighbor, current_path + [neighbor]))

# Execute A* search from A to G
result_path, total_cost = a_star('A', 'G')
print("Resulting Path:", result_path)
print("Total Cost:", total_cost)