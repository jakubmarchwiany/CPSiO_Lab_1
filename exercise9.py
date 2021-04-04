import cv2
import sys
import cv2 as cv
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def sobel_mask_filter(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path).convert("L")
    # Wgranie obrazu do tablicy
    arr_image = np.asarray(image)

    # Wykrywanie krawędzi
    sobel_x = cv.Sobel(arr_image, -1, 1, 0, ksize = 3)
    sobel_y = cv.Sobel(arr_image, -1, 0, 1, ksize = 3)

    plt.figure(figsize=(15, 10))

    plt.subplot(1, 3, 1)
    plt.title('Obraz')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1,3,2)
    plt.title('Sobel X')
    plt.imshow(sobel_x, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 3, 3)
    plt.title('Sobel Y')
    plt.imshow(sobel_y, cmap='gray', vmin=0, vmax=255)
    plt.show()


def laplacian(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path).convert("L")
    # Wgranie obrazu do tablicy
    arr_image = np.asarray(image)

    laplac3 = cv.Laplacian(arr_image, -1, ksize = 3)
    laplac5 = cv.Laplacian(arr_image, -1, ksize = 5)
    laplac11 = cv.Laplacian(arr_image, -1, ksize= 11)

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title('Obraz')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title('Maska 3x3')
    plt.imshow(laplac3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 3)
    plt.title('Maska 5x5')
    plt.imshow(laplac5, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 4)
    plt.title('Maska 11x11')
    plt.imshow(laplac11, cmap='gray', vmin=0, vmax=255)
    plt.show()