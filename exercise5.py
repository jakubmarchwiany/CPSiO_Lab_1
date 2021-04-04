import tkinter.filedialog

import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image


def read_file():
    window = tkinter.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    file_path = tkinter.filedialog.askopenfilename()

    return file_path


def open_image(file_path):
    if file_path is None:
        print("File path is null")
    else:
        image = Image.open(file_path)
        arr_image = np.asarray(image)

        plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

        plt.show()

        #image.show()


def draw_gray_plot(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path).convert("L")
    # Wgranie obrazu do tablicy
    arr_image = np.asarray(image)
    # Określenie rozmiaru obrazu
    width, height = image.size

    # Wybór opcji lini
    print("Wykres:\n"
          "[1] Z Lini poziomej\n"
          "[2] Z Lini poziomej")

    choose = int(input("Twój wybór : "))

    if choose == 1:
        y = int(input("Podaj y (0," + str(height - 1) + ")"))
        # Zapisanie wartości pixeli z danej lini poziomej do tablicy
        one_gray_line_array = arr_image[y, :]
    elif choose == 2:
        x = int(input("Podaj x (0," + str(width - 1) + ")"))
        # Zapisanie wartości pixeli z danej lini pionowej do tablicy
        one_gray_line_array = arr_image[:, x]


    plt.figure(figsize=(15, 10))

    plt.subplot(1, 2, 1)
    plt.title('Obraz')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.plot(one_gray_line_array,'b')
    plt.title('Wykres zmian poziomu szarości')
    plt.xlabel('Numer pixela')
    plt.ylabel('Poziom szarości')
    plt.show()

    plt.show()


def snipping_area(file_path):
    # Otworzenie obrazu z wybranego pliku
    image = Image.open(file_path).convert('RGB')
    # Wgranie obrazu do tablicy
    arr_image = np.asarray(image)
    # Określenie rozmiaru obrazu
    width, height = image.size

    print("Podaj początkowy punkt wycięcia: ")
    y1 = int(input("Podaj x1 (0," + str(height - 1) + ")"))
    x1 = int(input("Podaj y1 (0," + str(width - 1) + ")"))
    print("Podaj końcowy punkt wycięcia: ")
    y2 = int(input("Podaj x2 (0," + str(height - 1) + ")"))
    x2 = int(input("Podaj y2 (0," + str(width - 1) + ")"))

    # Stworzenie odpowiedniego rozmiaru tablicy
    arr_snipping_area = numpy.zeros((x2 - x1, y2 - y1, 3), dtype=np.uint8)

    # Wycięcie odpowiedniego fragmentu do tablicy
    for i in range(x2 - x1):
        for j in range(y2 - y1):
            arr_snipping_area[i, j] = arr_image[x1 + i, y1 + j]

    plt.figure(figsize=(15, 10))

    plt.subplot(1, 2, 1)
    plt.title('Obraz')
    plt.imshow(arr_image, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1, 2, 2)
    plt.title('Obraz po wycięciu')
    plt.imshow(arr_snipping_area, cmap='gray', vmin=0, vmax=255)


    plt.show()
    new_image = Image.fromarray(arr_snipping_area, 'RGB')
    new_image.save('new.png')
    new_image.show()
