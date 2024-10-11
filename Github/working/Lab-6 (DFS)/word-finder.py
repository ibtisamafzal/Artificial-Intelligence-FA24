def exist(board, word):
    # Function to perform DFS search
    def dfs(board, word, i, j, word_index):
        if word_index == len(word):  # All characters in the word are found
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[word_index]:
            return False
        
        # Mark the current cell as visited by setting it to a special character (e.g., '#')
        temp = board[i][j]
        board[i][j] = '#'
        
        # Explore all four possible directions (up, down, left, right)
        found = (dfs(board, word, i + 1, j, word_index + 1) or
                 dfs(board, word, i - 1, j, word_index + 1) or
                 dfs(board, word, i, j + 1, word_index + 1) or
                 dfs(board, word, i, j - 1, word_index + 1))
        
        # Restore the original character at the current cell
        board[i][j] = temp
        
        return found
    
    # Iterate over each cell in the grid to start a DFS search
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(board, word, i, j, 0):  # Start DFS from cells matching the first word character
                return True
    return False

# Custom board with the names: Jameel, Ibtisam, Adnan, Musab, Zaid, Shani
board = [
    ['J', 'A', 'M', 'E', 'E', 'L', 'X'],
    ['I', 'B', 'T', 'I', 'S', 'A', 'M'],
    ['A', 'D', 'N', 'A', 'N', 'X', 'X'],
    ['M', 'U', 'S', 'A', 'B', 'X', 'X'],
    ['Z', 'A', 'I', 'D', 'X', 'X', 'X'],
    ['S', 'H', 'A', 'N', 'I', 'X', 'X']
]

# Take word input from the user
word = input("Enter the word to search: ")

# Call the function and print the result
if exist(board, word):
    print(f"The word '{word}' exists in the board.")
else:
    print(f"The word '{word}' does not exist in the board.")
