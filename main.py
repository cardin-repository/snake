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
dir_change_check = snake_direction


# Initialize game

pygame.init()
game_running = True

# Display game window & display fps

game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Press F2 to quit")
fps = pygame.time.Clock()

# Create snake & position

snake_pos = [100, 50]
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

# function for direction checks to avoid opposite direction changes

def dir_check():
    global snake_direction, dir_change_check

    # check if input change is opposite, if its not allow direction change

    if dir_change_check == 'LEFT' and snake_direction != 'RIGHT':
        snake_direction = 'LEFT'
    if dir_change_check == 'RIGHT' and snake_direction != 'LEFT':
        snake_direction = 'RIGHT'
    if dir_change_check == 'DOWN' and snake_direction != 'UP':
        snake_direction = 'DOWN'
    if dir_change_check == 'UP' and snake_direction != 'DOWN':
        snake_direction = 'UP'

# function to facilitate snake movement

def snake_move():
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'UP':
        snake_pos[1] -= 10

# update snake body parts

def update_snake():
    snake_body.insert(0, list(snake_pos))
    snake_body.pop()

# drawing snake function

def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(game_window, dark_green, pygame.Rect(pos[0], pos[1], 12, 12))
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0] + 1, pos[1] + 1, 10, 10))

# main function

while game_running:

    # check for key inputs, F2 to QUIT

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dir_change_check = 'RIGHT'
            if event.key == pygame.K_LEFT:
                dir_change_check = 'LEFT'
            if event.key == pygame.K_DOWN:
                dir_change_check = 'DOWN'
            if event.key == pygame.K_UP:
                dir_change_check = 'UP'
            if event.key == pygame.K_F2:
                game_running = False

    # check for illegal moves

    dir_check()

    # adjust snake direction

    snake_move()

    # update snake positioning and delete last

    update_snake()

    # update screen before redrawing snake

    game_window.fill(black)

    # draw snake and outline

    draw_snake()

    # update game

    pygame.display.update()
    fps.tick(snake_spd)