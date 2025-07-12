import intro
import calcul

calcul.metryka = 'manhattan'#'euclidean' ,'manhattan'
maks_iteracji = 100  # w zależności od rozmiaru danych

def main():
    print('\nLICZBA KLASTRÓW ', calcul.liczbaKlastrów)
    intro.wczytajDane()
    intro.normalizujDane()
    calcul.losujCentroidy()
    calcul.wypiszCentroidy()
    calcul.przypiszKrotkomNumeryKlastrów()
    calcul.utwórzKlastry()
    # calcul.wypiszKlastry()

    # klasteryzacja zatrzyma się wcześniej, jeśli centroidy już się nie zmieniają
    repeat = 0
    while repeat < maks_iteracji:
        stare = calcul.Centroidy.copy()
        calcul.newCentroidy()
        calcul.wypiszCentroidy()
        calcul.przypiszKrotkomNumeryKlastrów()
        calcul.utwórzKlastry()
        #calcul.wypiszKlastry()

        if calcul.czy_centroidy_są_te_same(stare, calcul.Centroidy):
            print(f"Centroidy ustabilizowały się po {repeat + 1} iteracjach.")
            break
        else:
            repeat += 1

    # Jeśli pętla zakończyła się bez wcześniejszego przerwania:
    if repeat == maks_iteracji:
        print(f"Osiągnięto maksymalną liczbę iteracji: {maks_iteracji}")