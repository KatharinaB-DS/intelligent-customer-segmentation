import random
import intro
import calcul

liczbaKlastrów = 6
maks_iteracji = 100

# Główne zmienne
medoidy = []
klastry = []

# Funkcja do przypisania punktów do najbliższego medoidu
def przypisz_do_klastra():
    global klastry
    klastry = [[] for _ in range(liczbaKlastrów)]
    for punkt in intro.krotkiNormal:
        min_dist = float('inf')
        min_index = -1
        for i, medoid in enumerate(medoidy):
            dist = calcul.oblicz_odległość(punkt, medoid)
            if dist < min_dist:
                min_dist = dist
                min_index = i
        klastry[min_index].append(punkt)

# Funkcja obliczająca nowy medoid w obrębie klastra
def znajdz_nowy_medoid(klaster):
    min_suma = float('inf')
    najlepszy = klaster[0]
    for kandydat in klaster:
        suma = 0
        for punkt in klaster:
            suma += calcul.oblicz_odległość(kandydat, punkt)
        if suma < min_suma:
            min_suma = suma
            najlepszy = kandydat
    return najlepszy

# Funkcja główna algorytmu

def kmedoids():
    global medoidy
    intro.krotkiNormal.clear()
    intro.krotkiDane.clear()
    intro.wczytajDane()
    intro.normalizujDane()

    # Wybierz losowo k medoidów (rzeczywiste punkty)
    medoidy = random.sample(intro.krotkiNormal, liczbaKlastrów)

    for _ in range(maks_iteracji):
        przypisz_do_klastra()
        nowe_medoidy = [znajdz_nowy_medoid(klaster) for klaster in klastry]
        if nowe_medoidy == medoidy:
            print(" Medoidy ustabilizowały się. Koniec iteracji.")
            break
        medoidy = nowe_medoidy

    # Wypisz wyniki
    for i, medoid in enumerate(medoidy):
        print(f"Klaster {i}, Medoid: {medoid[:-1]}")  # ukryje -1
        print(f"Liczba punktów: {len(klastry[i])}")

# Funkcja testowa

def test():
    global liczbaKlastrów
    liczbaKlastrów = 6
    calcul.metryka = 'euclidean'  # lub 'manhattan'
    kmedoids()
