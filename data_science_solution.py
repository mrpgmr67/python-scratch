def create_empty_grid(rows, columns):
    """Create an empty grid with the given dimensions."""
    return [[' ' for _ in range(columns)] for _ in range(rows)]


def place_word_in_grid(grid, word, row, col, direction):
    """Place a word in the grid at the specified location and direction."""
    for i in range(len(word)):
        if direction == 'across' and col + i < len(grid[0]):
            grid[row][col + i] = word[i]
        elif direction == 'down' and row + i < len(grid):
            grid[row + i][col] = word[i]


# Initialize the grid
grid_size = (20, 20)  # Rows, Columns
crossword_grid = create_empty_grid(*grid_size)

# Place the words in the grid
# Across
place_word_in_grid(crossword_grid, "RESULTS", 1, 3, 'across')
place_word_in_grid(crossword_grid, "ANALYTICS", 4, 1, 'across')
place_word_in_grid(crossword_grid, "CLEANING", 10, 1, 'across')
place_word_in_grid(crossword_grid, "BLACKBOX", 8, 4, 'across')

# Down
place_word_in_grid(crossword_grid, "STORYTELLING", 1, 5, 'down')
place_word_in_grid(crossword_grid, "STATISTICS", 2, 1, 'down')
place_word_in_grid(crossword_grid, "AI", 4, 3, 'down')
place_word_in_grid(crossword_grid, "MODEL", 7, 10, 'down')

# Print the grid
for row in crossword_grid:
    print(' '.join(row))
