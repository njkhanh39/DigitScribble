import pygame

class Entity:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.die = False
        self.size_x = 0
        self.size_y = 0
    def render(self, display):
        pass
    def update(self, dt):
        pass
    def move(self, dt, dir):
        if(dir == "left"):
            self.x -= dt*self.speed
        else: self.x += dt*self.speed