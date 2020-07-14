import pygame
import random

pygame.init()

win=pygame.display.set_mode((800,600))
bal=pygame.image.load('ball.png')
brick=pygame.image.load('bric.png')
bg=pygame.image.load('bg.png')

clock=pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x=400
        self.y=570
        self.color=(200,0,0)
        self.width=30
        self.height=30
    def draw(self):
        win.blit(bal,(self.x,self.y))

    


class Bar:
    def __init__(self):
        self.x=random.randrange(150,450)
        self.y=200
        self.width=200
        self.height=30
        self.color=(0,200,0)

    def draw(self):
        win.blit(brick,(self.x,self.y))
    def move(self,speed):
        self.y+=speed
        if(self.y>=600):
            self.y=0
            self.x=random.randrange(150,450)
        

speed=1
tick=60
jumpcount=9
jump=False
ball=Ball()
bar1=Bar()
bar1.y=400
bar2=Bar()
bar3=Bar()
bar3.y=0

isjump=False

done=False

while not done:
    win.blit(bg,(0,0))
    if(jump):
        bar1.move(speed)
    
    bar1.draw()
    if(jump):
        bar2.move(speed)
    bar2.draw()
    if(jump):
        bar3.move(speed)
    bar3.draw()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        tick+=1
        jump=True
        isjump=True
    if pressed[pygame.K_LEFT]:
        ball.x-=3
    if pressed[pygame.K_RIGHT]:
        ball.x+=3


    if(isjump):
        if jumpcount>=-9:
            neg=1
            if jumpcount<0:
                neg=-1
            ball.y-=(jumpcount**2)*neg
            jumpcount-=1
        else:
            done=True
            isjump=False
            jumpcount=9
            
    if(jump):    
        if(neg==-1 and (bar1.y-(ball.y+ball.height)<=20 and bar1.y-(ball.y+ball.height)>=0)):
            if(ball.x>=bar1.x-30 and ball.x<=bar1.x+200):
                isjump=False
                jumpcount=9
                ball.y=bar1.y-30
            else:
                done=True
            
        if(neg==-1 and (bar2.y-(ball.y+ball.height)<=20 and bar2.y-(ball.y+ball.height)>=0)):
            if(ball.x>=bar2.x-30 and ball.x<=bar2.x+200):
                isjump=False
                jumpcount=9
                ball.y=bar2.y-30
            else:
                done=True
            
        if(neg==-1 and (bar3.y-(ball.y+ball.height)<=20 and bar3.y-(ball.y+ball.height)>=0)):
            if(ball.x>=bar3.x-30 and ball.x<=bar3.x+200):
                isjump=False
                jumpcount=9
                ball.y=bar3.y-30
            else:
                done=True
            
        
            
    if(jump):
        if(ball.y>=560):
            done=True

    
    
    
    ball.draw()
    pygame.display.update()
    clock.tick(tick)


pygame.quit()
    
    

        
