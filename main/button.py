import pygame

class Button:
    def __init__(self, x, y, width, height, text='', font=None, font_size=30, text_color=(255, 255, 255), button_color=(0, 0, 255), hover_color=(0, 100, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color

        #states
        self.button_state = ["idle", "active", "hover"]
        self.cur_state = "idle"

        self.draw_rect = True

    def render(self, screen):
        # Change color on hover
        color = self.hover_color if self.cur_state == "hover" else self.button_color
        if(self.draw_rect): pygame.draw.rect(screen, color, self.rect)
        
        # Draw text
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def handle(self, mouse_pos):
        self.cur_state = "idle"
        #hover
        if self.rect.collidepoint(mouse_pos):
           
            self.cur_state = "hover" 

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]: # Left click
                        self.cur_state = "active"
                        
    
    def is_clicked(self):
        if self.cur_state == "active":
            return True
        return False

    def set_position(self,x,y):
        self.rect.x = x
        self.rect.y = y