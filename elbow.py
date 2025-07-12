import intro
import calcul
import matplotlib.pyplot as plt

def metoda_lokcia(metryka, k_min=1, k_max=10):
    sse_lista = []

    for k in range(k_min, k_max + 1):
        calcul.liczbaKlastrów = k
        calcul.Centroidy.clear()
        calcul.klastry.clear()
        intro.krotkiNormal.clear()
        intro.krotkiDane.clear()

        intro.wczytajDane()
        intro.normalizujDane()

        calcul.metryka = metryka

        calcul.losujCentroidy()
        for _ in range(10):
            calcul.przypiszKrotkomNumeryKlastrów()
            calcul.utwórzKlastry()
            calcul.newCentroidy()

        # SSE 
        suma_sse = 0
        for i, klaster in enumerate(calcul.klastry):
            for krotka in klaster:
                suma_sse += calcul.odleglosc(krotka, calcul.Centroidy[i])
        sse_lista.append(suma_sse)

    return list(range(k_min, k_max + 1)), sse_lista

def znajdz_lokiec(sse_lista):
    
    max_diff = -1
    opt_k = 1
    for i in range(1, len(sse_lista) - 1):
        prev_drop = sse_lista[i - 1] - sse_lista[i]
        next_drop = sse_lista[i] - sse_lista[i + 1]
        diff = abs(prev_drop - next_drop)
        if diff > max_diff:
            max_diff = diff
            opt_k = i + 1  
    return opt_k

#SSE
k_vals, sse_eu = metoda_lokcia('euclidean')
_, sse_man = metoda_lokcia('manhattan')

lokiec_eu = znajdz_lokiec(sse_eu)
lokiec_man = znajdz_lokiec(sse_man)

plt.figure(figsize=(9, 5))
plt.plot(k_vals, sse_eu, marker='o', label='Euklidesowa', color='blue')
plt.plot(k_vals, sse_man, marker='s', label='Manhattan', color='green')

plt.axvline(x=lokiec_eu, color='blue', linestyle='--', label=f'Łokieć EU: k={lokiec_eu}')
plt.axvline(x=lokiec_man, color='green', linestyle='--', label=f'Łokieć MAN: k={lokiec_man}')

plt.title("Metoda łokcia – porównanie metryk")
plt.xlabel("Liczba klastrów (k)")
plt.ylabel("Suma odległości (SSE)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()