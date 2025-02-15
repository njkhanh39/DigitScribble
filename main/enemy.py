import pygame
from entity import Entity
from animation import Animation

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
            if(len(self.enemies) < self.max_size): self.enemies.append(Enemy(self.x, self.y))
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
    def kill_first(self):
        if(len(self.enemies)==0): return
        self.enemies.pop(0)

class Enemy(Entity): #bat
    def __init__(self, x, y):
        super().__init__(x, y, 100)
        self.init_animation()
    
    def init_animation(self):
        self.animation = Animation("main/images/enemy.png",180,120, 4, 100)
        self.size_x = 180
        self.size_y = 120
    
    def update(self, dt):
        #die
        if(self.x + self.size_x < 0):
            self.die = True

        #move
        self.move(dt, "left")

        #animation
        self.animation.update(dt)
    
    def render(self, display):
        self.animation.render(display, self.x, self.y)