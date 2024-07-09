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
dark_green = pygame.Color(0, 100, 0)
snake_spd = 10
snake_direction = 'RIGHT'


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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F2:
                game_running = False

    
    #setting snake default to right by default for testing
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    #update snake positioning and deleted
    snake_body.insert(0, list(snake_pos))
    snake_body.pop()

    #update screen before redrawing snake
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, dark_green, pygame.Rect(pos[0], pos[1], 12, 12))
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0] + 1, pos[1] + 1, 10, 10))

    
    pygame.display.update()
    #print current positions of the snake body
    print(snake_body)
    fps.tick(snake_spd)