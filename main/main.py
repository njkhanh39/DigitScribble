from loadmodel import RBF_SVM
from predict_image import ImageProcessor

import pygame
from game import Game


pygame.init()

g = Game()

while g.running:
    g.game_loop()

pygame.quit()


# svc = RBF_SVM()
# svc.load()

# image_p = ImageProcessor()
# image_p.process('main\input\pic1.png')

# X_pred = image_p.raw_data #for predicting
# print("Predicted Value: ", svc.predict(X_pred))

# #draw image
# image_p.show_loaded_image()
