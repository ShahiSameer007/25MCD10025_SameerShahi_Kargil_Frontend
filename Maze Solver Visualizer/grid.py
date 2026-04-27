import pygame
import random

ROWS = 30

def create_grid():
    return [[0 for _ in range(ROWS)] for _ in range(ROWS)]

def generate_maze(grid, start=None, end=None):
    import random

    for row in range(ROWS):
        for col in range(ROWS):
            if random.random() < 0.25:  
                grid[row][col] = 1
            else:
                grid[row][col] = 0

    
    if start:
        r, c = start
        grid[r][c] = 0
    if end:
        r, c = end
        grid[r][c] = 0

def draw_grid(win, grid, start, end, path, width):
    cell_size = width // ROWS

    for row in range(ROWS):
        for col in range(ROWS):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)

            if (row, col) == start:
                pygame.draw.rect(win, (0, 255, 0), rect)
            elif (row, col) == end:
                pygame.draw.rect(win, (255, 0, 0), rect)
            elif (row, col) in path:
                pygame.draw.rect(win, (0, 0, 255), rect)
            elif grid[row][col] == 1:
                pygame.draw.rect(win, (0, 0, 0), rect)

            pygame.draw.rect(win, (200, 200, 200), rect, 1)