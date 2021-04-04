import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image


def aligning_the_histogram(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path).convert('L')
    # Wgranie obrazu do tablicy
    arr_image = np.asarray(image)
    # Określenie rozmiaru obrazu
    width, height = image.size

    # Stworzenie 256 elementowej tablicy wypełnionej zerami
    image_histogram = numpy.zeros(256, dtype=int)

    # Wyliczeniu ile pixeli ma daną wartość 0-255
    for i in range(height - 1):
        for j in range(width - 1):
            image_histogram[arr_image[i, j]] += 1

    # Tworzenie tablicy dystrybuant empirycznych
    distributor = numpy.zeros(256, dtype=float)

    # Wyliczenie ilości pixeli na ekranie
    number_of_pixels = width * height

    # Oblicznie Dystrybuant
    sum_gray = 0.0
    for i in range(255):
        sum_gray += (image_histogram[i] / number_of_pixels)
        distributor[i] += sum_gray

    d0min = int(0)
    for i in range(255):
        if distributor[i] != 0:
            break
        else:
            d0min += 1

    # Tworzenie tablicy LUC
    luc_table = numpy.zeros(256, dtype=float)

    for i in range(256):
        luc_table[i] = int(((distributor[i] - distributor[d0min]) / (1 - distributor[d0min])) * (256 - 1))

    # Tworzenie tablicy rozmiaru obrazu
    new_arr_image = numpy.full_like(arr_image, 0)

    # Algorytm wybierania piexlu do nowego obrazu
    for i in range(height - 1):
        for j in range(width - 1):
            new_arr_image[i, j] = luc_table[arr_image[i, j]]

    # Tworzenie tablicy na nowy histogram
    new_image_histogram = numpy.zeros(256, dtype=int)

    for i in range(height - 1):
        for j in range(width - 1):
            new_image_histogram[new_arr_image[i, j]] += 1

    # Tworzenie wykresów
    # bla bla bla

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title('Obraz')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,2,2)
    plt.title("Histogram Obrazu")
    plt.plot(image_histogram,'b')

    plt.subplot(2, 2, 3)
    plt.title('Obraz po wyrównaniu histogramu',)
    plt.imshow(new_arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 4)
    plt.title("Histogram Obrazu")
    plt.plot(new_image_histogram,'b')

    plt.show()
