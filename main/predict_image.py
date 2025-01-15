from loadmodel import RBF_SVM
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

class ImageProcessor: #read image from file, turn that image in to raw data
    def __init__(self):
        self.raw_data = None

    def process(self, image_path = 'main\input\pic1.png'):
        image = Image.open(image_path)
        image = image.resize((28, 28))
        image = image.convert('L')  # 'L' mode is 8-bit pixels, grayscale
        image_array = np.array(image)
        raw_data = image_array.flatten()

        #this one is for drawing
        self.image_data = raw_data.reshape(28, 28)

        #for feeding to SVM (it will be applied with PCA then normalized later)
        self.raw_data = raw_data.reshape(1, -1)
    
    def show_loaded_image(self):
        plt.imshow(self.image_data, cmap='gray')
        plt.axis('off')
        plt.show()  