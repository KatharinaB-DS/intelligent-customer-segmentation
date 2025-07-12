#moduł przechowuje początkową liczbę klastrów,
#oraz poczatkową pustą listę klastrów i centroidów.
#UWAGA: wartości poczatkowe zmiennych modułowych
#       są dostępne po każdorazowym załadowaniu modułu

import math
import random
import intro

metryka = 'euclidean'  # 'manhattan' 'euclidean'
liczbaKlastrów =6
# poczatkowa liczba klastró
klastry = []
#każdy z klastrów jest listą krotekNormal położonych najbliżej centroidy
Centroidy = []


def test():
    print('\nLICZBA KLASTRÓW ', liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()
    losujCentroidy()
    wypiszCentroidy()
    przypiszKrotkomNumeryKlastrów()
    #intro.wypiszKrotkiNormal()
    utwórzKlastry()
    #wypiszKlastry()
    newCentroidy()
    wypiszCentroidy()


def losujCentroide():
    # losuje początkowe położenie centroidy dla pojedynczego klastra
    centroida = []
    for _ in range(3):  # 3 cechy znormalizowane
        centroida.append(random.uniform(0.0, 1.0))
    # kraj losowany jako liczba całkowita (1–38)
    centroida.append(random.randint(1, 38))
    return centroida


def losujCentroidy():
    # losuje określoną przez liczbę klastrów poczatkowe położenia centroid
    i = 1
    while i <= liczbaKlastrów:
        Centroidy.append(losujCentroide())
        i = i + 1


def wypiszCentroide(centroida):
    print('%7.3f %7.3f %7.3f %3d' % (centroida[0], centroida[1], centroida[2], centroida[3]))


def wypiszCentroidy():
    # wypisuje do interpretera aktualne wartości wszystkich centroid
    print('CENTROIDY')
    for centroida in Centroidy:
        wypiszCentroide(centroida)


def oblicz_odległość(krotkaNormal, centroida):
    suma = 0
    for i in range(len(krotkaNormal) - 1):  # pomijamy indeks klastra
        if metryka == 'euclidean':
            diff = centroida[i] - krotkaNormal[i]
            suma += diff ** 2
        elif metryka == 'manhattan':
            suma += abs(centroida[i] - krotkaNormal[i])
    return suma


def przypiszKrotkomNumeryKlastrów():
    for krotkaNormal in intro.krotkiNormal:
        minimum = 1e100
        for i in range(len(Centroidy)):
            next = oblicz_odległość(krotkaNormal, Centroidy[i])
            if next < minimum:
                minimum = next
                minimumIndex = i

        if len(krotkaNormal) == 4:
            krotkaNormal.append(minimumIndex)
        else:
            krotkaNormal[4] = minimumIndex



def utwórzKlastry():
    klastry.clear()
    for i in range(len(Centroidy)):
        klaster = []
        for krotka in intro.krotkiNormal:
            if len(krotka) >= 5 and krotka[4] == i:
                klaster.append(krotka)
        klastry.append(klaster)



def wypiszKlaster(nrKlastra):
    print('NUMER KLASTRA ', nrKlastra)
    for krotka in klastry[nrKlastra]:
        print('%7.3f %7.3f %7.3f %3d %2d' % (krotka[0], krotka[1], krotka[2], krotka[3], krotka[4]))



def wypiszKlastry():
    # wypisuje do interpretera aktualne wartości wszystkich klastrów
    for numer in range(0, len(Centroidy)):
        wypiszKlaster(numer)


def newCentroide(klaster):
    # oblicza nowe położenie centroidy we wskazanym klastrze
    # i zwraca wynik w postaci nowej centroidy dla wskazanego klastra
    n = len(klaster)
    if n == 0:
        return losujCentroide()  # zabezpieczenie

    sum0 = sum1 = sum2 = sum3 = 0
    for krotka in klaster:
        sum0 += krotka[0]
        sum1 += krotka[1]
        sum2 += krotka[2]
        sum3 += krotka[3]
    return [
        sum0 / n,
        sum1 / n,
        sum2 / n,
        round(sum3 / n)
    ]


def newCentroidy():
    Centroidy.clear()
    print('\nprzesunięto centroidy ------------')  
    for nr in range(liczbaKlastrów):
        Centroidy.append(newCentroide(klastry[nr]))

def odleglosc(krotka, centroida):
    if metryka == 'euclidean':
        suma = 0
        for i in range(0, len(krotka) - 1):
            diff = centroida[i] - krotka[i]
            suma += diff * diff
        return suma
    elif metryka == 'manhattan':
        suma = 0
        for i in range(0, len(krotka) - 1):
            suma += abs(centroida[i] - krotka[i])
        return suma

def czy_centroidy_są_te_same(stare, nowe):
    for c1, c2 in zip(stare, nowe):
        for v1, v2 in zip(c1, c2):
            if abs(v1 - v2) > 1e-5:
                return False
    return True