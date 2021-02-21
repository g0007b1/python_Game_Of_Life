import pygame
import numpy as np
N = 60
pygame.init()

winWidth = 600
winHeight = 600
win = pygame.display.set_mode((winHeight, winWidth))

pygame.display.set_caption("Game")

# matrix = [[0] * N for i in range(N)]
matrix = np.random.randint(2, size=(N, N))
run = True


def drawStartPosition():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                pygame.draw.rect(win, (0, 0, 255), (i * 10, j * 10, 10, 10))
            if matrix[i][j] == 0:
                pygame.draw.rect(win, (255, 255, 255), (i * 10, j * 10, 10, 10))


def drawMatrix():
    for i in range(N):
        pygame.draw.line(win, (0, 0, 0), (i * 10, 0), (i * 10, winWidth), 1)
        for j in range(N):
            pygame.draw.line(win, (0, 0, 0), (0, j * 10), (winHeight, j * 10), 1)

def gameOfLife():
    cells = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(N):
        for j in range(N):
            if 2 < i < N-2 and 2 < j < N-2:
                total = matrix[i][j - 1] + matrix[i][j + 1] + matrix[i - 1][j] + matrix[i + 1][j] + matrix[i - 1][j - 1] + matrix[i - 1][j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j + 1]
                if matrix[i][j] == 1:
                    if (total < 2) or (total > 3):
                        cells[i][j] = 0
                if matrix[i][j] == 0:
                    if total == 3:
                        cells[i][j] = 1
                if (matrix[i][j] == 1 and total == 2) or (matrix[i][j] == 1 and total == 3):
                    cells[i][j] = 1
    for i in range(N):
        for j in range(N):
            matrix[i][j] = cells[i][j]


while run:
    pygame.time.delay(50)
    win.fill((255, 255, 255))
    drawStartPosition()
    # drawMatrix()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (x, y) = pygame.mouse.get_pos()
            matrix[x // 10][y // 10] = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        gameOfLife()
    if keys[pygame.K_r]:
        matrix = np.random.randint(2, size=(N, N))
    if keys[pygame.K_e]:
        matrix = [[0] * N for i in range(N)]

    # gameOfLife()
    pygame.display.flip()
pygame.quit()
