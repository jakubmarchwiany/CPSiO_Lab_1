import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def multiplication_by_constant(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path).convert('L')
    #image.show()

    # Tworzenie tablicy o rozmiarach obrazu
    arr_image = np.asarray(image)

    # Podanie stałej c
    c = float(input("Podaj stałą c : "))

    # Przemnożenie przez stałą
    new_image = arr_image * c


    plt.subplot(1, 2, 1)
    plt.title('Obraz')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('Obraz po przemnożeniu przez stałą '+ str(c))
    plt.imshow(new_image, cmap='gray', vmin=0, vmax=255)

    plt.show()


def dynamics_of_grayscale(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path).convert('L')

    # Wgranie obrazu do tablicy
    arr_image = np.asarray(image)

    # Określenie rozmiaru obrazu
    width, height = image.size

    # Zdefiniowanej stałych
    m = 0.35
    e = 8.0

    # Stworzenie odpowiedniego rozmiaru tablicy
    new_arr_image = np.full_like(arr_image, 0)

    # Algorytm
    for i in range(height - 1):
        for j in range(width - 1):
            if arr_image[i, j] == 0:
                new_arr_image[i, j] = arr_image[i, j]
            else:
                new_arr_image[i, j] = (255.0 / (1.0 + (m / (arr_image[i, j]/255.0)) ** e))

    plt.subplot(1, 2, 1)
    plt.title('Obraz')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('m = ' + str(m) +', e =' + str(e))
    plt.imshow(new_arr_image, cmap='gray', vmin=0, vmax=255)

    plt.show()


def gamma_correction(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path).convert('L')
    # Wgranie obrazu do tablicy
    arr_image = np.asarray(image)
    # Określenie rozmiaru obrazu
    width, height = image.size

    # Zdefiniowanej stałych
    y = 1.5
    c = 0.5



    # Stworzenie odpowiedniego rozmiaru tablicy
    new_arr_image = np.full_like(arr_image, 0)

    # Przemnożenie przez stałe
    new_arr_image = (arr_image ** y) * c

    plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    plt.title('Obraz')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('y = ' + str(y) + ', c =' + str(c))
    plt.imshow(new_arr_image, cmap='gray', vmin=0, vmax=255)

    plt.show()
