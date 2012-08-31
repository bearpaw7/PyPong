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

def bounceHorizontal(direction):
    direction=(int)(direction)%360
    if direction<90:
        direction=360-direction
    elif direction<180:
        direction=270-(direction-90)
    elif direction<270:
        direction=180-(direction-180)
    else:
        direction=360-direction
    return direction
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
width=700
height=400
size=[width,height]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("PyPong")
 
#Loop until the user clicks the close button.
done=False
clock=pygame.time.Clock()

paddleLength=100
paddleWidth=20

player1column=40
player2column=650

player1top=(height/2)
player2top=(height/2)-paddleLength

player1movement=0
player2movement=0

# [x,y]
ball=[width/2.0,height/2.0]
ballDirection=45
ballRadius=15
ballSpeed=1.25

while done==False:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(30)
     
    for event in pygame.event.get(): # User did something
        # If user clicked close
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done=True # Flag that we are done so we exit this loop
        # First player
        if event.type == pygame.KEYUP and event.key == pygame.K_q:
            player1movement = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_a:
            player1movement = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            player1movement = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            player1movement = -1
        # Second player
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            player2movement = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            player2movement = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player2movement = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player2movement = -1
    # move player bars
    if player1movement > 0:
        player1top -= 5
    elif player1movement < 0:
        player1top += 5
    if player2movement > 0:
        player2top -= 5
    elif player2movement < 0:
        player2top += 5


    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(white)
 
    # Draw on the screen a green line from (0,0) to (100,100) 
    # 5 pixels wide.
    pygame.draw.line(screen,red,[player1column,player1top],[player1column,player1top+paddleLength],paddleWidth)
    pygame.draw.line(screen,blue,[player2column,player2top],[player2column,player2top+paddleLength],paddleWidth)

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


    if ball[0]>=player1column and ball[0]<=(player1column+paddleWidth):
        if ball[1]>player1top and ball[1]<(player1top+paddleLength):
            ballDirection+=180
            ballSpeed+=ballSpeed*0.20
    if ball[0]>=player2column and ball[0]<=(player2column+paddleWidth):
        print ball
        if ball[1]>player2top and ball[1]<(player2top+paddleLength):
            ballDirection+=180
            ballSpeed+=ballSpeed*0.20
    ballDirection%=360
    if ball[1]<0:
        ballDirection=bounceHorizontal(ballDirection)
        ball[1]=0
    elif ball[1]>height:
        ballDirection=bounceHorizontal(ballDirection)
        ball[1]=height

    ball[0]+=(ballSpeed*math.cos(ballDirection*pi/180)) 
    ball[1]+=(ballSpeed*math.sin(ballDirection*pi/180))
    pygame.draw.circle(screen,
                       black,
                       [(int)(ball[0]),(int)(ball[1])],
                       ballRadius,
                       0
    )


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

print 'Goodbye'
# Be IDLE friendly
pygame.quit ()



