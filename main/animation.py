import pygame

class Animation:
    def __init__(self, sprite_file, frame_width, frame_height, frame_count, frame_rate):
        self.sprite_sheet = pygame.image.load(sprite_file)
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_count = frame_count
        self.frame_rate = frame_rate
        self.current_frame = 0
        self.timer = 0

    def update(self, dt):
        self.timer += 600*dt
        if self.timer >= self.frame_rate:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % self.frame_count

    def render(self, surface, x, y):
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        surface.blit(self.sprite_sheet, (x, y), frame_rect)
