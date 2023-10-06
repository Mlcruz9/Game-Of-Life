import pygame
from variables import ROWS, COLS, CELL_SIZE, WIDTH, HEIGHT, screen, grid
from time import sleep

# Función para dibujar el tablero en función de la matriz grid
def draw_grid():
    screen.fill((0, 0, 0))
    for i in range(ROWS):
        for j in range(COLS):
            color = (0, 255, 0) if grid[i, j] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Calcula el siguiente estado del tablero
def next_state(grid):
    new_grid = grid.copy()
    for i in range(1, ROWS - 1):
        for j in range(1, COLS - 1):
            neighbors = grid[i - 1:i + 2, j - 1:j + 2]
            total_neighbors = neighbors.sum() - grid[i, j]
            if grid[i, j] == 1 and (total_neighbors < 2 or total_neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and total_neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

# Función para permitir al usuario configurar el estado inicial
def set_initial_state():
    global grid
    running = True
    placing = True  # Variable que indica si el usuario está colocando elementos
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and placing:
                # Obtén la posición del clic del ratón y actualiza el estado de la celda correspondiente
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                grid[row, col] = 1 if grid[row, col] == 0 else 0
                draw_grid()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # El usuario presionó la barra espaciadora para finalizar la configuración
                placing = False

                while running:
                    sleep(0.5)
                    grid = next_state(grid)

                    # Dibuja el tablero en la pantalla
                    screen.fill((0, 0, 0))
                    for i in range(ROWS):
                        for j in range(COLS):
                            color = (155, 155, 155) if grid[i, j] == 1 else (0, 0, 0)
                            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
            

                    pygame.display.flip()
                    clock.tick(10)