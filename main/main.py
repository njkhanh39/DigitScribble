from loadmodel import RBF_SVM
from predict_image import ImageProcessor

import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:
    #clear before render

    screen.fill((0,0,0))

    #render
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True: 
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True: 
        player.move_ip(1,0)
    elif key[pygame.K_w] == True: 
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True: 
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update
    pygame.display.update()
    

pygame.quit()
# svc = RBF_SVM()
# svc.load()

# image_p = ImageProcessor()
# image_p.process('main\input\pic1.png')

# X_pred = image_p.raw_data #for predicting
# print("Predicted Value: ", svc.predict(X_pred))

# #draw image
# image_p.show_loaded_image()
