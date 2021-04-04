import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def salt_and_pepper_noise(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path)
    # Wgranie obrazu do tablicy
    arr_image = np.asarray(image)
    # Określenie rozmiaru obrazu
    width, height = image.size

    # Zdefiniowanej stałych
    sp = 0.5
    amount = 0.05

    # Skopiowanie obrazu do tablicy
    arr_image_salt_pepper = np.copy(arr_image)

    # Stworzenie zakłóceń typu sól i pieprz
    num_salt = np.ceil(amount * arr_image.size * sp)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in arr_image.shape]
    arr_image_salt_pepper[tuple(coords)] = 1

    num_pepper = np.ceil(amount * arr_image.size * (1. - sp))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in arr_image.shape]
    arr_image_salt_pepper[tuple(coords)] = 0

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.title('Obraz oryginalny')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 3)
    plt.title('Obraz z szumem "sól i pieprz')
    plt.imshow(arr_image_salt_pepper, cmap='gray', vmin=0, vmax=255)

    print("Jaki Filtr użyć:\n"
          "[1] filtr uśredniający z kwadratową maską\n"
          "[2] nieliniowego filtra medianowego")

    choose = int(input("Twój wybór: "))

    if choose == 1:
        square_mask_filter(arr_image_salt_pepper)
    else:
        nonlinear_median_filter(arr_image_salt_pepper)



def square_mask_filter(arr_image_salt_pepper):
    # Filtrowanie przez kwadratową maskę
    new_image_mask_3x3 = cv2.blur(arr_image_salt_pepper, (3, 3))
    new_image_mask_9x9 = cv2.blur(arr_image_salt_pepper, (9, 9))
    new_image_mask_15x15 = cv2.blur(arr_image_salt_pepper, (15, 15))

    plt.subplot(2, 3, 4)
    plt.title('Szum "sól i pieprz", maska 3x3')
    plt.imshow(new_image_mask_3x3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 5)
    plt.title('Szum "sól i pieprz", maska 9x9')
    plt.imshow(new_image_mask_9x9, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 6)
    plt.title('Szum "sól i pieprz", maska 15x15')
    plt.imshow(new_image_mask_15x15, cmap='gray', vmin=0, vmax=255)

    plt.suptitle("Filtracja uśredniająca z kwadratową maską", fontsize=16)
    plt.show()


def nonlinear_median_filter(arr_image_salt_pepper):
    # Filtrowanie medianowe
    new_image_salt_pepper = np.array(arr_image_salt_pepper, dtype=np.uint8)
    new_image_mask_3x3 = cv2.medianBlur(new_image_salt_pepper, 3)
    new_image_mask_9x9 = cv2.medianBlur(new_image_salt_pepper, 9)
    new_image_mask_15x15 = cv2.medianBlur(new_image_salt_pepper, 15)

    plt.subplot(2, 3, 4)
    plt.title('Szum "sól i pieprz", maska 3x3')
    plt.imshow(new_image_mask_3x3, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 5)
    plt.title('Szum "sól i pieprz", maska 9x9')
    plt.imshow(new_image_mask_9x9, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 3, 6)
    plt.title('Szum "sól i pieprz", maska 15x15')
    plt.imshow(new_image_mask_15x15, cmap='gray', vmin=0, vmax=255)

    plt.suptitle("Filtracja medianowa", fontsize=16)
    plt.show()