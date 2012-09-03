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
from random import randrange

# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
red =   [255,  0,  0]

pi=3.141592653

width=700
height=400

class Ball:
    def __init__(self,x,y,degrees):
        self.position=[x,y]
        self.direction=degrees
        self.radius=9
        self.velocity=1.25
        pygame.mixer.init()
        self.redsound=pygame.mixer.Sound("red.ogg")
        self.bluesound=pygame.mixer.Sound("blue.ogg")
        self.tink=pygame.mixer.Sound("tink.ogg")

    def top(self):
        return self.position[1]-self.radius
    def bottom(self):
        return self.position[1]+self.radius
    def left(self):
        return self.position[0]-self.radius
    def right(self):
        return self.position[0]+self.radius

    def collide(self, paddle):
        if paddle.color == red:
            if self.left()>=paddle.left() and self.left()<=paddle.right():
                if self.position[1]>=paddle.top() and self.position[1]<=paddle.bottom():
                    self.velocity=min((self.velocity+self.velocity*0.20),paddle.thick)
                    self.position[0]=paddle.right()+self.radius
                    self.direction=randrange(0,120)+300
                    self.tink.play()
        if paddle.color == blue:
            if self.right()<=paddle.right() and self.right()>=paddle.left():
                if self.position[1]>=paddle.top() and self.position[1]<=paddle.bottom():
                    self.velocity=min((self.velocity+self.velocity*0.20),paddle.thick)
                    self.position[0]=paddle.left()-self.radius
                    self.direction=randrange(120,240)
                    self.tink.play()

    def bounceHorizontal(self):
        self.direction=(int)(self.direction)%360
        if self.direction<90:
            self.direction=360-self.direction
        elif self.direction<180:
            self.direction=270-(self.direction-90)
        elif self.direction<270:
            self.direction=180-(self.direction-180)
        else:
            self.direction=360-self.direction

    def update(self,paddle1,paddle2):
        self.position[0]+=self.velocity*math.cos(self.direction*pi/180)
        self.position[1]-=self.velocity*math.sin(self.direction*pi/180)
        if self.top()<=0:
            self.bounceHorizontal()
            self.position[1]=self.radius
            self.velocity=min((self.velocity+self.velocity*0.20),paddle1.thick)
            self.tink.play()
        elif self.bottom()>=height:
            self.bounceHorizontal()
            self.position[1]=height-self.radius
            self.velocity=min((self.velocity+self.velocity*0.20),paddle1.thick)
            self.tink.play()
        if self.right()<0:
            self.position=[width/2,height/2]
            self.direction=0
            self.velocity=1.25
            paddle2.points+=1
            self.bluesound.play()
        elif self.left()>width:
            self.position=[width/2,height/2]
            self.direction=180
            self.velocity=1.25
            paddle1.points+=1
            self.redsound.play()
        self.collide(paddle1)
        self.collide(paddle2)

    def draw(self,screen):
        pygame.draw.circle(screen,black,[(int)(self.position[0]),(int)(self.position[1])],self.radius,0)
#        pygame.draw.line(screen, red, [0,self.top()], [800,self.top()], 1)
#        pygame.draw.line(screen, red, [0,self.bottom()], [800,self.bottom()], 1)
#        pygame.draw.line(screen, red, [self.left(),0], [self.left(),800], 1)
#        pygame.draw.line(screen, red, [self.right(),0], [self.right(),800], 1)

class Paddle:
    def __init__(self,_top,_column,_length,_color):
        # [x,y] is top left coordinate of paddle
        self.head=_top
        self.column=_column
        self.length=_length
        self.thick=14
        self.activity=0
        self.color=_color
        self.points=0

    def top(self):
        return self.head
    def bottom(self):
        return self.top()+self.length
    def left(self):
        return self.column-self.thick/2
    def right(self):
        return self.column+self.thick/2

    def score(self):
        return self.points.__str__()

    def setActivity(self,event):
        if self.color == red:
            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                self.activity=0
            elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                self.activity=0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.activity=1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.activity=-1
        elif self.color == blue:
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                self.activity=0
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                self.activity=0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.activity=1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.activity=-1

    def update(self):
        # move player bars
        if self.activity>0:
            self.head-=5
        elif self.activity<0:
            self.head+=5

    def draw(self,screen):
        pygame.draw.line(screen,self.color,[self.column,self.top()],[self.column,self.bottom()],self.thick)
#        pygame.draw.line(screen, black, [0,self.top()], [800,self.top()], 1)
#        pygame.draw.line(screen, blue, [0,self.bottom()], [800,self.bottom()], 1)
#        pygame.draw.line(screen, red, [self.left(),0], [self.left(),800], 1)
#        pygame.draw.line(screen, black, [self.right(),0], [self.right(),800], 1)

class PyPong:
    def __init__(self):
        print 'Initiated PyPong'

    def play(self):
    # Initialize the game engine
        pygame.init()
        
        size=[width,height]
        screen=pygame.display.set_mode(size)
        pygame.display.set_caption("PyPong")
        
        #Loop until the user clicks the close button.
        done=False
        clock=pygame.time.Clock()
        
        ball=Ball(width/2,height/2,0)
        # Paddle(top,column,length,color)
        player1=Paddle(height/3,40,height/6,red)
        player2=Paddle(height/3,width-50,height/6,blue)
        
        while done==False:
            # This limits the while loop to a max of 45 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(45)
        
            for event in pygame.event.get(): # User did something
                # If user clicked close
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    done=True # Flag that we are done so we exit this loop
                player1.setActivity(event)
                player2.setActivity(event)
        
            player1.update()
            player2.update()
            ball.update(player1,player2)
        #    print ball.position
            screen.fill(white)
        
            player1.draw(screen)
            player2.draw(screen)
            ball.draw(screen)
        
            font = pygame.font.Font(None, 25)
        
            # Render the text. "True" means anti-aliased text. 
            # Black is the color. This creates an image of the 
            # letters, but does not put it on the screen
            text = font.render("PyPong",True,black)
            score1text=font.render(player1.score(),True,red)
            score2text=font.render(player2.score(), True, blue)
        
            # Put the image of the text on the screen at 250x250
            screen.blit(text, [250,250])
            screen.blit(score1text,[50,0])
            screen.blit(score2text,[650,0])

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()
        
        print 'Goodbye'
        # Be IDLE friendly
        pygame.quit ()

if __name__ == '__main__':
    game=PyPong()
    game.play()


