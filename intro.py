# moduł przechowuje:
# oryginalne i znormalizowane krotki danych,
# słowniki normalizacyjne do zmiennych tekstowych,
# funkcje wczytywania i wypisywania krotek,
# funkcję normalizacji danych
# intro.py – wersja do etapu 2: segmentacja klientów na podstawie cleaned_customers.csv

def test():
    wczytajDane()
    normalizujDane()
    wypiszKrotkiNormal()

import csv

krotkiDane = []
krotkiNormal = []

country_dict = {
    'United Kingdom': 1, 'France': 2, 'Germany': 3, 'Australia': 4, 'Netherlands': 5,
    'Norway': 6, 'EIRE': 7, 'Switzerland': 8, 'Spain': 9, 'Poland': 10, 'Portugal': 11,
    'Italy': 12, 'Belgium': 13, 'Lithuania': 14, 'Japan': 15, 'Iceland': 16,
    'Channel Islands': 17, 'Denmark': 18, 'Cyprus': 19, 'Sweden': 20, 'Austria': 21,
    'Israel': 22, 'Finland': 23, 'Bahrain': 24, 'Greece': 25, 'Hong Kong': 26,
    'Singapore': 27, 'Lebanon': 28, 'United Arab Emirates': 29, 'Saudi Arabia': 30,
    'Czech Republic': 31, 'Canada': 32, 'Unspecified': 33, 'Brazil': 34, 'USA': 35,
    'European Community': 36, 'Malta': 37, 'RSA': 38
}



def wczytajDane():
    # wczytuje dane ze wskazanego pliku tekstowego do listy krotkiDane
    with open('cleaned_customers.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            krotka = [
    int(float(row['TotalQuantity'])),
    float(row['AvgUnitPrice']),
    int(float(row['CustomerSpanDays'])),
    int(row['CountryCode']) 
            ]
            krotkiDane.append(krotka)


def wypiszDane():
    # wypisuje zawartość listy krotkiDane do interpretera
    for krotka in krotkiDane:
        print('%4d %7.2f %4d %3d' % (krotka[0], krotka[1], krotka[2], krotka[3]))


def wypiszKrotkiNormal():
    # wypisuje zawartość listy krotkiNormal do interpretera
    print('KROTKI NORMAL')
    for krotka in krotkiNormal:
        print('%7.3f %7.3f %7.3f %3d %2d' % (krotka[0], krotka[1], krotka[2], krotka[3], krotka[4]))

def normalizujDane():
    # normalizuje dane surowe z listy *krotki* i wpisuje je do listy *krotkiNormal*
    # -1 oznacza, że nie wpisano jeszcze numeru klastra, do którego należy krotka
    # znajdź min i max dla każdej cechy (bez CountryCode)
     
    min_vals = [min([k[i] for k in krotkiDane]) for i in range(3)]
    max_vals = [max([k[i] for k in krotkiDane]) for i in range(3)]

    for dane in krotkiDane:
        krotka = []
        for i in range(3):
            if max_vals[i] != min_vals[i]:
                norm = (dane[i] - min_vals[i]) / (max_vals[i] - min_vals[i])
            else:
                norm = 0.0  # wszystkie wartości jednakowe nie dzielimy przez 0
            krotka.append(norm)
        krotka.append(dane[3])  # zakodowany kraj (bez normalizacji)
        krotka.append(-1)       # klaster
        krotkiNormal.append(krotka)