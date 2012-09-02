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

class Ball:
    def __init__(self,x,y,degrees):
        self.position=[x,y]
        self.direction=degrees
        self.radius=10
        self.velocity=1.25
    def top(self):
        return self.position[0]-self.radius
    def bottom(self):
        return self.position[0]+self.radius
    def left(self):
        return self.position[1]-self.radius
    def right(self):
        return self.position[1]+self.radius
    def collide(self, paddle):
        if self.left()>=paddle.left() and self.right()<=paddle.right():
            if self.top()>=paddle.top() and self.bottom()<=paddle.bottom():
                self.direction+=150
                self.velocity=min((self.velocity+self.velocity*0.20),paddle.width)
                if paddle.color == red:
                    self.position[0]=paddle.right()+self.radius
                if paddle.color == blue:
                    self.position[0]=paddle.left()-self.radius
    def update(self,paddle1,paddle2):
        self.position[0]+=self.velocity*math.cos(self.direction*pi/180)
        self.position[1]-=self.velocity*math.sin(self.direction*pi/180)

        if self.top()<0:
            self.direction=bounceHorizontal(self.direction)
            self.position[1]=self.radius
        elif self.bottom()>height:
            self.direction=bounceHorizontal(self.direction)
            self.position[1]=height-self.radius
        if self.right()<0:
            self.position=[width/2,height/2]
            self.direction=0
            self.velocity=1.25
        elif self.left()>width:
            self.position=[width/2,height/2]
            self.direction=0
            self.velocity=1.25
        self.collide(paddle1)
        self.collide(paddle2)
    def draw(self,screen):
        pygame.draw.circle(screen,black,[(int)(self.position[0]),(int)(self.position[1])],self.radius,0)

class Paddle:
    def __init__(self,x,y,_color):
        self.position=[x,y]
        self.width=15
        self.height=150
        self.activity=0
        self.color=_color
    def top(self):
        return self.position[0]
    def bottom(self):
        return self.position[0]+self.height
    def left(self):
        return self.position[1]
    def right(self):
        return self.position[1]+self.width
    def update(self,event):
        if self.color == red:
            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                self.activity=0
            elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                self.activity=0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.activity=1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.activity=-1
        if self.color == blue:
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                self.activity=0
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                self.activity=0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.activity=1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.activity=-1
        # move player bars
        if self.activity>0:
            self.position[0]-=5
        elif self.activity<0:
            self.position[0]+=5
    def draw(self,screen):
        pygame.draw.line(screen,self.color,[self.left(),self.top()],[self.left(),self.bottom()],self.width)

# Initialize the game engine
pygame.init()

size=[width,height]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("PyPong")

#Loop until the user clicks the close button.
done=False
clock=pygame.time.Clock()

ball=Ball(width/2,height/2,0)
player1=Paddle(40,height/3,red)
player2=Paddle(60,height/3,blue)

while done==False:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(45)

    for event in pygame.event.get(): # User did something
        # If user clicked close
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done=True # Flag that we are done so we exit this loop
        player1.update(event)
        player2.update(event)
    ball.update(player1,player2)

    screen.fill(white)

    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)

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




