'''
Created on Aug 30, 2012

@author: bearpaw7
'''
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
 
# Import a library of functions called 'pygame'

import math
import pygame
#from pygame import math

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

pi=3.141592653

# Set the height and width of the screen
size=[700,400]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("PyPong")
 
#Loop until the user clicks the close button.
done=False
clock = pygame.time.Clock()

player1y=200
player1move=0
player2y=200
player2move=0
ballx=350
bally=200
balldirection=0

while done==False:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        # First player
        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            player1move = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_a:
            player1move = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            player1move = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            player1move = -1

        # Second player
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            player2move = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            player2move = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player2move = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player2move = -1
    # move player bars
    if player1move > 0:
        player1y -= 10
    elif player1move < 0:
        player1y += 10
    if player2move > 0:
        player2y -= 10
    elif player2move < 0:
        player2y += 10


    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(white)
 
    # Draw on the screen a green line from (0,0) to (100,100) 
    # 5 pixels wide.
    pygame.draw.line(screen,red,[40,player1y],[40,player1y+140],10)
    pygame.draw.line(screen,blue,[640,player2y],[640,player2y+140],10)

    # Draw on the screen several green lines from (0,10) to (100,110) 
    # 5 pixels wide using a loop
#    y_offset=0
#    while y_offset < 100:
#        pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
#        y_offset=y_offset+10
 
    # Draw a rectangle
#    pygame.draw.rect(screen,black,[20,20,250,100],2)
     
    # Draw an ellipse, using a rectangle as the outside boundaries
#    pygame.draw.ellipse(screen,black,[20,20,250,100],2) 
 
    # Draw an arc as part of an ellipse. 
    # Use radians to determine what angle to draw.
#    pygame.draw.arc(screen,black,[20,220,250,200], 0, pi/2, 2)
#    pygame.draw.arc(screen,green,[20,220,250,200], pi/2, pi, 2)
#    pygame.draw.arc(screen,blue, [20,220,250,200], pi,3*pi/2, 2)
#    pygame.draw.arc(screen,red, [20,220,250,200],3*pi/2, 2*pi, 2)
    
    ballx += (int)(math.sin(balldirection*pi/180))
    bally += (int)(math.cos(balldirection*pi/180))
    
    pygame.draw.circle(screen, black, (ballx, bally), 15, 0)
    # This draws a triangle using the polygon command
#    pygame.draw.polygon(screen,black,[[100,100],[0,200],[200,200]],5)
 
    # Select the font to use. Default font, 25 pt size.
    font = pygame.font.Font(None, 25)
 
    # Render the text. "True" means anti-aliased text. 
    # Black is the color. This creates an image of the 
    # letters, but does not put it on the screen
    text = font.render("PyPong",True,black)
 
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250,250])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit ()




