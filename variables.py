import numpy as np
import pygame

# Dimensiones del tablero y tamaño de las celdas
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Inicializa pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Inicializa el tablero con celdas muertas
grid = np.zeros((ROWS, COLS), dtype=int)