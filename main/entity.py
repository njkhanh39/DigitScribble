import pygame

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.die = False
    def render(self, display):
        pass
    def update(self, dt):
        pass