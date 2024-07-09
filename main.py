import pygame, time, random

# Setting window size for game

window_x = 1200
window_y = 900

# Define vars

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
snake_spd = 10

# Initialize game

pygame.init()
game_running = True

# Display game window & display fps

game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("hoc and cardin")
fps = pygame.time.Clock()

# Create snake & position

snake_pos = [100, 50]
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

# main function

while game_running:
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.display.update()
    fps.tick(snake_spd)