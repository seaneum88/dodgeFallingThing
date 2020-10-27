import os
import pygame
import random

#######################################################################################################
# initialization
pygame.init()

# screen setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title screen
pygame.display.set_caption("Dodge Falling Thing") # game name

# FPS
clock = pygame.time.Clock()
#######################################################################################################

# 1. game setting (background, game image, position, speed, font...)
current_path = os.path.dirname(__file__) # current file location
image_path = os.path.join(current_path, "images") # images file location

# getting background image
background = pygame.image.load(os.path.join(image_path, "background.png"))

# making character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size # getting image size
character_width = character_size[0] # width size of character
character_height = character_size[1] # height size of character
character_x_pos = (screen_width / 2) - (character_width / 2) # half size of the screen - half of the character size
character_y_pos = screen_height - character_height # bottom position of the screen

# character position
character_to_x = 0

# character speed
character_speed = 5

# making unicorn
unicorn = pygame.image.load(os.path.join(image_path, "unicorn.png"))
unicorn_size = unicorn.get_rect().size
unicorn_width = unicorn_size[0]
unicorn_height = unicorn_size[1]
unicorn_x_pos = random.randint(0, (screen_width - unicorn_width))
unicorn_y_pos = 0

# unicorn speed
unicorn_speed = 10

# define Font
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks() # start time

game_result = "Game Over"

# font
game_font = pygame.font.Font(None, 40) # create font

# play time
total_time = 60

# start time
start_ticks = pygame.time.get_ticks() # getting tick

# event loop
running = True
while running:
    dt = clock.tick(30) # setting in game frame per second

    # 2. handling event (keyboard, mouse..)
    for event in pygame.event.get(): # recognizing event
        if event.type == pygame.QUIT: # when user click exit button
            running = False

        if event.type == pygame.KEYDOWN: # check if key is down
            if event.key == pygame.K_LEFT: # check if left key is working
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # check if right key is working
                character_to_x += character_speed

        if event.type == pygame.KEYUP: # check if key is up
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. character position
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. handling collision

    # character rect info
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos 

    unicorn_rect = unicorn.get_rect()
    unicorn_rect.left = unicorn_x_pos
    unicorn_rect.top = unicorn_y_pos

    if character_rect.colliderect(unicorn_rect):
        print("OOOPS~~")
        running = False

    # 5. display
    screen.blit(background, (0, 0)) # adding background image from variable
    screen.blit(character, (character_x_pos, character_y_pos)) # adding character image from variable
    screen.blit(unicorn, (unicorn_x_pos, unicorn_y_pos)) # adding unicorn image from variable

    unicorn_y_pos += unicorn_speed

    if unicorn_y_pos > screen_height:
        unicorn_speed += 1
        unicorn_y_pos = 0
        unicorn_x_pos = random.randint(0, (screen_width - unicorn_width))

    # calculate game time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # if time is over
    if total_time - elapsed_time <= 0:
        game_result = "YOU WIN"
        running = False

    pygame.display.update() # re-displaying game screen

# game over message
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)


# delay before exit
pygame.time.delay(2000) # 2 second delay before exit

# exit pygame
pygame.quit()