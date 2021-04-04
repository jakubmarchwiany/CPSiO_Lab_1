import exercise5
import exercise6
import exercise7
import exercise8
import exercise9

global file_path


def tests():
    global file_path

    file_path = "C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_1/test.png"




def print_menu():
    print("----------------------------------\n"
          "---------------Menu---------------\n"
          "----------------------------------\n"
          "[0] Zamknij program\n"
          "[1] Wczytaj obraz z pliku\n"
          "[2] Wyświetl obraz\n"
          "[3] Wykres zmian poziomu szarości\n"
          "[4] Wybór podobrazu\n"
          "[5] Mnożenie obrazu przez stałą\n"
          "[6] Zmiana dynamiki skali szarości\n"
          "[7] Zmiana gammy\n"
          "[8] Wyrównywanie histogramu\n"
          "[9] Szum sól i pieprz\n"
          "[10] Filtra z maską Sobela do wykrywania krawędzi\n"
          "[11] Zaobserwuj działanie Laplasjanu")


def menu():
    global file_path
    tests()
    while True:
        print_menu()
        choose = float(input("Twój wybór : "))

        if choose == 0:
            break
        elif choose == 1:
            file_path = exercise5.read_file()
        elif choose == 2:
            exercise5.open_image(file_path)
        elif choose == 3:
            exercise5.draw_gray_plot(file_path)
        elif choose == 4:
            exercise5.snipping_area(file_path)
        elif choose == 5:
            exercise6.multiplication_by_constant(file_path)
        elif choose == 6:
            exercise6.dynamics_of_grayscale(file_path)
        elif choose == 7:
            exercise6.gamma_correction(file_path)
        elif choose == 8:
            exercise7.aligning_the_histogram(file_path)
        elif choose == 9:
            exercise8.salt_and_pepper_noise(file_path)
        elif choose == 10:
            exercise9.sobel_mask_filter(file_path)
        elif choose == 11:
            exercise9.laplacian(file_path)
        else:
            print("nie ma takiego wyboru")


if __name__ == '__main__':
    tests()
    menu()
