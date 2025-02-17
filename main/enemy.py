import pygame
from entity import Entity
import random
from animation import Animation
from button import Button
import global_constants as gc

class Label: #moving label on top of entity's head
    def __init__(self, x, y, num = 0):
        self.x = x
        self.y = y
        self.font_dir = gc.FONT_DIR
        self.key = num
        self.init_label()

    def init_label(self):
        self.text = Button(self.x, self.y, 60, 60, str(self.key), self.font_dir, 30, (128,0,128))
        #to not draw the rect
        self.text.draw_rect = False

    def update(self, dt, velocity):
        self.x -= velocity*dt
        self.text.set_position(self.x, self.y)


    def render(self, display):
        self.text.render(display)
        

class EnemySpawner: #x = 1000, y = 70
    def __init__(self, x, y, spawn_rate = 25):
        self.timer = 0
        self.spawn_rate = spawn_rate

        #spawn coordinate
        self.x = x
        self.y = y

        #enemies array
        self.max_size = 10
        self.enemies = []

    def update(self, delt):
        self.timer += 10*delt

        #update spawning
        if(self.timer > self.spawn_rate):
            self.timer = 0
            #spawn
            if(len(self.enemies) < self.max_size): 
                num = random.randint(0, 9)
                self.enemies.append(Enemy(self.x, self.y, num))
        #update enemies dead or alive

        for i in range(0, len(self.enemies)):
            if(self.enemies[i].die == True):
                self.enemies.pop(i)
                break
            else:
                self.enemies[i].update(delt)
    def render(self, display):
        #render entities
        for en in self.enemies:
            en.render(display)
    
    #kill first enemy
    def check_kill(self, key):
       # print("Checking for key = ", key)
        if(len(self.enemies)==0): return
        for i in range(0,len(self.enemies)):
           # print("enemy key: ", self.enemies[i].label.key)
            if(key == self.enemies[i].label.key):
                self.enemies.pop(i)
                break

class Enemy(Entity): #bat
    def __init__(self, x, y, number = 0):
        super().__init__(x, y, 100)
        self.init_animation()

        #assigned label
        self.label = Label(x + 80, y - 30, number)
    
    def init_animation(self):
        self.animation = Animation("main/images/enemy.png",180,120, 4, 100)
        self.size_x = 180
        self.size_y = 120
    
    def update(self, dt):
        #die
        if(self.x + self.size_x < 0):
            self.die = True

        #move
        self.label.update(dt, self.speed)
        self.move(dt, "left")

        #animation
        self.animation.update(dt)
    
    def render(self, display):
        self.label.render(display)
        self.animation.render(display, self.x, self.y)