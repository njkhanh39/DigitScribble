import pygame
from entity import Entity
from animation import Animation

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.init_animation()
    
    def init_animation(self):
        self.animation = Animation("main\images\wasp_left.png",40,40, 3, 60)
    
    def update(self, dt):
        self.animation.update(dt)
    
    def render(self, display):
        self.animation.render(display, self.x, self.y)