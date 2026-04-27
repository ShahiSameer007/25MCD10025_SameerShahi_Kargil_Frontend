import pygame
import sys
from grid import create_grid, draw_grid, generate_maze, ROWS
from A_star import a_star

pygame.init()
font = pygame.font.SysFont("Arial", 18)

WIDTH = 600
HEIGHT = 650   
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding Visualizer")

grid = create_grid()

start = None
end = None
path = []

cell_size = WIDTH // ROWS

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                row = pos[1] // cell_size
                col = pos[0] // cell_size

                if not start:
                    start = (row, col)
                elif not end:
                    end = (row, col)
                else:
                    grid[row][col] = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start and end:
                result = a_star(grid, start, end)
                path.clear()

                if result:
                    current = end
                    while current in result:
                        path.append(current)
                        current = result[current]
                else:
                    print("No path found!")
            
            if event.key == pygame.K_c:
                grid = create_grid()
                start = None
                end = None
                path.clear()

            if event.key == pygame.K_r:
                generate_maze(grid, start, end)
                start = None
                end = None
                path.clear()

    WIN.fill((255, 255, 255))
    draw_grid(WIN, grid, start, end, path, WIDTH)
    text = "R: Maze | C: Clear | SPACE: Run A*"
    label = font.render(text, True, (0, 0, 0))
    WIN.blit(label, (10, 610))
    pygame.display.update()